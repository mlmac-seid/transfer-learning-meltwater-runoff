#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:54:19 2026

@author: mlm211

Conduct transfer learning on catchment-scale MLPs with Rio Behar in-situ observations and 2015-2016 catchment-scale MAR data.
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

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
# Working directory on personal computer:
# os.chdir('/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale')

# Load pre-trained catchment-scale MLP
mlp_catchment_tl = tf.keras.models.load_model(
    './catchment_MAR_emulators/rb_mar_mlp.keras')

# Load 2015 Rio Behar supraglacial discharge
rio_behar_2015_discharge = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/in-situ data/Rio_Behar_2015_supraglacial_discharge.csv')

# Load 2016 Rio Behar supraglacial discharge
rio_behar_2016_discharge = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/in-situ data/Rio_Behar_2016_supraglacial_discharge.csv')

# Load MAR data
mar_catchment_2015 = pd.read_csv(
    'Rio_Behar_catchment_variables/rb_catchment_2015_vars.csv')
mar_catchment_2016 = pd.read_csv(
    'Rio_Behar_catchment_variables/rb_catchment_2016_vars.csv')

# Load catchment delineation
rio_behar_catchment_delineation = gpd.read_file('/Users/mlm211/Documents/DeepMelt/in-situ data/rio_behar_basin_delineation.shp')
# Reproject to EPSG:3413
rio_behar_proj = rio_behar_catchment_delineation.to_crs(epsg=3413)

# Make datetime column for 2015 Rio Behar discharge
rio_behar_2015_discharge = rio_behar_2015_discharge.rename(columns={'startYear': 'year',
                                                                    'startMonth': 'month',
                                                                    'startDay': 'day',
                                                                    'startHour': 'hour'})
rio_behar_2015_discharge['time'] = pd.to_datetime(
    rio_behar_2015_discharge[['year', 'month', 'day', 'hour']])
rio_behar_2015_discharge = rio_behar_2015_discharge.drop(columns=['year',
                                                                  'month',
                                                                  'day',
                                                                  'hour'])

# Make datetime column for 2016 Rio Behar discharge
rio_behar_2016_discharge = rio_behar_2016_discharge.rename(columns={'startYear': 'year',
                                                                    'startMonth': 'month',
                                                                    'startDay': 'day',
                                                                    'startHour': 'hour'})
rio_behar_2016_discharge['time'] = pd.to_datetime(
    rio_behar_2016_discharge[['year', 'month', 'day', 'hour']])
rio_behar_2016_discharge = rio_behar_2016_discharge.drop(columns=['year',
                                                                  'month',
                                                                  'day',
                                                                  'hour'])


# Make new df of 2015 daily discharge
rio_behar_2015_discharge['date'] = rio_behar_2015_discharge['time'].dt.date
rio_behar_2015_daily_discharge = (rio_behar_2015_discharge.groupby('date', as_index=False)[
                                  'avgQ'].sum().rename(columns={'avgQ': 'dailyQ', 'date': 'time'}))

# Make new df of 2016 daily discharge
rio_behar_2016_discharge['date'] = rio_behar_2016_discharge['time'].dt.date
rio_behar_2016_daily_discharge = (rio_behar_2016_discharge.groupby('date', as_index=False)[
                                  'avgQ'].sum().rename(columns={'avgQ': 'dailyQ', 'date': 'time'}))


# Get variables from MAR
mar_vars_2015 = mar_catchment_2015[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2015 = mar_vars_2015.rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2016 = mar_catchment_2016[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2016 = mar_vars_2016.rename(
    columns={'air_temp': 't2m', 
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})

# Merge MAR variables to 2015 discharge
mar_vars_2015['time'] = pd.to_datetime(mar_vars_2015['time'])
rio_behar_2015_daily_discharge['time'] = pd.to_datetime(
    rio_behar_2015_daily_discharge['time'])
mar_vars_2015['date'] = mar_vars_2015['time'].dt.date
rio_behar_2015_daily_discharge['date'] = rio_behar_2015_daily_discharge['time'].dt.date
rio_behar_2015_mar_tl = pd.merge(mar_vars_2015, rio_behar_2015_daily_discharge,
                                 on='date', how='right').dropna().reset_index(drop=True)
rio_behar_2015_mar_tl = rio_behar_2015_mar_tl.drop(
    columns=['time_x', 'time_y'])

# Merge MAR variables to 2016 discharge
mar_vars_2016['time'] = pd.to_datetime(mar_vars_2016['time'])
rio_behar_2016_daily_discharge['time'] = pd.to_datetime(
    rio_behar_2016_daily_discharge['time'])
mar_vars_2016['date'] = mar_vars_2016['time'].dt.date
rio_behar_2016_daily_discharge['date'] = rio_behar_2016_daily_discharge['time'].dt.date
rio_behar_2016_mar_tl = pd.merge(mar_vars_2016, rio_behar_2016_daily_discharge,
                                 on='date', how='right').dropna().reset_index(drop=True)
rio_behar_2016_mar_tl = rio_behar_2016_mar_tl.drop(
    columns=['time_x', 'time_y'])

# Merge 2015 and 2016 data
rio_behar_mar_tl = pd.concat(
    [rio_behar_2015_mar_tl, rio_behar_2016_mar_tl], axis=0).reset_index(drop=True)

# Convert discharge (m^3/s) to runoff (mm/h) for Rio Behar
rio_behar_idc_area = rio_behar_proj.geometry.area.iloc[0]  # m^2
rio_behar_mar_tl['runoff'] = (
    rio_behar_mar_tl['dailyQ'] / rio_behar_idc_area) * 1000 * 3600

# Artificially create a week of winter data from MAR data for 2015-2016
def make_winter_week_df(mar_df):
    # Ensure datetime
    winter = mar_df.copy()
    winter['time'] = pd.to_datetime(winter['time'])

    # First 7 rows/days from MAR file
    winter = winter.sort_values('time').head(7)

    # Rename variables to match training dataframe
    winter_df = winter.rename(
        columns={
            'air_temp': 't2m',
            'ice_temp': 'ts',
            'albedo': 'al2',
            'shortwave_down': 'swd',
            'meltwater_runoff': 'runoff'
        }
    )

    # Keep only needed columns
    winter_df = winter_df[['time', 't2m', 'ts', 'al2', 'swd', 'runoff']]

    # Convert time to date
    winter_df['date'] = winter_df['time'].dt.date

    # Reorder columns
    winter_df = winter_df[['date', 't2m', 'ts', 'al2', 'swd', 'runoff']]

    return winter_df

winter_2015_df = make_winter_week_df(mar_catchment_2015)
rio_behar_mar_tl = pd.concat(
    [rio_behar_mar_tl, winter_2015_df],
    ignore_index=True
)

winter_2016_df = make_winter_week_df(mar_catchment_2016)
rio_behar_mar_tl = pd.concat(
    [rio_behar_mar_tl, winter_2016_df],
    ignore_index=True
)

# Define output directory to save Rio Behar runoff data (change as needed)
output_dir_data = "/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment in-situ data"

# Create the directory if it doesn't exist
os.makedirs(output_dir_data, exist_ok=True)

# File name (with path) to save Rio Behar runoff data
rio_behar_mar_tl_file_name = os.path.join(
    output_dir_data, "rio_behar_catchment_mar_tl.csv")

# Delete old Rio Behar runoff data csv file if it exists
if os.path.exists(rio_behar_mar_tl_file_name):
    os.remove(rio_behar_mar_tl_file_name)

# Save Rio Behar runoff data to CSV
rio_behar_mar_tl.to_csv(rio_behar_mar_tl_file_name, index=False)

# Create training sets from Rio Behar data with MAR variables
t2m_ts_al2_swd = ['t2m', 'ts', 'al2', 'swd']
rio_behar_mar_x_train = rio_behar_mar_tl[t2m_ts_al2_swd]
rio_behar_mar_y_train = rio_behar_mar_tl['runoff']

# Scale new data
scaler_x = StandardScaler()
scaler_y = StandardScaler()

rio_behar_mar_x_train_scaled = scaler_x.fit_transform(rio_behar_mar_x_train)
rio_behar_mar_y_train_scaled = scaler_y.fit_transform(
    rio_behar_mar_y_train.values.reshape(-1, 1))

# Freeze layers in each MLP except for the last layer
for layer in mlp_catchment_tl.layers[:-1]:
    layer.trainable = False

# Confirm only the last layer in each MLP is trainable
print('mlp_catchment_tl layers:')
for i, l in enumerate(mlp_catchment_tl.layers):
    print(f"{i}: {l.name}, trainable={l.trainable}")


# Recompile each MLP with only the trainable last layer
mlp_catchment_tl.compile(
    loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.001))

# Retrain last layer on Rio Behar data with MAR variables
mlp_catchment_tl.fit(
    rio_behar_mar_x_train_scaled, rio_behar_mar_y_train_scaled, epochs=1000)

# Save transfer learned models on Rio Behar data with MAR variables
if os.path.exists('catchment_TL_models/mlp_catchment_tl_rio_behar_mar.keras'):
    os.remove(
        'catchment_TL_models/mlp_catchment_tl_rio_behar_mar.keras')
mlp_catchment_tl.save(
    'catchment_TL_models/mlp_catchment_tl_rio_behar_mar.keras')
