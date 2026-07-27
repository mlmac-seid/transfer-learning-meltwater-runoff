#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:49:47 2026

@author: mlm211
"""


# Set working directory
import os
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm
import random
import matplotlib.dates as mdates

#os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
os.chdir('/Users/maya/Documents/Duke University/DeepMelt/catchment-scale')

"""
List of in-situ data to be predicted:

    Rio Behar:
        -07/20/2015-07/23/2015
        -07/05/2016-07/13/2016

    AK4:
        -06/08/2008-07/18/2016

    Minturn:
        -07/15/2019-09/29/2019
        -03/31/2020-09/30/2020
"""

# Load in-situ runoff data
rb_in_situ_runoff = pd.read_csv('./catchment in-situ data/rio_behar_catchment_mar_tl.csv')
ak4_in_situ_runoff = pd.read_csv('./catchment in-situ data/ak4_catchment_mar_tl.csv')
minturn_in_situ_runoff = pd.read_csv('./catchment in-situ data/minturn_catchment_mar_tl.csv')

# Make sure date columns are datetime
rb_in_situ_runoff['date'] = pd.to_datetime(rb_in_situ_runoff['date'])
ak4_in_situ_runoff['date'] = pd.to_datetime(ak4_in_situ_runoff['date'])
minturn_in_situ_runoff['date'] = pd.to_datetime(minturn_in_situ_runoff['date'])

# Make yearly dfs of in-situ data
rb_in_situ_2015 = rb_in_situ_runoff[rb_in_situ_runoff['date'].dt.year == 2015]
rb_in_situ_2016 = rb_in_situ_runoff[rb_in_situ_runoff['date'].dt.year == 2016]

ak4_in_situ_2008 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2008]
ak4_in_situ_2009 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2009]
ak4_in_situ_2010 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2010]
ak4_in_situ_2011 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2011]
ak4_in_situ_2012 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2012]
ak4_in_situ_2013 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2013]
ak4_in_situ_2014 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2014]
ak4_in_situ_2015 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2015]
ak4_in_situ_2016 = ak4_in_situ_runoff[ak4_in_situ_runoff['date'].dt.year == 2016]

minturn_in_situ_2019 = minturn_in_situ_runoff[minturn_in_situ_runoff['date'].dt.year == 2019]
minturn_in_situ_2020 = minturn_in_situ_runoff[minturn_in_situ_runoff['date'].dt.year == 2020]
minturn_in_situ_2021 = minturn_in_situ_runoff[minturn_in_situ_runoff['date'].dt.year == 2021]
minturn_in_situ_2022 = minturn_in_situ_runoff[minturn_in_situ_runoff['date'].dt.year == 2022]

# Select only summer values
rb_in_situ_2015 = rb_in_situ_2015.loc[
    (rb_in_situ_2015["date"] >= "2015-04-01") & (rb_in_situ_2015["date"] <= "2015-09-30")
].sort_values("date")
rb_in_situ_2016 = rb_in_situ_2016.loc[
    (rb_in_situ_2016["date"] >= "2016-04-01") & (rb_in_situ_2016["date"] <= "2016-09-30")
].sort_values("date")

ak4_in_situ_2008 = ak4_in_situ_2008.loc[
    (ak4_in_situ_2008["date"] >= "2008-04-01") & (ak4_in_situ_2008["date"] <= "2008-09-30")
].sort_values("date")
ak4_in_situ_2009 = ak4_in_situ_2009.loc[
    (ak4_in_situ_2009["date"] >= "2009-04-01") & (ak4_in_situ_2009["date"] <= "2009-09-30")
].sort_values("date")
ak4_in_situ_2010 = ak4_in_situ_2010.loc[
    (ak4_in_situ_2010["date"] >= "2010-04-01") & (ak4_in_situ_2010["date"] <= "2010-09-30")
].sort_values("date")
ak4_in_situ_2011 = ak4_in_situ_2011.loc[
    (ak4_in_situ_2011["date"] >= "2011-04-01") & (ak4_in_situ_2011["date"] <= "2011-09-30")
].sort_values("date")
ak4_in_situ_2012 = ak4_in_situ_2012.loc[
    (ak4_in_situ_2012["date"] >= "2012-04-01") & (ak4_in_situ_2012["date"] <= "2012-09-30")
].sort_values("date")
ak4_in_situ_2013 = ak4_in_situ_2013.loc[
    (ak4_in_situ_2013["date"] >= "2013-04-01") & (ak4_in_situ_2013["date"] <= "2013-09-30")
].sort_values("date")
ak4_in_situ_2014 = ak4_in_situ_2014.loc[
    (ak4_in_situ_2014["date"] >= "2014-04-01") & (ak4_in_situ_2014["date"] <= "2014-09-30")
].sort_values("date")
ak4_in_situ_2015 = ak4_in_situ_2015.loc[
    (ak4_in_situ_2015["date"] >= "2015-04-01") & (ak4_in_situ_2015["date"] <= "2015-09-30")
].sort_values("date")
ak4_in_situ_2016 = ak4_in_situ_2016.loc[
    (ak4_in_situ_2016["date"] >= "2016-04-01") & (ak4_in_situ_2016["date"] <= "2016-09-30")
].sort_values("date")

minturn_in_situ_2019 = minturn_in_situ_2019.loc[
    (minturn_in_situ_2019["date"] >= "2019-04-01") & (minturn_in_situ_2019["date"] <= "2019-09-30")
].sort_values("date")
minturn_in_situ_2020 = minturn_in_situ_2020.loc[
    (minturn_in_situ_2020["date"] >= "2020-04-01") & (minturn_in_situ_2020["date"] <= "2020-09-30")
].sort_values("date")
minturn_in_situ_2021 = minturn_in_situ_2021.loc[
    (minturn_in_situ_2021["date"] >= "2021-04-01") & (minturn_in_situ_2021["date"] <= "2021-09-30")
].sort_values("date")
minturn_in_situ_2022 = minturn_in_situ_2022.loc[
    (minturn_in_situ_2022["date"] >= "2022-04-01") & (minturn_in_situ_2022["date"] <= "2022-09-30")
].sort_values("date")

# Load MAR data for each summer
def load_and_prepare_mar_data(path):
    df = pd.read_csv(path)
    df["time"] = pd.to_datetime(df["time"])
    df = df.rename(columns={
        "air_temp": "t2m",
        "ice_temp": "ts",
        "albedo": "al2",
        "shortwave_down": "swd",
        "meltwater_runoff": "runoff"
    })
    return df

rb_2015_mar = load_and_prepare_mar_data('Rio_Behar_catchment_variables/rb_catchment_2015_vars.csv')
rb_2016_mar = load_and_prepare_mar_data('Rio_Behar_catchment_variables/rb_catchment_2016_vars.csv')

ak4_2008_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2008_vars.csv")
ak4_2009_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2009_vars.csv")
ak4_2010_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2010_vars.csv")
ak4_2011_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2011_vars.csv")
ak4_2012_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2012_vars.csv")
ak4_2013_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2013_vars.csv")
ak4_2014_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2014_vars.csv")
ak4_2015_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2015_vars.csv")
ak4_2016_mar = load_and_prepare_mar_data("AK4_catchment_variables/ak4_catchment_2016_vars.csv")

minturn_2019_mar = load_and_prepare_mar_data('Minturn_catchment_variables/minturn_catchment_2019_vars.csv')
minturn_2020_mar = load_and_prepare_mar_data("Minturn_catchment_variables/minturn_catchment_2020_vars.csv")
minturn_2021_mar = load_and_prepare_mar_data("Minturn_catchment_variables/minturn_catchment_2021_vars.csv")
minturn_2022_mar = load_and_prepare_mar_data("Minturn_catchment_variables/minturn_catchment_2022_vars.csv")

# Normalize MAR dates
for df in [
    rb_2015_mar, rb_2016_mar,
    ak4_2008_mar, ak4_2009_mar, ak4_2010_mar, ak4_2011_mar, ak4_2012_mar, ak4_2013_mar, ak4_2014_mar, ak4_2015_mar, ak4_2016_mar,
    minturn_2019_mar, minturn_2020_mar, minturn_2021_mar, minturn_2022_mar
]:
    df['date'] = df['time'].dt.normalize()

# Subset MAR to dates of in-situ data
rb_2015_mar = rb_2015_mar[rb_2015_mar['date'].isin(rb_in_situ_2015['date'])]
rb_2016_mar = rb_2016_mar[rb_2016_mar['date'].isin(rb_in_situ_2016['date'])]

ak4_2008_mar = ak4_2008_mar[ak4_2008_mar['date'].isin(ak4_in_situ_2008['date'])]
ak4_2009_mar = ak4_2009_mar[ak4_2009_mar['date'].isin(ak4_in_situ_2009['date'])]
ak4_2010_mar = ak4_2010_mar[ak4_2010_mar['date'].isin(ak4_in_situ_2010['date'])]
ak4_2011_mar = ak4_2011_mar[ak4_2011_mar['date'].isin(ak4_in_situ_2011['date'])]
ak4_2012_mar = ak4_2012_mar[ak4_2012_mar['date'].isin(ak4_in_situ_2012['date'])]
ak4_2013_mar = ak4_2013_mar[ak4_2013_mar['date'].isin(ak4_in_situ_2013['date'])]
ak4_2014_mar = ak4_2014_mar[ak4_2014_mar['date'].isin(ak4_in_situ_2014['date'])]
ak4_2015_mar = ak4_2015_mar[ak4_2015_mar['date'].isin(ak4_in_situ_2015['date'])]
ak4_2016_mar = ak4_2016_mar[ak4_2016_mar['date'].isin(ak4_in_situ_2016['date'])]

minturn_2019_mar = minturn_2019_mar[minturn_2019_mar['date'].isin(minturn_in_situ_2019['date'])]
minturn_2020_mar = minturn_2020_mar[minturn_2020_mar['date'].isin(minturn_in_situ_2020['date'])]
minturn_2021_mar = minturn_2021_mar[minturn_2021_mar['date'].isin(minturn_in_situ_2021['date'])]
minturn_2022_mar = minturn_2022_mar[minturn_2022_mar['date'].isin(minturn_in_situ_2022['date'])]

# Load transfer learning models
models = {
    "2015-2016 Rio Behar": tf.keras.models.load_model('catchment_TL_models/mlp_catchment_tl_rio_behar_mar.keras'),
    "2008-2016 AK4": tf.keras.models.load_model('catchment_TL_models/mlp_catchment_tl_ak4_mar.keras'),
    "2019-2022 Minturn": tf.keras.models.load_model('catchment_TL_models/mlp_catchment_tl_minturn_mar.keras')
}

# Load MAR emulators
mar_emulators = {
    "Rio Behar": tf.keras.models.load_model('catchment_MAR_emulators/rb_mar_mlp.keras'),
    "AK4": tf.keras.models.load_model('catchment_MAR_emulators/AK4_mar_mlp.keras'),
    "Minturn": tf.keras.models.load_model('catchment_MAR_emulators/minturn_mar_mlp.keras')
}

# Standardize feature names
def standardize_feature_names(df):
    rename_map = {"t2m": "air_temp",
                  "al2": "albedo",
                  "ts": "ice_temp",
                  "swd": "shortwave_down"}
    cols_to_rename = {k: v for k, v in rename_map.items() if k in df.columns}
    return df.rename(columns=cols_to_rename)

for name in [
    'rb_in_situ_2015', 'rb_in_situ_2016',
    'ak4_in_situ_2008', 'ak4_in_situ_2009', 'ak4_in_situ_2010', 'ak4_in_situ_2011',
    'ak4_in_situ_2012', 'ak4_in_situ_2013', 'ak4_in_situ_2014', 'ak4_in_situ_2015', 'ak4_in_situ_2016',
    'minturn_in_situ_2019', 'minturn_in_situ_2020', 'minturn_in_situ_2021', 'minturn_in_situ_2022',
    'rb_2015_mar', 'rb_2016_mar'
]:
    locals()[name] = standardize_feature_names(locals()[name])

# MAR emulator scalers
mar_emulator_scalers = {
    "Rio Behar": (
        joblib.load("catchment_MAR_emulators/rb_mar_xscaler.pkl"),
        joblib.load("catchment_MAR_emulators/rb_mar_yscaler.pkl")
    ),
    "AK4": (
        joblib.load("catchment_MAR_emulators/ak4_mar_xscaler.pkl"),
        joblib.load("catchment_MAR_emulators/ak4_mar_yscaler.pkl")
    ),
    "Minturn": (
        joblib.load("catchment_MAR_emulators/minturn_mar_xscaler.pkl"),
        joblib.load("catchment_MAR_emulators/minturn_mar_yscaler.pkl")
    ),
}

# Load TL training data
tl_training_sets = {
    "2015-2016 Rio Behar": pd.read_csv('catchment in-situ data/rio_behar_catchment_mar_tl.csv'),
    "2008-2016 AK4": pd.read_csv('catchment in-situ data/ak4_catchment_mar_tl.csv'),
    "2019-2022 Minturn": pd.read_csv('catchment in-situ data/minturn_catchment_mar_tl.csv')
}

TARGET = "runoff"

FEATURES_BY_TL_KEY = {
    "2015-2016 Rio Behar": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
    "2008-2016 AK4": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
    "2019-2022 Minturn": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
}

FEATURES_BY_MAR_KEY = {
    "Rio Behar": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
    "AK4": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
    "Minturn": ["air_temp", "ice_temp", "albedo", "shortwave_down"],
}

def rebuild_tl_scaler(df, feature_cols):
    df = standardize_feature_names(df)
    X = df[feature_cols]
    y = df[[TARGET]]
    return StandardScaler().fit(X), StandardScaler().fit(y)

tl_scalers = {}
for name, df in tl_training_sets.items():
    feature_cols = FEATURES_BY_TL_KEY[name]
    tl_scalers[name] = rebuild_tl_scaler(df, feature_cols)

results_df = pd.DataFrame(columns=[
    "Prediction Site",
    "Model",
    "Training Site",
    "In-situ Cumulative Runoff",
    "MAR Cumulative Runoff",
    "Model Predicted Cumulative Runoff",
    "MSE",
    "normalized MSE",
    "R^2",
    "NSE",
    "Error Rate"
])

EVAL_MODEL_MAP = {
    "2015 Rio Behar": {"mar_emulator": "Rio Behar", "tl": "2015-2016 Rio Behar"},
    "2016 Rio Behar": {"mar_emulator": "Rio Behar", "tl": "2015-2016 Rio Behar"},
    "2008 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2009 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2010 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2011 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2012 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2013 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2014 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2015 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2016 AK4": {"mar_emulator": "AK4", "tl": "2008-2016 AK4"},
    "2019 Minturn": {"mar_emulator": "Minturn", "tl": "2019-2022 Minturn"},
    "2020 Minturn": {"mar_emulator": "Minturn", "tl": "2019-2022 Minturn"},
    "2021 Minturn": {"mar_emulator": "Minturn", "tl": "2019-2022 Minturn"},
    "2022 Minturn": {"mar_emulator": "Minturn", "tl": "2019-2022 Minturn"}
}

def mc_dropout_predictions(model, scaler_x, scaler_y, X, n_runs=100):
    X_scaled = scaler_x.transform(X)
    preds = []

    for _ in range(n_runs):
        y_scaled = model(X_scaled, training=True)
        y = scaler_y.inverse_transform(y_scaled.numpy()).ravel()
        preds.append(y)

    preds = np.array(preds)
    mean = preds.mean(axis=0)
    lower = np.percentile(preds, 5, axis=0)
    upper = np.percentile(preds, 95, axis=0)

    return mean, lower, upper


def nse(obs, pred):
    obs = obs.flatten()
    pred = pred.flatten()
    return 1 - np.sum((obs - pred) ** 2) / np.sum((obs - np.mean(obs)) ** 2)


def evaluate_catchment(in_situ_df, mar_df, eval_label):
    global results_df

    assert eval_label in EVAL_MODEL_MAP, f"Unknown evaluation label: {eval_label}"

    mar_emulator_key = EVAL_MODEL_MAP[eval_label]["mar_emulator"]
    tl_key_for_plot = EVAL_MODEL_MAP[eval_label]["tl"]

    mar_feature_cols = FEATURES_BY_MAR_KEY[mar_emulator_key]

    eval_df = in_situ_df.dropna(subset=mar_feature_cols + [TARGET]).copy()

    X_mar = eval_df[mar_feature_cols]
    y_true = eval_df[[TARGET]].values

    mar_eval = mar_df.loc[mar_df["date"].isin(eval_df["date"])].sort_values("date")
    y_mar = mar_eval[[TARGET]].values

    mean_runoff = np.mean(y_true)

    mar_emulator = mar_emulators[mar_emulator_key]
    scaler_x_mar_emulator, scaler_y_mar_emulator = mar_emulator_scalers[mar_emulator_key]

    if X_mar.shape[1] != mar_emulator.input_shape[-1]:
        raise ValueError(
            f"{eval_label}: MAR emulator '{mar_emulator_key}' expects "
            f"{mar_emulator.input_shape[-1]} features, but got {X_mar.shape[1]} "
            f"from columns {mar_feature_cols}"
        )

    X_scaled = scaler_x_mar_emulator.transform(X_mar)
    y_pred_scaled = mar_emulator.predict(X_scaled, verbose=0)
    y_pred_mar_emulator = scaler_y_mar_emulator.inverse_transform(y_pred_scaled)

    mar_emulator_mean, mar_emulator_low, mar_emulator_high = mc_dropout_predictions(
        mar_emulator, scaler_x_mar_emulator, scaler_y_mar_emulator, X_mar
    )

    mse_mar_emulator = np.mean((y_true - y_pred_mar_emulator) ** 2)
    normalized_mse_mar_emulator = mse_mar_emulator / mean_runoff if mean_runoff != 0 else np.nan

    results_df.loc[len(results_df)] = {
        "Prediction Site": eval_label,
        "Model": f"{mar_emulator_key} MAR Emulator",
        "Training Site": mar_emulator_key,
        "In-situ Cumulative Runoff": np.cumsum(y_true)[-1],
        "MAR Cumulative Runoff": np.cumsum(y_mar)[-1],
        "Model Predicted Cumulative Runoff": np.cumsum(y_pred_mar_emulator)[-1],
        "MSE": mse_mar_emulator,
        "normalized MSE": normalized_mse_mar_emulator,
        "R^2": r2_score(y_true, y_pred_mar_emulator),
        "NSE": nse(y_true, y_pred_mar_emulator),
        "Error Rate": abs(np.cumsum(y_true)[-1] - np.cumsum(y_pred_mar_emulator)[-1]) / np.cumsum(y_true)[-1]
    }

    tl_pred_plot = None
    tl_low_plot = None
    tl_high_plot = None

    for tl_key, tl_model in models.items():
        tl_feature_cols = FEATURES_BY_TL_KEY[tl_key]

        missing_cols = [col for col in tl_feature_cols if col not in in_situ_df.columns]
        if missing_cols:
            continue

        tl_eval_df = in_situ_df.dropna(subset=tl_feature_cols + [TARGET]).copy()

        if tl_eval_df.empty:
            continue

        X_tl = tl_eval_df[tl_feature_cols]
        y_true_tl = tl_eval_df[[TARGET]].values

        scaler_x, scaler_y = tl_scalers[tl_key]

        if X_tl.shape[1] != tl_model.input_shape[-1]:
            raise ValueError(
                f"{eval_label}: TL model '{tl_key}' expects "
                f"{tl_model.input_shape[-1]} features, but got {X_tl.shape[1]} "
                f"from columns {tl_feature_cols}"
            )

        X_scaled = scaler_x.transform(X_tl)
        y_pred_scaled = tl_model.predict(X_scaled, verbose=0)
        y_pred_tl = scaler_y.inverse_transform(y_pred_scaled)

        mse_tl = np.mean((y_true_tl - y_pred_tl) ** 2)
        normalized_mse_tl = mse_tl / mean_runoff if mean_runoff != 0 else np.nan

        mar_eval_tl = mar_df.loc[mar_df["date"].isin(tl_eval_df["date"])].sort_values("date")
        y_mar_tl = mar_eval_tl[[TARGET]].values

        results_df.loc[len(results_df)] = {
            "Prediction Site": eval_label,
            "Model": f"{tl_key} TL Model",
            "Training Site": tl_key,
            "In-situ Cumulative Runoff": np.cumsum(y_true_tl)[-1],
            "MAR Cumulative Runoff": np.cumsum(y_mar_tl)[-1],
            "Model Predicted Cumulative Runoff": np.cumsum(y_pred_tl)[-1],
            "MSE": mse_tl,
            "normalized MSE": normalized_mse_tl,
            "R^2": r2_score(y_true_tl, y_pred_tl),
            "NSE": nse(y_true_tl, y_pred_tl),
            "Error Rate": abs(np.cumsum(y_true_tl)[-1] - np.cumsum(y_pred_tl)[-1]) / np.cumsum(y_true_tl)[-1]
        }

        if tl_key == tl_key_for_plot:
            tl_pred_plot = y_pred_tl.ravel()
            _, tl_low_plot, tl_high_plot = mc_dropout_predictions(
                tl_model, scaler_x, scaler_y, X_tl
            )
            tl_dates = tl_eval_df["date"]
            tl_y_true_plot = y_true_tl.ravel()

    dates = eval_df["date"]

    plt.figure(figsize=(10, 6))

    plt.plot(dates, np.cumsum(y_true.ravel()), "--", color="red", label="In-situ")
    plt.plot(dates, np.cumsum(y_pred_mar_emulator.ravel()), "-.", color="steelblue", label=f"{mar_emulator_key} MAR Emulator")
    plt.fill_between(dates, np.cumsum(mar_emulator_low), np.cumsum(mar_emulator_high), color="steelblue", alpha=0.25)

    plt.plot(tl_dates, np.cumsum(tl_pred_plot), "-", color="darkorange", label=f"{tl_key_for_plot} TL Model")
    plt.fill_between(tl_dates, np.cumsum(tl_low_plot), np.cumsum(tl_high_plot), color="darkorange", alpha=0.25)

    plt.xlabel("Date")
    plt.ylabel("Cumulative Runoff (mmWE)")
    plt.legend()
    plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Run evaluations
evaluate_catchment(rb_in_situ_2015, rb_2015_mar, "2015 Rio Behar")
evaluate_catchment(rb_in_situ_2016, rb_2016_mar, "2016 Rio Behar")

evaluate_catchment(ak4_in_situ_2008, ak4_2008_mar, "2008 AK4")
evaluate_catchment(ak4_in_situ_2009, ak4_2009_mar, "2009 AK4")
evaluate_catchment(ak4_in_situ_2010, ak4_2010_mar, "2010 AK4")
evaluate_catchment(ak4_in_situ_2011, ak4_2011_mar, "2011 AK4")
evaluate_catchment(ak4_in_situ_2012, ak4_2012_mar, "2012 AK4")
evaluate_catchment(ak4_in_situ_2013, ak4_2013_mar, "2013 AK4")
evaluate_catchment(ak4_in_situ_2014, ak4_2014_mar, "2014 AK4")
evaluate_catchment(ak4_in_situ_2015, ak4_2015_mar, "2015 AK4")
evaluate_catchment(ak4_in_situ_2016, ak4_2016_mar, "2016 AK4")

evaluate_catchment(minturn_in_situ_2019, minturn_2019_mar, "2019 Minturn")
evaluate_catchment(minturn_in_situ_2020, minturn_2020_mar, "2020 Minturn")
evaluate_catchment(minturn_in_situ_2021, minturn_2021_mar, "2021 Minturn")
evaluate_catchment(minturn_in_situ_2022, minturn_2022_mar, "2022 Minturn")

# Save cumulative evaluation results
#output_dir = '/Users/mlm211/Documents/DeepMelt/catchment-scale'
output_dir = '/Users/maya/Documents/Duke University/DeepMelt/catchment-scale'
results_file_name = os.path.join(output_dir, 'catchment_in-situ_cumulative_evaluation_results.csv')

if os.path.exists(results_file_name):
    os.remove(results_file_name)

results_df.to_csv(results_file_name, index=False)

# Calculate cumulative runoff bias

bias_results = []

for site in results_df["Prediction Site"].unique():

    site_df = results_df[
        results_df["Prediction Site"] == site
    ]

    obs = site_df["In-situ Cumulative Runoff"].iloc[0]

    # MAR emulator
    mar_emulator_row = site_df[
        site_df["Model"].str.contains("MAR Emulator", na=False)
    ].iloc[0]

    # Same-catchment TL model
    prediction_catchment = " ".join(site.split()[1:])

    tl_row = site_df[
        (site_df["Model"].str.contains("TL Model", na=False)) &
        (site_df["Training Site"].str.contains(prediction_catchment, na=False))
    ].iloc[0]

    mar_emulator_pred = mar_emulator_row["Model Predicted Cumulative Runoff"]
    tl_pred = tl_row["Model Predicted Cumulative Runoff"]

    mar_emulator_bias = 100 * (mar_emulator_pred - obs) / obs
    tl_bias = 100 * (tl_pred - obs) / obs

    bias_results.append({
        "Prediction Site": site,
        "Catchment": prediction_catchment,
        "MAR Bias (%)": mar_emulator_bias,
        "TL Bias (%)": tl_bias
    })

bias_df = pd.DataFrame(bias_results)

print(bias_df)

mean_mar_bias = bias_df["MAR Bias (%)"].mean()
mean_tl_bias = bias_df["TL Bias (%)"].mean()

print(f"\nMean MAR bias: {mean_mar_bias:.1f}%")
print(f"Mean TL bias: {mean_tl_bias:.1f}%")

# Load MAR emulators and TL model MSE for each catchment and year predicted
mar_emulator_tl_error_rate = pd.read_csv('./catchment_emulator_TL_error_rate.csv')

# Convert to long format
mar_emulator_tl_error_rate_long = mar_emulator_tl_error_rate.melt(
    id_vars=['catchment', 'year'],
    value_vars=['base_model_error_rate', 'TL_model_error_rate'],
    var_name='model',
    value_name='error rate'
)

# Clean model names
mar_emulator_tl_error_rate_long['model'] = mar_emulator_tl_error_rate_long['model'].replace({
    'base_model_error_rate': 'MAR emulator',
    'TL_model_error_rate': 'TL model'
})

# Plot box and whisker plot
plt.figure(figsize=(8, 6))
palette = {
    'MAR emulator': 'steelblue',
    'TL model': 'darkorange'}
ax = sns.boxplot(data=mar_emulator_tl_error_rate_long, x='catchment', y='error rate',
            hue='model', palette=palette, width=0.5, showfliers=False)
for patch in ax.patches:
    patch.set_alpha(0.85)
plt.xlabel('Catchment', fontsize=16)
plt.yscale('log')
plt.ylabel('Error Rate (log scale)', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(title='Model', fontsize=13, title_fontsize=14, loc='upper left')
plt.grid(True, which='major', axis='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)
plt.tight_layout()
plt.show()

# Error rate heatmap of generalization across catchments
tl_results = results_df[results_df["Model"].str.contains("TL Model", na=False)].copy()

tl_results["TL Model"] = tl_results["Model"].str.replace(" TL Model", "", regex=False)
tl_results["TL Model"] = tl_results["TL Model"].str.replace(r"^\d{4}-\d{4} ", "", regex=True)
tl_results["Catchment"] = tl_results["Prediction Site"].str.split().str[1:].str.join(" ")

error_rate_avg = tl_results.groupby(["TL Model", "Catchment"])["Error Rate"].mean().reset_index()

error_rate_matrix = error_rate_avg.pivot(index="TL Model", columns="Catchment", values="Error Rate")

order = ["Rio Behar", "AK4", "Minturn"]
error_rate_matrix = error_rate_matrix.reindex(index=order[::-1], columns=order)

plt.figure(figsize=(12, 8))

ax = sns.heatmap(
    error_rate_matrix,
    cmap="flare",
    vmin=0,
    vmax = error_rate_matrix.max().max(),
    linewidths=0.5,
    linecolor="white",
    annot=True,
    fmt=".1f",
    annot_kws={"size": 16},
    cbar_kws={"label": "Normalized MSE"},
    alpha=0.8
)

cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=16)
cbar.set_label("Error Rate", fontsize=16)

plt.xlabel("Prediction Catchment", fontsize=16)
plt.ylabel("Transfer Learning Model", fontsize=16)
plt.xticks(fontsize=16, rotation=45)
plt.yticks(fontsize=16, rotation=0)
plt.tight_layout()
plt.show()

# Create a random consecutive gap in June–August
def create_random_gap(df, gap_days=7):
    df = df.copy().sort_values("date").reset_index(drop=True)

    if len(df) < gap_days:
        raise ValueError(f"Dataset too small for a {gap_days}-day gap (n={len(df)})")

    # Restrict to June–August
    summer_mask = df["date"].dt.month.isin([6, 7, 8])
    summer_indices = np.where(summer_mask)[0]

    if len(summer_indices) < gap_days:
        raise ValueError("Not enough June–August data for requested gap length")

    # Find valid consecutive windows
    valid_starts = []
    for i in range(len(summer_indices) - gap_days + 1):
        window = summer_indices[i:i + gap_days]
        if np.all(np.diff(window) == 1):
            valid_starts.append(window[0])

    if not valid_starts:
        raise ValueError("No valid consecutive gap window found in June–August")

    # Random start
    start_idx = random.choice(valid_starts)
    gap_idx = np.arange(start_idx, start_idx + gap_days)

    # Store original + remove values
    df["runoff_original"] = df["runoff"].copy()
    df.loc[gap_idx, "runoff"] = np.nan

    return df, gap_idx


# Fill gaps using TL model
def fill_gaps_with_tl(df, mar_df, eval_label):
    tl_key = EVAL_MODEL_MAP[eval_label]["tl"]

    tl_model = models[tl_key]
    scaler_x, scaler_y = tl_scalers[tl_key]
    feature_cols = FEATURES_BY_TL_KEY[tl_key]

    df = df.copy()

    missing_mask = df["runoff"].isna()

    # only fill rows where all required predictors exist
    feature_mask = df[feature_cols].notna().all(axis=1)
    predict_mask = missing_mask & feature_mask

    X_missing = df.loc[predict_mask, feature_cols]

    if len(X_missing) == 0:
        return df

    if X_missing.shape[1] != tl_model.input_shape[-1]:
        raise ValueError(
            f"{eval_label}: TL model '{tl_key}' expects "
            f"{tl_model.input_shape[-1]} features, but got {X_missing.shape[1]} "
            f"from columns {feature_cols}"
        )

    X_scaled = scaler_x.transform(X_missing)
    y_pred_scaled = tl_model.predict(X_scaled, verbose=0)
    y_pred = scaler_y.inverse_transform(y_pred_scaled).ravel()

    df["runoff_filled"] = np.nan
    df.loc[predict_mask, "runoff_filled"] = y_pred

    return df

# Calculate normalized MSE for the TL-filled gap
def gap_normalized_mse(obs, pred):
    obs = np.asarray(obs).flatten()
    pred = np.asarray(pred).flatten()

    mask = ~np.isnan(obs) & ~np.isnan(pred)
    obs = obs[mask]
    pred = pred[mask]

    if len(obs) == 0:
        return np.nan

    mse = np.mean((obs - pred) ** 2)
    mean_obs = np.mean(obs)

    if mean_obs == 0:
        return np.nan

    return mse / mean_obs


# Plot results of gap filling 
def plot_gap_filling(df, gap_idx, eval_label, ax):
    df = df.sort_values("date").reset_index(drop=True).copy()

    # Create continuous series
    df["runoff_plot"] = df["runoff"].copy()
    df.loc[gap_idx, "runoff_plot"] = df.loc[gap_idx, "runoff_original"]

    # Plots
    ax.plot(df["date"], df["runoff_plot"], color="black", linewidth=2, label="Observed")

    true_gap = df.loc[gap_idx]
    ax.plot(true_gap["date"], true_gap["runoff_original"],
            color="red", linestyle="--", linewidth=2, label="Gap in Observed")
    
    nmse_value = None
    
    if "runoff_filled" in df.columns:
        pred_gap = df.loc[gap_idx]
        ax.plot(pred_gap["date"], pred_gap["runoff_filled"],
                color="blue", linewidth=2, label="TL Model")
        nmse_value = gap_normalized_mse(
            pred_gap["runoff_original"].values,
            pred_gap["runoff_filled"].values
        )

    ax.set_title(eval_label, fontsize=20)
    ax.set_xlabel("Date", fontsize=18)
    ax.set_ylabel("Meltwater Runoff (mmWE)", fontsize=18)
    if nmse_value is not None:
        if eval_label == "2008 AK4" or eval_label == "2019 Minturn" or eval_label == "2022 Minturn":
            ax.text(0.60, 0.95,
                    f"NMSE = {nmse_value:.2f}",
                    transform=ax.transAxes,
                    fontsize=24,
                    verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="white", edgecolor="grey", alpha=0.75))
        else:
            ax.text(0.03, 0.95,
                    f"NMSE = {nmse_value:.2f}",
                    transform=ax.transAxes,
                    fontsize=24,
                    verticalalignment="top",
                    bbox=dict(boxstyle="round", facecolor="white", edgecolor="grey", alpha=0.75))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=3, maxticks=5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.tick_params(axis="both", labelsize=16)
    ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)
    for label in ax.get_xticklabels():
        label.set_rotation(30)
        label.set_horizontalalignment('right')

# Run for all years
def run_gap_filling_all_years():

    # Define catchment data here
    catchment_data = {
        "Rio Behar": [
            ("2015 Rio Behar", rb_in_situ_2015, rb_2015_mar),
            ("2016 Rio Behar", rb_in_situ_2016, rb_2016_mar),
        ],
        "AK4": [
            ("2008 AK4", ak4_in_situ_2008, ak4_2008_mar),
            ("2009 AK4", ak4_in_situ_2009, ak4_2009_mar),
            ("2010 AK4", ak4_in_situ_2010, ak4_2010_mar),
            ("2011 AK4", ak4_in_situ_2011, ak4_2011_mar),
            ("2012 AK4", ak4_in_situ_2012, ak4_2012_mar),
            ("2013 AK4", ak4_in_situ_2013, ak4_2013_mar),
            ("2014 AK4", ak4_in_situ_2014, ak4_2014_mar),
            ("2015 AK4", ak4_in_situ_2015, ak4_2015_mar),
            ("2016 AK4", ak4_in_situ_2016, ak4_2016_mar),
        ],
        "Minturn": [
            ("2019 Minturn", minturn_in_situ_2019, minturn_2019_mar),
            ("2020 Minturn", minturn_in_situ_2020, minturn_2020_mar),
            ("2021 Minturn", minturn_in_situ_2021, minturn_2021_mar),
            ("2022 Minturn", minturn_in_situ_2022, minturn_2022_mar),
        ]
    }

    # Flatten list
    all_years = [
        (catchment, label, df, mar)
        for catchment, options in catchment_data.items()
        for (label, df, mar) in options
    ]

    n_panels = len(all_years)
    ncols = 4
    nrows = int(np.ceil(n_panels / ncols))

    fig, axes = plt.subplots(nrows, ncols, figsize=(28, 4 * nrows))
    axes = np.array(axes).flatten()

    for i, (catchment, label, insitu_df, mar_df) in enumerate(all_years):
        print(f"Running gap filling: {label}")

        gap_days = 2 if catchment == "Rio Behar" else 7

        gapped_df, gap_idx = create_random_gap(insitu_df, gap_days)
        filled_df = fill_gaps_with_tl(gapped_df, mar_df, label)

        plot_gap_filling(filled_df, gap_idx, label, axes[i])

    # Turn off unused axes
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    # Shared legend
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, fontsize=14)
    plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()


# Run
run_gap_filling_all_years()

# Run a single gap filling experiment (without plotting)
def run_single_gap_experiment(insitu_df, mar_df, label, gap_days):
    gapped_df, gap_idx = create_random_gap(insitu_df, gap_days)
    filled_df = fill_gaps_with_tl(gapped_df, mar_df, label)

    # Linear interpolation on the gapped runoff series
    filled_df["runoff_linear_interp"] = (
        filled_df["runoff"]
        .interpolate(method="linear", limit_direction="both")
    )

    pred_gap = filled_df.loc[gap_idx]

    tl_nmse = gap_normalized_mse(
        pred_gap["runoff_original"].values,
        pred_gap["runoff_filled"].values
    )

    linear_interp_nmse = gap_normalized_mse(
        pred_gap["runoff_original"].values,
        pred_gap["runoff_linear_interp"].values
    )

    return tl_nmse, linear_interp_nmse

# Create an ensemble of 1,000 gap filling experiments
def run_gap_ensemble(n_runs=1000):
    catchment_data = {
        "Rio Behar": [
            ("2015 Rio Behar", rb_in_situ_2015, rb_2015_mar),
            ("2016 Rio Behar", rb_in_situ_2016, rb_2016_mar),
        ],
        "AK4": [
            ("2008 AK4", ak4_in_situ_2008, ak4_2008_mar),
            ("2009 AK4", ak4_in_situ_2009, ak4_2009_mar),
            ("2010 AK4", ak4_in_situ_2010, ak4_2010_mar),
            ("2011 AK4", ak4_in_situ_2011, ak4_2011_mar),
            ("2012 AK4", ak4_in_situ_2012, ak4_2012_mar),
            ("2013 AK4", ak4_in_situ_2013, ak4_2013_mar),
            ("2014 AK4", ak4_in_situ_2014, ak4_2014_mar),
            ("2015 AK4", ak4_in_situ_2015, ak4_2015_mar),
            ("2016 AK4", ak4_in_situ_2016, ak4_2016_mar),
        ],
        "Minturn": [
            ("2019 Minturn", minturn_in_situ_2019, minturn_2019_mar),
            ("2020 Minturn", minturn_in_situ_2020, minturn_2020_mar),
            ("2021 Minturn", minturn_in_situ_2021, minturn_2021_mar),
            ("2022 Minturn", minturn_in_situ_2022, minturn_2022_mar),
        ]
    }

    results = []

    for catchment, options in catchment_data.items():
        for label, insitu_df, mar_df in options:
            print(f"Running gap filling ensemble for: {label}")

            gap_days = 2 if catchment == "Rio Behar" else 7

            for run in range(n_runs):
                tl_nmse, linear_interp_nmse = run_single_gap_experiment(
                    insitu_df, mar_df, label, gap_days
                    )

                results.append({
                    "catchment": catchment,
                    "label": label,
                    "run": run,
                    "TL normalized MSE": tl_nmse,
                    "Linear Interpolation normalized MSE": linear_interp_nmse
                    })

    return pd.DataFrame(results)

# Results of 1,000 gap filling experiments
nmse_ensemble_results = run_gap_ensemble(n_runs=1000)

# Find the best mean TL normalized MSE year for each catchment
best_nmse_by_catchment = (
    nmse_ensemble_results
    .groupby(["catchment", "label"])["TL normalized MSE"]
    .mean()
    .reset_index()
    .sort_values("TL normalized MSE", ascending=True)
    .groupby("catchment")
    .head(1)
)

print(best_nmse_by_catchment)

# Make a 4-panel figure with only the best NMSE year per catchment
def plot_best_gap_filling_per_catchment(best_nmse_by_catchment):
    catchment_data = {
        "Rio Behar": [
            ("2015 Rio Behar", rb_in_situ_2015, rb_2015_mar),
            ("2016 Rio Behar", rb_in_situ_2016, rb_2016_mar),
        ],
        "AK4": [
            ("2008 AK4", ak4_in_situ_2008, ak4_2008_mar),
            ("2009 AK4", ak4_in_situ_2009, ak4_2009_mar),
            ("2010 AK4", ak4_in_situ_2010, ak4_2010_mar),
            ("2011 AK4", ak4_in_situ_2011, ak4_2011_mar),
            ("2012 AK4", ak4_in_situ_2012, ak4_2012_mar),
            ("2013 AK4", ak4_in_situ_2013, ak4_2013_mar),
            ("2014 AK4", ak4_in_situ_2014, ak4_2014_mar),
            ("2015 AK4", ak4_in_situ_2015, ak4_2015_mar),
            ("2016 AK4", ak4_in_situ_2016, ak4_2016_mar),
        ],
        "Minturn": [
            ("2019 Minturn", minturn_in_situ_2019, minturn_2019_mar),
            ("2020 Minturn", minturn_in_situ_2020, minturn_2020_mar),
            ("2021 Minturn", minturn_in_situ_2021, minturn_2021_mar),
            ("2022 Minturn", minturn_in_situ_2022, minturn_2022_mar),
        ]
    }

    fig, axes = plt.subplots(2, 2, figsize=(26, 18))
    axes = axes.flatten()

    catchment_order = ["Rio Behar", "AK4", "Minturn"]

    for i, catchment in enumerate(catchment_order):
        best_label = best_nmse_by_catchment.loc[
            best_nmse_by_catchment["catchment"] == catchment,
            "label"
        ].iloc[0]

        label, insitu_df, mar_df = [
            item for item in catchment_data[catchment]
            if item[0] == best_label
        ][0]

        print(f"Plotting best gap filling case for {catchment}: {label}")

        gap_days = 2 if catchment == "Rio Behar" else 7

        gapped_df, gap_idx = create_random_gap(insitu_df, gap_days)
        filled_df = fill_gaps_with_tl(gapped_df, mar_df, label)

        plot_gap_filling(filled_df, gap_idx, label, axes[i])

        axes[i].set_title(label, fontsize=28)
        axes[i].set_xlabel("Date", fontsize=24)
        axes[i].set_ylabel("Meltwater Runoff (mmWE)", fontsize=24)
        axes[i].tick_params(axis="both", labelsize=22)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="upper center",
        ncol=3,
        fontsize=28
        )

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


# Run best-case 4-panel gap filling plot
plot_best_gap_filling_per_catchment(best_nmse_by_catchment)

nmse_ensemble_summary = (
    nmse_ensemble_results
    .groupby("catchment")[["TL normalized MSE", "Linear Interpolation normalized MSE"]]
    .agg(["mean", "std"])
    .reset_index()
)

nmse_ensemble_summary_year = (
    nmse_ensemble_results
    .groupby("label")[["TL normalized MSE", "Linear Interpolation normalized MSE"]]
    .agg(["mean", "std"])
    .reset_index()
)

print(nmse_ensemble_summary)
print(nmse_ensemble_summary_year)
