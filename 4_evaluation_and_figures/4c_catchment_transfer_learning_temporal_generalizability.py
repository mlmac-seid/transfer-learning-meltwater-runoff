#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

# Catchment configuration
catchments = {
    "AK4": {
        "data": "/Users/maya/Documents/Duke University/DeepMelt/catchment-scale/catchment in-situ data/ak4_catchment_mar_tl.csv",
        "base_model": "./catchment_MAR_emulators/ak4_mar_mlp.keras"
    },
    "Rio Behar": {
        "data": "/Users/maya/Documents/Duke University/DeepMelt/catchment-scale/catchment in-situ data/rio_behar_catchment_mar_tl.csv",
        "base_model": "./catchment_MAR_emulators/rb_mar_mlp.keras"
    },
    "Minturn": {
        "data": "/Users/maya/Documents/Duke University/DeepMelt/catchment-scale/catchment in-situ data/minturn_catchment_mar_tl.csv",
        "base_model": "./catchment_MAR_emulators/minturn_mar_mlp.keras"
    }
}

# TL training datasets
tl_training_sets = {
    "AK4": pd.read_csv('catchment in-situ data/ak4_catchment_mar_tl.csv'),
    "Rio Behar": pd.read_csv('catchment in-situ data/rio_behar_catchment_mar_tl.csv'),
    "Minturn": pd.read_csv('catchment in-situ data/minturn_catchment_mar_tl.csv')
}

features = ['t2m', 'ts', 'al2', 'swd']
target = 'runoff'

# Train models with same scaler
trained_loyo_models = {}
trained_tl_models = {}
trained_mar_emulator_loyo_models = {}

for name, cfg in catchments.items():

    print(f"\n===== TRAINING: {name} =====")

    df = pd.read_csv(cfg["data"])
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year

    years = sorted(df['year'].unique())

    base_model = tf.keras.models.load_model(cfg["base_model"])

    trained_loyo_models[name] = {}
    trained_tl_models[name] = {}
    trained_mar_emulator_loyo_models[name] = {}

    tl_df = tl_training_sets[name]

    for test_year in years:

        print(f"Training year excluded: {test_year}")

        # Training data for withheld year
        train_df = df[df['year'] != test_year]
        X_train = train_df[features]
        y_train = train_df[target]

        # Shared scaler
        scaler_x = StandardScaler()
        scaler_y = StandardScaler()

        X_train_scaled = scaler_x.fit_transform(X_train)
        y_train_scaled = scaler_y.fit_transform(y_train.values.reshape(-1, 1))
        
        # MAR emulator with withheld year (copy architecture from MAR emulator)
        mar_emulator_loyo_model = tf.keras.models.clone_model(base_model)
        
        mar_emulator_loyo_model.compile(loss=MeanSquaredError(),
                                        optimizer=Adam(0.001))
        
        mar_emulator_loyo_model.fit(X_train_scaled, y_train_scaled, epochs=200,
                                    verbose=0)

        # TL model with withheld year
        loyo_model = tf.keras.models.clone_model(base_model)
        loyo_model.set_weights(base_model.get_weights())

        loyo_model.compile(loss=MeanSquaredError(), optimizer=Adam(0.001))

        loyo_model.fit(X_train_scaled, y_train_scaled, epochs=200, verbose=0)

        # TL model with full training set (retrained with same scaler)
        X_tl = tl_df[features]
        y_tl = tl_df[target]

        X_tl_scaled = scaler_x.transform(X_tl)
        y_tl_scaled = scaler_y.transform(y_tl.values.reshape(-1, 1))

        tl_model = tf.keras.models.clone_model(base_model)
        tl_model.set_weights(base_model.get_weights())

        tl_model.compile(loss=MeanSquaredError(), optimizer=Adam(0.001))

        tl_model.fit(X_tl_scaled, y_tl_scaled, epochs=200, verbose=0)

        # Store
        trained_loyo_models[name][test_year] = {
            "model": loyo_model,
            "scaler_x": scaler_x,
            "scaler_y": scaler_y
        }

        trained_tl_models[name][test_year] = {
            "model": tl_model,
            "scaler_x": scaler_x,
            "scaler_y": scaler_y
        }
        
        trained_mar_emulator_loyo_models[name][test_year] = {
            "model": mar_emulator_loyo_model,
            "scaler_x": scaler_x,
            "scaler_y": scaler_y
        }
        
def error_rate(obs, pred):
    obs_cumulative = np.sum(obs)
    pred_cumulative = np.sum(pred)

    if obs_cumulative == 0:
        return np.nan

    return abs(obs_cumulative - pred_cumulative) / obs_cumulative

def ensemble_error_rates(model, scaler_x, scaler_y, X, y_true, n_runs=100):
    X_scaled = scaler_x.transform(X)

    errors = []

    for _ in range(n_runs):
        y_pred_scaled = model(X_scaled, training=True)
        y_pred = scaler_y.inverse_transform(y_pred_scaled.numpy()).flatten()

        errors.append(error_rate(y_true, y_pred))

    return errors

# Evaluate ensembles and plot boxplots
ensemble_results = []

for name, cfg in catchments.items():

    print(f"\n===== EVALUATING: {name} =====")

    df = pd.read_csv(cfg["data"])
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year

    years = sorted(df["year"].unique())

    for test_year in years:

        print(f"Evaluating year: {test_year}")

        test_df = df[df["year"] == test_year].copy()

        X_test = test_df[features]
        y_test = test_df[target].values

        scaler_x = trained_loyo_models[name][test_year]["scaler_x"]
        scaler_y = trained_loyo_models[name][test_year]["scaler_y"]

        model_specs = [
            (
                "MAR emulator: withheld melt season",
                trained_mar_emulator_loyo_models[name][test_year]["model"]
            ),
            (
                "TL model: withheld melt season",
                trained_loyo_models[name][test_year]["model"]
            ),
            (
                "TL model: all melt seasons",
                trained_tl_models[name][test_year]["model"]
            )
        ]

        for model_label, model in model_specs:

            errors = ensemble_error_rates(
                model=model,
                scaler_x=scaler_x,
                scaler_y=scaler_y,
                X=X_test,
                y_true=y_test,
                n_runs=100
            )

            for run, err in enumerate(errors):
                ensemble_results.append({
                    "Catchment": name,
                    "Year": int(test_year),
                    "Model": model_label,
                    "Run": run,
                    "Error Rate": err
                })

ensemble_results_df = pd.DataFrame(ensemble_results)

fig, axes = plt.subplots(2, 2, figsize=(24, 16))
axes = axes.flatten()

model_order = [
    "MAR emulator: withheld melt season",
    "TL model: withheld melt season",
    "TL model: all melt seasons"
]

colors = {
    "MAR emulator: withheld melt season": "steelblue",
    "TL model: withheld melt season": "orchid",
    "TL model: all melt seasons": "darkorange"
}

years_order = {
    "Rio Behar": sorted(ensemble_results_df.loc[
        ensemble_results_df["Catchment"] == "Rio Behar", "Year"].unique()),
    "AK4": sorted(ensemble_results_df.loc[
        ensemble_results_df["Catchment"] == "AK4", "Year"].unique()),
    "Minturn": sorted(ensemble_results_df.loc[
        ensemble_results_df["Catchment"] == "Minturn", "Year"].unique())
}

# Common y-axis limits for all subplots
ymin = 0
ymax = ensemble_results_df["Error Rate"].max() * 1.05
yticks = np.linspace(ymin, ymax, 6)

for ax, catchment in zip(axes, catchments.keys()):

    plot_df = ensemble_results_df[
        ensemble_results_df["Catchment"] == catchment
    ]

    years = years_order[catchment]
    x = np.arange(len(years))

    width = 0.25
    offsets = [-width, 0, width]

    for offset, model in zip(offsets, model_order):
        data = []

        for yr in years:
            vals = plot_df[
                (plot_df["Year"] == yr) &
                (plot_df["Model"] == model)
            ]["Error Rate"].values

            data.append(vals)

        bp = ax.boxplot(
            data,
            positions=x + offset,
            widths=0.22,
            patch_artist=True,
            showfliers=False
        )

        for patch in bp["boxes"]:
            patch.set_facecolor(colors[model])
            patch.set_alpha(0.7)

        for median in bp["medians"]:
            median.set_color("black")

    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45)

    ax.set_title(catchment, fontsize=24)

    ax.grid(
        True,
        linestyle="--",
        linewidth=0.7,
        color="grey",
        alpha=0.6
    )

    ax.tick_params(axis="both", labelsize=20)

    # Same y-axis scale across all panels
    ax.set_ylim(ymin, ymax)
    ax.set_yticks(yticks)

# Axis labels
axes[0].set_ylabel("Error Rate", fontsize=20)
axes[2].set_ylabel("Error Rate", fontsize=20)

axes[2].set_xlabel("Melt Season Predicted", fontsize=20)
axes[3].set_xlabel("Melt Season Predicted", fontsize=20)

# Create legend manually
from matplotlib.patches import Patch

legend_handles = [
    Patch(facecolor=colors[m], edgecolor="black", alpha=0.7, label=m)
    for m in model_order
]

fig.legend(
    handles=legend_handles,
    loc="upper center",
    ncol=3,
    fontsize=20
)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()