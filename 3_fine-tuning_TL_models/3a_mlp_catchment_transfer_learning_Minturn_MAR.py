#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:13:47 2026

@author: mlm211

Conduct transfer learning on catchment-scale MLPs with Minturn in-situ observations and catchment-scale MAR data.
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
#os.chdir('/Users/maya/Documents/Duke University/DeepMelt/catchment-scale')

# Load pre-trained catchment-scale MLP
mlp_catchment_tl = tf.keras.models.load_model(
    './catchment_MAR_emulators/minturn_mar_mlp.keras')

# Load Minturn discharge
minturn_discharge = pd.read_csv('/Users/mlm211/Documents/DeepMelt/in-situ data/minturn_daily_flow.csv')

# Load MAR data
mar_catchment_2019 = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/Minturn_catchment_variables/minturn_catchment_2019_vars.csv')
mar_catchment_2020 = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/Minturn_catchment_variables/minturn_catchment_2020_vars.csv')
mar_catchment_2021 = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/Minturn_catchment_variables/minturn_catchment_2021_vars.csv')
mar_catchment_2022 = pd.read_csv(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/Minturn_catchment_variables/minturn_catchment_2022_vars.csv')

# Load catchment delineation
minturn_catchment_delineation = gpd.read_file('/Users/mlm211/Documents/DeepMelt/in-situ data/minturn_basin.shp')
# Reproject to EPSG:3413
minturn_proj = minturn_catchment_delineation.to_crs(epsg=3413)

# Convert DateTime column to datetime
minturn_discharge['time'] = pd.to_datetime(minturn_discharge['DateTime'])
minturn_discharge = minturn_discharge.drop(columns=['DateTime'])
minturn_discharge['date'] = minturn_discharge['time'].dt.date


# Get predictors from MAR
mar_vars_2019 = mar_catchment_2019[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2019 = mar_vars_2019.rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2020 = mar_catchment_2020[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2020 = mar_vars_2020.rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2021 = mar_catchment_2021[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2021 = mar_vars_2021.rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2022 = mar_catchment_2022[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']]
mar_vars_2022 = mar_vars_2022.rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})

mar_vars = pd.concat([mar_vars_2019, 
                      mar_vars_2020, 
                      mar_vars_2021, 
                      mar_vars_2022], axis=0).reset_index(drop=True)

# Merge MAR daily variables to daily discharge (right join keeps days with discharge)
mar_vars['time'] = pd.to_datetime(mar_vars['time'], utc=True, errors='coerce')
mar_vars['date'] = mar_vars['time'].dt.date
mar_vars = mar_vars.drop(columns=['time'])
minturn_mar_tl = pd.merge(mar_vars, minturn_discharge,
                          on='date', how='right').reset_index(drop=True)
minturn_mar_tl = minturn_mar_tl.rename(columns={"Flow(m3/s)": "dailyQ"})

# Convert daily average Q to daily total Q
minturn_mar_tl['dailyQ'] = minturn_mar_tl['dailyQ'] * 86400

# Drop rows missing data
minturn_mar_tl = minturn_mar_tl.dropna().reset_index(drop=True)

# Convert daily volume (m^3/day) -> runoff
minturn_catchment_area = minturn_proj.geometry.area.iloc[0] # m^2
minturn_mar_tl['runoff'] = (minturn_mar_tl['dailyQ'] / 
                            minturn_catchment_area) * 1000.0 # mm/day

# Artificially create a week of winter data from MAR data for 2019-2020
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

winter_2019_df = make_winter_week_df(mar_catchment_2019)
minturn_mar_tl = pd.concat(
    [minturn_mar_tl, winter_2019_df],
    ignore_index=True
)

winter_2020_df = make_winter_week_df(mar_catchment_2020)
minturn_mar_tl = pd.concat(
    [minturn_mar_tl, winter_2020_df],
    ignore_index=True
)

winter_2021_df = make_winter_week_df(mar_catchment_2021)
minturn_mar_tl = pd.concat(
    [minturn_mar_tl, winter_2021_df],
    ignore_index=True
)

winter_2022_df = make_winter_week_df(mar_catchment_2022)
minturn_mar_tl = pd.concat(
    [minturn_mar_tl, winter_2022_df],
    ignore_index=True
)

# Define output directory to save Minturn runoff data
output_dir_data = "/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment in-situ data"
# Output directory on personal computer:
# output_dir_data = "/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment in-situ data"

# Create the directory if it doesn't exist
os.makedirs(output_dir_data, exist_ok=True)

# File name (with path) to save Minturn runoff data
minturn_mar_tl_file_name = os.path.join(
    output_dir_data, "minturn_catchment_mar_tl.csv")

# Delete old Minturn runoff data csv file if it exists
if os.path.exists(minturn_mar_tl_file_name):
    os.remove(minturn_mar_tl_file_name)

# Save Minturn runoff data to CSV
minturn_mar_tl.to_csv(minturn_mar_tl_file_name, index=False)

# Create training sets from Minturn data with MAR variables
t2m_ts_al2_swd = ['t2m', 'ts', 'al2', 'swd']
minturn_mar_x_train = minturn_mar_tl[t2m_ts_al2_swd]
minturn_mar_y_train = minturn_mar_tl['runoff']

# Scale new data
scaler_x = StandardScaler()
scaler_y = StandardScaler()

minturn_x_train_scaled = scaler_x.fit_transform(minturn_mar_x_train)
minturn_y_train_scaled = scaler_y.fit_transform(
    minturn_mar_y_train.values.reshape(-1, 1))

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

# Retrain last layer on Minturn data with MAR variables
mlp_catchment_tl.fit(
    minturn_x_train_scaled, minturn_y_train_scaled, epochs=1000)

# Save transfer learned models on Minturn data with MAR variables
if os.path.exists('catchment_TL_models/mlp_catchment_tl_minturn_mar.keras'):
    os.remove('catchment_TL_models/mlp_catchment_tl_minturn_mar.keras')
mlp_catchment_tl.save('catchment_TL_models/mlp_catchment_tl_minturn_mar.keras')