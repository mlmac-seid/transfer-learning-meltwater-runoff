#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:38:14 2026

@author: mlm211

Pre-train MLP with Rio Behar catchment-scale MAR t2m and al2 for 2000-2021.
"""

import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import MeanSquaredError
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score as R2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import models, layers
from datetime import datetime, timedelta
import geopandas as gpd
import joblib

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')

# Load 2000-2024 MAR data for Rio Behar
rb_mar = pd.read_csv('./Rio_Behar_catchment_variables/rb_catchment_2000_2024_vars.csv')

# Select predictors
t2m_ts_al2_swd = ['air_temp', 'ice_temp', 'albedo', 'shortwave_down']

# Fit scalers
x_scaler = StandardScaler().fit(rb_mar[t2m_ts_al2_swd])
y_scaler = StandardScaler().fit(rb_mar[["meltwater_runoff"]])

# # Scale training data
x_train = x_scaler.transform(rb_mar[t2m_ts_al2_swd])
y_train_scaled = y_scaler.transform(
    rb_mar[["meltwater_runoff"]]).flatten()

nodes_tl = 64
activation_tl = 'relu'
dropout_tl = 0.2
loss_tl = MeanSquaredError()
optimizer_tl = Adam
learning_rate_tl = 0.001
epochs_tl = 1000

input_shape_tl = (x_train.shape[1],)
mlp_tl = tf.keras.Sequential([
    tf.keras.layers.Input(shape=input_shape_tl),
    tf.keras.layers.Dense(nodes_tl, activation=activation_tl),
    tf.keras.layers.Dropout(dropout_tl),
    tf.keras.layers.Dense(nodes_tl, activation=activation_tl),
    tf.keras.layers.Dropout(dropout_tl),
    tf.keras.layers.Dense(nodes_tl, activation=activation_tl),
    tf.keras.layers.Dropout(dropout_tl),
    tf.keras.layers.Dense(nodes_tl, activation=activation_tl),
    tf.keras.layers.Dropout(dropout_tl),
    tf.keras.layers.Dense(1)])

mlp_tl.compile(loss=loss_tl, optimizer=optimizer_tl(
    learning_rate=learning_rate_tl))
early_stopping_tl = EarlyStopping(
    monitor='loss', patience=20, restore_best_weights=True)

# Fit model
mlp_tl.fit(x_train, y_train_scaled, epochs=epochs_tl,
           callbacks=[early_stopping_tl], verbose=1)

# Save trained model for transfer learning
save_path_tl = './catchment_MAR_emulators/rb_mar_mlp.keras'
if os.path.exists(save_path_tl):
    os.remove(save_path_tl)
mlp_tl.save(save_path_tl)

# Save scalers
joblib.dump(
    x_scaler, './catchment_MAR_emulators/rb_mar_xscaler.pkl')
joblib.dump(
    y_scaler, './catchment_MAR_emulators/rb_mar_yscaler.pkl')

