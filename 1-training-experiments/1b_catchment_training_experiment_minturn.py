#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:04:50 2026

@author: mlm211

Run MLP on all years of Minturn catchment-scale data to predict a random year.
"""


import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam, SGD
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score as R2
import matplotlib.pyplot as plt
from catchment_training_experiments_log import log_catchment_training_experiment, catchment_training_log_minturn
from datetime import datetime
import joblib

# Set start time for script runtime
start_time = datetime.now()

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
# On personal computer:
# os.chdir('/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale')

# Load in data for 2000-2024
minturn_catchment_2000_2024_df = pd.read_csv(
    "./Minturn_catchment_variables/minturn_catchment_2000_2024_vars.csv")
minturn_catchment_2000_2024_df['time'] = pd.to_datetime(
    minturn_catchment_2000_2024_df['time'], errors='coerce')

for i in range(100):
    # Randomly select a year to be predicted
    years = np.arange(2000, 2022)
    random_year = int(np.random.choice(years, size=1))
    remaining_years = [y for y in years if y != random_year]
    withheld_mask = minturn_catchment_2000_2024_df['time'].dt.year == random_year
    test_random = minturn_catchment_2000_2024_df[withheld_mask].reset_index(
        drop=True)

    # Create training sets for each N (excluding withheld year)
    training_sets = {}
    for N in range(1, len(remaining_years) + 1):
        train_years = np.random.choice(remaining_years, size=N, replace=False)
        train_mask = minturn_catchment_2000_2024_df['time'].dt.year.isin(
            train_years)
        train_df = minturn_catchment_2000_2024_df[train_mask].reset_index(drop=True)
        globals()[f"train_N{N}_df"] = train_df
        training_sets[N] = train_df

    def mlp(x_train, x_test, y_train, y_test, y_scaler,
            nodes, activation, dropout, loss, optimizer,
            learning_rate, epochs, N):

        # define model type to be returned
        mlp_type = 'random_year'

        input_shape = (x_train.shape[1],)
        mlp = tf.keras.Sequential([
            tf.keras.layers.Input(shape=input_shape),
            tf.keras.layers.Dense(nodes, activation=activation),
            tf.keras.layers.Dropout(dropout),
            tf.keras.layers.Dense(nodes, activation=activation),
            tf.keras.layers.Dropout(dropout),
            tf.keras.layers.Dense(nodes, activation=activation),
            tf.keras.layers.Dropout(dropout),
            tf.keras.layers.Dense(nodes, activation=activation),
            tf.keras.layers.Dropout(dropout),
            tf.keras.layers.Dense(1)])

        mlp.compile(loss=loss, optimizer=optimizer(
            learning_rate=learning_rate))
        early_stopping = EarlyStopping(
            monitor='loss', patience=20, restore_best_weights=True)

        # Fit model
        mlp_fit = mlp.fit(x_train, y_train, epochs=epochs,
                          callbacks=[early_stopping], verbose=1)

        # Predict (scaled)
        y_pred_scaled = mlp.predict(x_test, verbose=0)
        
        # Inverse transform predictions and observations
        y_pred = y_scaler.inverse_transform(y_pred_scaled).flatten()
        y_test_orig = y_scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
        
        # MSE and R^2 in original units
        mse_test = np.mean((y_test_orig - y_pred) ** 2)
        R_2 = R2(y_test_orig, y_pred)

        # Total observed runoff
        obs_mru = np.sum(y_test_orig)
        # Total predicted runoff
        pred_mru = np.sum(y_pred)
        # Proportion of total runoff predicted by MLP
        prop_mru_modeled = pred_mru / obs_mru

        # Print summary
        print(mlp.summary())
        print(f"\n--- Results for N={N} ---")
        print(f"MSE test: {mse_test:.4f}")
        print(f"R² test: {R_2:.4f}")
        print(f"Observed total runoff: {obs_mru:.2f}")
        print(f"Predicted total runoff: {pred_mru:.2f}")
        print(f"Proportion modeled: {prop_mru_modeled:.3f}\n")

        # Plot observed vs. predicted
        # plt.figure(figsize=(10, 6))
        # plt.plot(y_test_orig, label="Observed runoff", marker='o')
        # plt.plot(y_pred, label="Predicted runoff", marker='x')
        # plt.xlabel("Sample index (time steps)")
        # plt.ylabel("Meltwater runoff")
        # plt.title(f"Observed vs Predicted Meltwater Runoff | N={N} years")
        # plt.legend()
        # plt.tight_layout()
        # plt.show()

        # Plot learning curve
        # plt.figure(figsize=(8, 4))
        # plt.plot(mlp_fit.history['loss'], label='Training loss')
        # plt.xlabel('Epochs')
        # plt.ylabel('MSE')
        # plt.title(f"Training Loss Curve | N={N} years")
        # plt.legend()
        # plt.tight_layout()
        # plt.show()

        return (mlp_type, nodes, activation, dropout,
                optimizer, learning_rate, epochs, mse_test,
                R_2, obs_mru, pred_mru, prop_mru_modeled)

    # Run MLPs for surface energy balance:
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        x_scaler = StandardScaler().fit(df[["surface_energy_balance"]])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[["surface_energy_balance"]])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(
            test_random[["surface_energy_balance"]])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with surface energy balance predicting a random year
        seb_run = mlp(x_train=x_train,
                      x_test=x_test_scaled,
                      y_train=y_train_scaled,
                      y_test=y_test_scaled,
                      y_scaler=y_scaler,
                      nodes=64,
                      activation='relu',
                      dropout=0.2,
                      loss=MeanSquaredError(),
                      optimizer=Adam,
                      learning_rate=0.001,
                      epochs=1000,
                      N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = seb_run

        # Log results for MLP with surface energy balance predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_seb",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)

    # Run MLPs for air temperature
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        x_scaler = StandardScaler().fit(df[["air_temp"]])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[["air_temp"]])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[["air_temp"]])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature predicting a random year
        t2m_run = mlp(x_train=x_train,
                      x_test=x_test_scaled,
                      y_train=y_train_scaled,
                      y_test=y_test_scaled,
                      y_scaler=y_scaler,
                      nodes=64,
                      activation='relu',
                      dropout=0.2,
                      loss=MeanSquaredError(),
                      optimizer=Adam,
                      learning_rate=0.001,
                      epochs=1000,
                      N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_run

        # Log results for MLP with air temperature predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)

    # Run MLPs for air temperature and albedo
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        t2m_al2 = ['air_temp', 'albedo']
        x_scaler = StandardScaler().fit(df[t2m_al2])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[t2m_al2])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[t2m_al2])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature and albedo predicting a random year
        t2m_al2_run = mlp(x_train=x_train,
                          x_test=x_test_scaled,
                          y_train=y_train_scaled,
                          y_test=y_test_scaled,
                          y_scaler=y_scaler,
                          nodes=64,
                          activation='relu',
                          dropout=0.2,
                          loss=MeanSquaredError(),
                          optimizer=Adam,
                          learning_rate=0.001,
                          epochs=1000,
                          N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_al2_run

        # Log results for MLP with air temperature and albedo predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m_al2",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)

    # Run MLPs for air temperature and ice temperature
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        t2m_ts = ['air_temp', 'ice_temp']
        x_scaler = StandardScaler().fit(df[t2m_ts])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[t2m_ts])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[t2m_ts])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature and ice temperature predicting a random year
        t2m_ts_run = mlp(x_train=x_train,
                         x_test=x_test_scaled,
                         y_train=y_train_scaled,
                         y_test=y_test_scaled,
                         y_scaler=y_scaler,
                         nodes=64,
                         activation='relu',
                         dropout=0.2,
                         loss=MeanSquaredError(),
                         optimizer=Adam,
                         learning_rate=0.001,
                         epochs=1000,
                         N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_ts_run

        # Log results for MLP with air temperature and ice temperature predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m_ts",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)

    # Run MLPs for air temperature, ice temperature, and albedo
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        t2m_ts_al2 = ['air_temp', 'ice_temp', 'albedo']
        x_scaler = StandardScaler().fit(df[t2m_ts_al2])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[t2m_ts_al2])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[t2m_ts_al2])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature, ice temperature, and albedo predicting a random year
        t2m_ts_al2_run = mlp(x_train=x_train,
                             x_test=x_test_scaled,
                             y_train=y_train_scaled,
                             y_test=y_test_scaled,
                             y_scaler=y_scaler,
                             nodes=64,
                             activation='relu',
                             dropout=0.2,
                             loss=MeanSquaredError(),
                             optimizer=Adam,
                             learning_rate=0.001,
                             epochs=1000,
                             N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_ts_al2_run

        # Log results for MLP with air temperature, ice temperature, and albedo predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m_ts_al2",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)
    
    # Run MLPs for air temperature and shortwave down
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        t2m_swd = ['air_temp', 'shortwave_down']
        x_scaler = StandardScaler().fit(df[t2m_swd])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[t2m_swd])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[t2m_swd])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature and ice temperature predicting a random year
        t2m_swd_run = mlp(x_train=x_train,
                         x_test=x_test_scaled,
                         y_train=y_train_scaled,
                         y_test=y_test_scaled,
                         y_scaler=y_scaler,
                         nodes=64,
                         activation='relu',
                         dropout=0.2,
                         loss=MeanSquaredError(),
                         optimizer=Adam,
                         learning_rate=0.001,
                         epochs=1000,
                         N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_swd_run

        # Log results for MLP with air temperature and ice temperature predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m_swd",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)
    
    # Run MLPs for air temperature and ice temperature, albedo, and shortwave down
    for N, df in training_sets.items():
        # Fit scalers on current training subset
        t2m_ts_al2_swd = ['air_temp', 'ice_temp', 'albedo', 'shortwave_down']
        x_scaler = StandardScaler().fit(df[t2m_ts_al2_swd])
        y_scaler = StandardScaler().fit(df[["meltwater_runoff"]])

        # Scale training data
        x_train = x_scaler.transform(df[t2m_ts_al2_swd])
        y_train_scaled = y_scaler.transform(df[["meltwater_runoff"]]).flatten()

        # Scale withheld test year with the same scalers
        x_test_scaled = x_scaler.transform(test_random[t2m_ts_al2_swd])
        y_test_scaled = y_scaler.transform(
            test_random[["meltwater_runoff"]]).flatten()

        # MLP with air temperature and ice temperature predicting a random year
        t2m_ts_al2_swd_run = mlp(x_train=x_train,
                         x_test=x_test_scaled,
                         y_train=y_train_scaled,
                         y_test=y_test_scaled,
                         y_scaler=y_scaler,
                         nodes=64,
                         activation='relu',
                         dropout=0.2,
                         loss=MeanSquaredError(),
                         optimizer=Adam,
                         learning_rate=0.001,
                         epochs=1000,
                         N=N)

        (mlp_type, nodes, activation, dropout, optimizer,
         learning_rate, epochs, mse_full, R_2,
         obs_mru, pred_mru, prop_mru_modeled) = t2m_ts_al2_swd_run

        # Log results for MLP with air temperature and ice temperature predicting a random year
        log_catchment_training_experiment(log_file=catchment_training_log_minturn,
                                               mlp_type=f"N{N}_{mlp_type}",
                                               training_size=N,
                                               predictors="x_t2m_ts_al2_swd",
                                               nodes=nodes,
                                               activation=activation,
                                               dropout=dropout,
                                               optimizer=optimizer,
                                               learning_rate=learning_rate,
                                               epochs=epochs,
                                               mse_full=mse_full,
                                               R_2=R_2,
                                               obs_mru=obs_mru,
                                               pred_mru=pred_mru,
                                               prop_mru_modeled=prop_mru_modeled)

# Determine and print script runtime
end_time = datetime.now()
elapsed_time = end_time - start_time
print(f"\nScript completed in: {elapsed_time}\n")
