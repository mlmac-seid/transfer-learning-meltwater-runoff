#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import tensorflow as tf
import joblib
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
#os.chdir('/Users/maya/Documents/Duke University/DeepMelt/catchment-scale')

# Load MAR data
rb_mar = pd.read_csv('./Rio_Behar_catchment_variables/rb_catchment_2000_2024_vars.csv')
ak4_mar = pd.read_csv('./AK4_catchment_variables/ak4_catchment_2000_2024_vars.csv')
minturn_mar = pd.read_csv('./Minturn_catchment_variables/minturn_catchment_2000_2024_vars.csv')
north_mar = pd.read_csv('./North_catchment_variables/north_catchment_2000_2024_vars.csv')

# Load models
rb_model = tf.keras.models.load_model('catchment_MAR_emulators/rb_mar_mlp.keras')
ak4_model = tf.keras.models.load_model('catchment_MAR_emulators/ak4_mar_mlp.keras')
minturn_model = tf.keras.models.load_model('catchment_MAR_emulators/minturn_mar_mlp.keras')
north_model = tf.keras.models.load_model('catchment_MAR_emulators/north_mar_mlp.keras')


# Catchment configuration
catchments = [
    ("Rio Behar", rb_mar, rb_model,
     "catchment_MAR_emulators/rb_mar_xscaler.pkl",
     "catchment_MAR_emulators/rb_mar_yscaler.pkl"),

    ("AK4", ak4_mar, ak4_model,
     "catchment_MAR_emulators/ak4_mar_xscaler.pkl",
     "catchment_MAR_emulators/ak4_mar_yscaler.pkl"),

    ("Minturn", minturn_mar, minturn_model,
     "catchment_MAR_emulators/minturn_mar_xscaler.pkl",
     "catchment_MAR_emulators/minturn_mar_yscaler.pkl"),

    ("North", north_mar, north_model,
     "catchment_MAR_emulators/north_mar_xscaler.pkl",
     "catchment_MAR_emulators/north_mar_yscaler.pkl")
]

predictors = ['air_temp', 'ice_temp', 'albedo', 'shortwave_down']

fig, axes = plt.subplots(2, 2, figsize=(12,14))
axes = axes.flatten()

for i, (name, df, model, xscaler_path, yscaler_path) in enumerate(catchments):

    x_scaler = joblib.load(xscaler_path)
    y_scaler = joblib.load(yscaler_path)
    
    X = df[predictors]
        
    X_scaled = x_scaler.transform(X)

    y_true = df["meltwater_runoff"].values

    y_pred_scaled = model.predict(X_scaled, verbose=0)
    y_pred = y_scaler.inverse_transform(y_pred_scaled).flatten()

    r2 = r2_score(y_true, y_pred)

    ax = axes[i]

    ax.scatter(y_true, y_pred, color='steelblue', alpha=0.5)

    # Best-fit line
    m, b = np.polyfit(y_true, y_pred, 1)
    x_line = np.linspace(min(y_true), max(y_true), 100)
    y_line = m * x_line + b
    ax.plot(x_line, y_line, color='dimgrey', linewidth=2)

    # Prevent negative axes
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    ax.text(
        0.05, 0.95,
        f"R² = {r2:.2f}",
        transform=ax.transAxes,
        fontsize=16,
        verticalalignment='top',
        bbox=dict(
            boxstyle='round',
            facecolor='white',
            edgecolor='grey',
            alpha=0.75
        )
    )

    ax.set_title(name, fontsize=18)

    # Remove x-axis labels for panels a and b
    if i not in [0, 1]:
        ax.set_xlabel(
            "Meltwater runoff from MAR (mmWE)",
            fontsize=16
        )

    # Remove y-axis labels for panels b and d
    if i not in [1, 3]:
        ax.set_ylabel(
            "Meltwater runoff from MAR Emulator (mmWE)",
            fontsize=16
        )

    ax.tick_params(axis='both', labelsize=14)

    ax.grid(
        True,
        which='both',
        axis='both',
        linestyle='--',
        linewidth=0.7,
        color='grey',
        alpha=0.6
    )

plt.tight_layout()
plt.show()

for name, df, model, xscaler_path, yscaler_path in catchments:

    x_scaler = joblib.load(xscaler_path)
    y_scaler = joblib.load(yscaler_path)
    
    X = df[predictors]

    X_scaled = x_scaler.transform(X)

    y_true = df["meltwater_runoff"].values
    y_pred_scaled = model.predict(X_scaled, verbose=0)
    y_pred = y_scaler.inverse_transform(y_pred_scaled).flatten()

    plot_df = df.copy()
    plot_df["MAR"] = y_true
    plot_df["Emulator"] = y_pred

    # Use date/time column if present
    if "date" in plot_df.columns:
        plot_df["datetime"] = pd.to_datetime(plot_df["date"])
    elif "time" in plot_df.columns:
        plot_df["datetime"] = pd.to_datetime(plot_df["time"])
    else:
        raise ValueError(
            f"No date or time column found for {name}. "
            "Please add the correct datetime column name."
        )

    plot_df["year"] = plot_df["datetime"].dt.year
    years = sorted(plot_df["year"].unique())

    fig, axes = plt.subplots(
        len(years), 1,
        figsize=(14, 3.2 * len(years)),
        sharex=False
    )

    if len(years) == 1:
        axes = [axes]

    for ax, year in zip(axes, years):
        yearly = plot_df[plot_df["year"] == year]

        ax.plot(
            yearly["datetime"],
            yearly["MAR"],
            label="MAR",
            linewidth=1.5
        )

        ax.plot(
            yearly["datetime"],
            yearly["Emulator"],
            label="Emulator",
            linewidth=1.5,
            alpha=0.85
        )

        ax.set_title(f"{name} — {year}", fontsize=16)
        ax.set_ylabel("Runoff (mmWE)", fontsize=13)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)
        ax.tick_params(axis="both", labelsize=12)

    axes[-1].set_xlabel("Date", fontsize=14)
    axes[0].legend(fontsize=12)

    fig.suptitle(
        f"{name}: MAR vs Emulator Daily Meltwater Runoff",
        fontsize=18,
        y=1.002
    )

    plt.tight_layout()
    plt.show()
    
    


for name, df, model, xscaler_path, yscaler_path in catchments:

    x_scaler = joblib.load(xscaler_path)
    y_scaler = joblib.load(yscaler_path)
    
    X = df[predictors]

    X_scaled = x_scaler.transform(X)

    y_true = df["meltwater_runoff"].values
    y_pred_scaled = model.predict(X_scaled, verbose=0)
    y_pred = y_scaler.inverse_transform(y_pred_scaled).flatten()

    plot_df = df.copy()
    plot_df["MAR"] = y_true
    plot_df["Emulator"] = y_pred

    # Datetime handling
    if "date" in plot_df.columns:
        plot_df["datetime"] = pd.to_datetime(plot_df["date"])
    elif "time" in plot_df.columns:
        plot_df["datetime"] = pd.to_datetime(plot_df["time"])
    else:
        raise ValueError(f"No date/time column found for {name}")

    plot_df = plot_df.sort_values("datetime")

    # --- Define melt season ---
    # Example: melt season = year of summer (May–Sept)
    plot_df["year"] = plot_df["datetime"].dt.year
    plot_df["month"] = plot_df["datetime"].dt.month

    # Keep only melt season months (adjust if needed)
    melt_df = plot_df[plot_df["month"].between(5, 9)].copy()

    years = sorted(melt_df["year"].unique())

    fig, axes = plt.subplots(
        len(years), 1,
        figsize=(14, 3.2 * len(years)),
        sharex=False
    )

    if len(years) == 1:
        axes = [axes]

    for ax, year in zip(axes, years):
        yearly = melt_df[melt_df["year"] == year].copy()

        # --- CUMULATIVE SUM ---
        yearly["MAR_cum"] = np.cumsum(yearly["MAR"])
        yearly["Emulator_cum"] = np.cumsum(yearly["Emulator"])

        ax.plot(
            yearly["datetime"],
            yearly["MAR_cum"],
            label="MAR (cumulative)",
            linewidth=2
        )

        ax.plot(
            yearly["datetime"],
            yearly["Emulator_cum"],
            label="Emulator (cumulative)",
            linewidth=2,
            alpha=0.85
        )

        ax.set_title(f"{name} — {year} Melt Season", fontsize=16)
        ax.set_ylabel("Cumulative Runoff (mmWE)", fontsize=13)
        ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)
        ax.tick_params(axis="both", labelsize=12)

    axes[-1].set_xlabel("Date", fontsize=14)
    axes[0].legend(fontsize=12)

    fig.suptitle(
        f"{name}: Cumulative Melt Season Runoff (MAR vs Emulator)",
        fontsize=18,
        y=1.002
    )

    plt.tight_layout()
    plt.show()
