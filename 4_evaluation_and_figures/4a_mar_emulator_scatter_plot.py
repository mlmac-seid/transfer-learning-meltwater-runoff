#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import tensorflow as tf
import joblib
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np


def regression_p_value(x, y):
    """
    Calculate an approximate two-sided p-value.
    """
    n = len(x)

    if n < 3:
        return np.nan

    r = np.corrcoef(x, y)[0, 1]

    # Handle a perfect correlation to avoid division by zero
    if np.isclose(np.abs(r), 1):
        return 0.0

    t_stat = r * np.sqrt((n - 2) / (1 - r**2))

    # Two-sided p-value using the normal-distribution approximation
    p_value = float(
        tf.math.erfc(np.abs(t_stat) / np.sqrt(2)).numpy()
    )

    return p_value


os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
# os.chdir('/Users/maya/Documents/Duke University/DeepMelt/catchment-scale')


# Load MAR data
rb_mar = pd.read_csv(
    './Rio_Behar_catchment_variables_2000_2021/rb_catchment_2000_2024_vars.csv'
)
ak4_mar = pd.read_csv(
    './AK4_catchment_variables_2008_2016/ak4_catchment_2000_2024_vars.csv'
)
minturn_mar = pd.read_csv(
    './Minturn_catchment_variables_2019_2020/minturn_catchment_2000_2024_vars.csv'
)

# Load trained MAR emulator models
rb_model = tf.keras.models.load_model(
    'trained_catchment_MLPs/rb_mar_mlp.keras'
)
ak4_model = tf.keras.models.load_model(
    'trained_catchment_MLPs/ak4_mar_mlp.keras'
)
minturn_model = tf.keras.models.load_model(
    'trained_catchment_MLPs/minturn_mar_mlp.keras'
)


# Catchment configuration
catchments = [
    (
        "Rio Behar",
        rb_mar,
        rb_model,
        "trained_catchment_MLPs/rb_mar_xscaler.pkl",
        "trained_catchment_MLPs/rb_mar_yscaler.pkl"
    ),
    (
        "AK4",
        ak4_mar,
        ak4_model,
        "trained_catchment_MLPs/ak4_mar_xscaler.pkl",
        "trained_catchment_MLPs/ak4_mar_yscaler.pkl"
    ),
    (
        "Minturn",
        minturn_mar,
        minturn_model,
        "trained_catchment_MLPs/minturn_mar_xscaler.pkl",
        "trained_catchment_MLPs/minturn_mar_yscaler.pkl"
    )
]

predictors = ['air_temp', 'ice_temp', 'albedo', 'shortwave_down']

# Scatterplots: MAR runoff versus emulator runoff
fig, axes = plt.subplots(1, 3, figsize=(20, 9))
axes = axes.flatten()

for i, (name, df, model, xscaler_path, yscaler_path) in enumerate(catchments):

    x_scaler = joblib.load(xscaler_path)
    y_scaler = joblib.load(yscaler_path)

    X = df[predictors]
    X_scaled = x_scaler.transform(X)

    y_true = df["meltwater_runoff"].values

    y_pred_scaled = model.predict(X_scaled, verbose=0)
    y_pred = y_scaler.inverse_transform(y_pred_scaled).flatten()

    # Performance metrics
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    p_value = regression_p_value(y_true, y_pred)

    ax = axes[i]

    ax.scatter(y_true, y_pred, color='steelblue', alpha=0.5)

    # Best-fit line
    m, b = np.polyfit(y_true, y_pred, 1)
    x_line = np.linspace(min(y_true), max(y_true), 100)
    y_line = m * x_line + b
    ax.plot(x_line, y_line, color='dimgrey', linewidth=2)

    # Format p-value for annotation
    if p_value < 0.001:
        p_text = "p < 0.001"
    else:
        p_text = f"p = {p_value:.3f}"

    # Prevent negative axes
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    # Performance annotation
    ax.text(
        0.05,
        0.95,
        f"R² = {r2:.2f}\nRMSE = {rmse:.2f} mmWE\n{p_text}",
        transform=ax.transAxes,
        fontsize=18,
        verticalalignment='top',
        bbox=dict(
            boxstyle='round',
            facecolor='white',
            edgecolor='grey',
            alpha=0.75
        )
    )

    ax.set_title(name, fontsize=22)
    ax.set_xlabel("Meltwater runoff from MAR (mmWE)", fontsize=20)

    if i == 0:
        ax.set_ylabel(
            "Meltwater runoff from MAR Emulator (mmWE)",
            fontsize=20
        )

    ax.tick_params(axis='both', labelsize=20)

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

# Daily MAR versus emulator runoff plots by year
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

    plot_df = plot_df.sort_values("datetime")
    plot_df["year"] = plot_df["datetime"].dt.year
    years = sorted(plot_df["year"].unique())

    fig, axes = plt.subplots(
        len(years),
        1,
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

# Cumulative melt-season runoff plots by year
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

    # Melt season: May through September
    plot_df["year"] = plot_df["datetime"].dt.year
    plot_df["month"] = plot_df["datetime"].dt.month
    melt_df = plot_df[plot_df["month"].between(5, 9)].copy()

    years = sorted(melt_df["year"].unique())

    fig, axes = plt.subplots(
        len(years),
        1,
        figsize=(14, 3.2 * len(years)),
        sharex=False
    )

    if len(years) == 1:
        axes = [axes]

    for ax, year in zip(axes, years):

        yearly = melt_df[melt_df["year"] == year].copy()

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
