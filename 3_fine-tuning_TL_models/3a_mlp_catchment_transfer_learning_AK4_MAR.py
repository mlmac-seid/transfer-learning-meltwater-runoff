#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:36:16 2026

@author: mlm211

Conduct transfer learning on catchment-scale MLPs with AK4 in-situ observations and catchment-scale MAR data.
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
    './catchment_MAR_emulators/ak4_mar_mlp.keras')

# Load in-situ AK4 discharge data
tab_path = "../in-situ data/AK-004-001_river_discharge.tab"
ak4_discharge = pd.read_csv(tab_path, sep="\t", skiprows=26, engine="python")

# Make datetime column for AK4 discharge
ak4_discharge['time'] = pd.to_datetime(
    ak4_discharge['Date/Time'], utc=True, errors='coerce')
ak4_discharge = ak4_discharge.drop(columns=['Date/Time'])

# Rename discharge column
ak4_discharge = ak4_discharge.rename(columns={'Q [m**3/s]': 'discharge_m3s'})

# Drop rows with bad times or discharge
ak4_discharge['time'] = pd.to_datetime(
    ak4_discharge['time'], utc=True, errors='coerce')
ak4_discharge['discharge_m3s'] = pd.to_numeric(
    ak4_discharge['discharge_m3s'], errors='coerce')
ak4_discharge = ak4_discharge.dropna(
    subset=['time', 'discharge_m3s']).sort_values('time').reset_index(drop=True)

# Compute per-sample volume (Q * dt), then sum to daily volume (m^3/day)
# Compute forward time delta (seconds) to next sample; fill last with median dt
ak4_discharge['dt_s'] = (ak4_discharge['time'].shift(-1) -
                         ak4_discharge['time']).dt.total_seconds()
median_dt = int(ak4_discharge['dt_s'].median(skipna=True)) if not np.isnan(
    ak4_discharge['dt_s'].median(skipna=True)) else 3600
ak4_discharge['dt_s'] = ak4_discharge['dt_s'].fillna(median_dt)
ak4_discharge['volume_m3'] = ak4_discharge['discharge_m3s'] * \
    ak4_discharge['dt_s']

# Aggregate to daily volume (m^3/day) using UTC day
ak4_discharge['date'] = ak4_discharge['time'].dt.date
ak4_daily_discharge = (ak4_discharge.groupby('date', as_index=False)[
                       'volume_m3'].sum().rename(columns={'volume_m3': 'dailyQ'}))

# Load catchment-scale MAR data for 2008-2016
mar_catchment_2008 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2008_vars.csv')
mar_catchment_2009 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2009_vars.csv')
mar_catchment_2010 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2010_vars.csv')
mar_catchment_2011 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2011_vars.csv')
mar_catchment_2012 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2012_vars.csv')
mar_catchment_2013 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2013_vars.csv')
mar_catchment_2014 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2014_vars.csv')
mar_catchment_2015 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2015_vars.csv')
mar_catchment_2016 = pd.read_csv(
    'AK4_catchment_variables/ak4_catchment_2016_vars.csv')

# Load catchment delineation
ak4_catchment_delineation = gpd.read_file('/Users/mlm211/Documents/DeepMelt/in-situ data/AK4_basin_delineation.shp')
# Reproject to EPSG:3413
ak4_proj = ak4_catchment_delineation.to_crs(epsg=3413)

# Get predictors from MAR
mar_vars_2008 = mar_catchment_2008[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2009 = mar_catchment_2009[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2010 = mar_catchment_2010[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2011 = mar_catchment_2011[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2012 = mar_catchment_2012[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2013 = mar_catchment_2013[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2014 = mar_catchment_2014[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2015 = mar_catchment_2015[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})
mar_vars_2016 = mar_catchment_2016[['time', 'air_temp', 'ice_temp', 'albedo', 'shortwave_down']].rename(
    columns={'air_temp': 't2m',
             'ice_temp': 'ts',
             'albedo': 'al2',
             'shortwave_down': 'swd'})

mar_vars = pd.concat([mar_vars_2008, mar_vars_2009, mar_vars_2010, mar_vars_2011, mar_vars_2012,
                     mar_vars_2013, mar_vars_2014, mar_vars_2015, mar_vars_2016], axis=0).reset_index(drop=True)

# Merge MAR daily to daily discharge (right join keeps days with discharge)
mar_vars['time'] = pd.to_datetime(mar_vars['time'], utc=True, errors='coerce')
mar_vars['date'] = mar_vars['time'].dt.date
mar_vars = mar_vars.drop(columns=['time'])
ak4_mar_tl = pd.merge(mar_vars, ak4_daily_discharge,
                      on='date', how='right').reset_index(drop=True)

# Drop rows missing data
ak4_mar_tl = ak4_mar_tl.dropna(
    subset=['t2m', 'al2', 'dailyQ']).reset_index(drop=True)

# Convert daily volume (m^3/day) -> runoff (mm/day)
ak4_catchment_area = ak4_proj.geometry.area.iloc[0]  # m^2
# mm/day = (m^3/day) / (m^2) * 1000
ak4_mar_tl['runoff'] = (ak4_mar_tl['dailyQ'] /
                        ak4_catchment_area) * 1000.0  # mm/day

# Artificially create a week of winter data from MAR data for 2008-2016
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

winter_2008_df = make_winter_week_df(mar_catchment_2008)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2008_df],
    ignore_index=True
)

winter_2009_df = make_winter_week_df(mar_catchment_2009)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2009_df],
    ignore_index=True
)

winter_2010_df = make_winter_week_df(mar_catchment_2010)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2010_df],
    ignore_index=True
)

winter_2011_df = make_winter_week_df(mar_catchment_2011)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2011_df],
    ignore_index=True
)

winter_2012_df = make_winter_week_df(mar_catchment_2012)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2012_df],
    ignore_index=True
)

winter_2013_df = make_winter_week_df(mar_catchment_2013)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2013_df],
    ignore_index=True
)

winter_2014_df = make_winter_week_df(mar_catchment_2014)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2014_df],
    ignore_index=True
)

winter_2015_df = make_winter_week_df(mar_catchment_2015)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2015_df],
    ignore_index=True
)

winter_2016_df = make_winter_week_df(mar_catchment_2016)
ak4_mar_tl = pd.concat(
    [ak4_mar_tl, winter_2016_df],
    ignore_index=True
)

# Define output directory to save AK4 runoff data (change as needed)
# output_dir_data = "/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment in-situ data"
# Output directory on personal computer:
output_dir_data = "/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment in-situ data"

# Create the directory if it doesn't exist
os.makedirs(output_dir_data, exist_ok=True)

# File name (with path) to save AK4 runoff data
ak4_mar_tl_file_name = os.path.join(
    output_dir_data, "ak4_catchment_mar_tl.csv")

# Delete old AK4 runoff data csv file if it exists
if os.path.exists(ak4_mar_tl_file_name):
    os.remove(ak4_mar_tl_file_name)

# Save AK4 runoff data to CSV
ak4_mar_tl.to_csv(ak4_mar_tl_file_name, index=False)

# Create training sets from AK4 data with MAR variables
t2m_ts_al2_swd = ['t2m', 'ts', 'al2', 'swd']
ak4_mar_x_train = ak4_mar_tl[t2m_ts_al2_swd]
ak4_mar_y_train = ak4_mar_tl['runoff']

# Scale new data
scaler_x = StandardScaler()
scaler_y = StandardScaler()

ak4_x_train_scaled = scaler_x.fit_transform(ak4_mar_x_train)
ak4_y_train_scaled = scaler_y.fit_transform(
    ak4_mar_y_train.values.reshape(-1, 1))

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

# Retrain last layer on AK4 data with MAR variables
mlp_catchment_tl.fit(
    ak4_x_train_scaled, ak4_y_train_scaled, epochs=1000)

# ensure model save dir exists
os.makedirs('catchment_TL_models', exist_ok=True)

# Save transfer learned models on Rio Behar data with MAR variables
if os.path.exists('catchment_TL_models/mlp_catchment_tl_ak4_mar.keras'):
    os.remove(
        'catchment_TL_models/mlp_catchment_tl_ak4_mar.keras')
mlp_catchment_tl.save(
    'catchment_TL_models/mlp_catchment_tl_ak4_mar.keras')
