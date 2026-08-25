#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:17:15 2026

@author: mlm211

Calculate ensemble mean MSE and uncertainties for catchment-scale training size and predictors experiments.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')
# Working directory on personal computer:
# os.chdir('/Users/maya/Documents/Duke University/DeepMelt/catchment-scale')

# Load in model run logs for catchment-scale training size experiments
rb_log = pd.read_csv(
    './catchment_training_size_experiment_logs/catchment_training_size_experiment_random_log_rio_behar.csv')
minturn_log = pd.read_csv(
    './catchment_training_size_experiment_logs/catchment_training_size_experiment_random_log_minturn.csv')
ak4_log = pd.read_csv(
    './catchment_training_size_experiment_logs/catchment_training_size_experiment_random_log_ak4.csv')


# Calculate ensemble mean MSE and the standard error of the mean MSE
def mean_sem(data):
    x = data.dropna().values
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    sem = std / np.sqrt(len(x))
    return mean, sem


# Ensemble mean MSE and uncertainty for each catchment
def mean_uncertainty(log_file):
    # Only select 21 years of training data
    random_21_years = log_file[log_file['training_size'] == 21]

    rows = []

    predictor_sets = [
        'x_t2m',
        'x_t2m_al2',
        'x_t2m_ts',
        'x_t2m_ts_al2',
        'x_t2m_swd',
        'x_t2m_ts_al2_swd'
    ]

    for predictor in predictor_sets:
        df = random_21_years[random_21_years['predictors'] == predictor]
        mean, sem = mean_sem(df['MSE'])

        rows.append({
            'predictors': predictor,
            'mean_MSE': mean,
            'SEM_MSE': sem
        })

    mse_uncertainty_df = pd.DataFrame(rows)

    # Ensemble statistics
    ensemble_stats = (
        random_21_years
        .groupby('predictors')['MSE']
        .agg(mean_MSE='mean', std_MSE='std')
        .reset_index()
    )

    # Remove SEB predictor set, if present
    ensemble_stats = ensemble_stats[
        ensemble_stats['predictors'] != 'x_seb'
    ]

    # Number of observations in test set
    n = 365

    # Number of parameters in each predictor set
    k_dict = {
        'x_t2m': 1,
        'x_t2m_ts': 2,
        'x_t2m_al2': 2,
        'x_t2m_ts_al2': 3,
        'x_t2m_swd': 2,
        'x_t2m_ts_al2_swd': 4
    }

    ensemble_stats['k'] = ensemble_stats['predictors'].map(k_dict)

    # Bayesian Information Criterion formula
    ensemble_stats['BIC'] = (
        n * np.log(ensemble_stats['mean_MSE']) +
        ensemble_stats['k'] * np.log(n)
    )

    # Sort predictors from highest BIC to lowest BIC
    ensemble_stats = ensemble_stats.sort_values(
        'BIC',
        ascending=False
    ).reset_index(drop=True)

    # Plot error-complexity curve in BIC-ranked order
    x = ensemble_stats['predictors']
    y = ensemble_stats['mean_MSE']
    yerr = ensemble_stats['std_MSE']

    plt.figure(figsize=(10, 5))
    plt.plot(
        range(len(x)),
        y,
        marker='o',
        linewidth=2,
        label='Ensemble Mean MSE',
        color='steelblue'
    )

    plt.fill_between(
        range(len(x)),
        y - yerr,
        y + yerr,
        color='steelblue',
        alpha=0.35,
        label='±1 Std Dev'
    )

    plt.xticks(range(len(x)), x, rotation=45)
    plt.xlabel('Predictor Set')
    plt.ylabel('MSE')
    plt.legend()
    plt.grid(
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

    return mse_uncertainty_df, ensemble_stats


# Run function for ensemble mean MSE and uncertainty for each catchment
rb_mse_uncertainty_df, rb_ensemble_stats = mean_uncertainty(rb_log)
minturn_mse_uncertainty_df, minturn_ensemble_stats = mean_uncertainty(minturn_log)
ak4_mse_uncertainty_df, ak4_ensemble_stats = mean_uncertainty(ak4_log)

# Add catchment name to each ensemble_stats dataframe
rb_ensemble_stats['catchment'] = 'Rio Behar'
minturn_ensemble_stats['catchment'] = 'Minturn'
ak4_ensemble_stats['catchment'] = 'AK4'

# Combine all catchments into one dataframe
all_bic = pd.concat([
    rb_ensemble_stats,
    minturn_ensemble_stats,
    ak4_ensemble_stats
], ignore_index=True)

# Calculate BIC relative to x_t2m within each catchment
baseline_bic = (
    all_bic[all_bic['predictors'] == 'x_t2m']
    .set_index('catchment')['BIC']
)

all_bic['BIC_relative'] = all_bic.apply(
    lambda row: row['BIC'] - baseline_bic.loc[row['catchment']],
    axis=1
)

# Desired predictor order from left to right
predictor_order = [
    'x_t2m',              # Predictor Set 1
    'x_t2m_ts',           # Predictor Set 2
    'x_t2m_swd',          # Predictor Set 3
    'x_t2m_ts_al2',       # Predictor Set 4
    'x_t2m_al2',          # Predictor Set 5
    'x_t2m_ts_al2_swd'    # Predictor Set 6
]

# Numeric labels for predictor sets on x-axis
# These labels intentionally appear out of numerical order
predictor_labels = ['1', '2', '3', '4', '5', '6']

# Custom colors for each catchment
catchment_colors = {
    'AK4': '#CC6677',       # salmon
    'Minturn': '#332288',   # purple
    'Rio Behar': '#88CCEE'  # light blue
}

# Horizontal offsets so overlapping points are visible
offsets = {
    'AK4': -0.18,
    'Minturn': -0.06,
    'Rio Behar': 0.18
}

# Create figure
plt.figure(figsize=(10, 6))

# Numeric x positions for predictor sets
x_positions = np.arange(len(predictor_order))

# Plot each catchment separately
catchments = ['AK4', 'Minturn', 'Rio Behar']

for catchment in catchments:
    subset = all_bic[all_bic['catchment'] == catchment]

    # Reorder predictors
    subset = subset.set_index('predictors').loc[predictor_order].reset_index()

    plt.scatter(
        x_positions + offsets[catchment],
        subset['BIC_relative'],
        s=90,
        color=catchment_colors[catchment],
        label=catchment
    )

# Add zero reference line for x_t2m baseline
plt.axhline(
    0,
    color='black',
    linestyle='--',
    linewidth=1
)

# Formatting
plt.xlabel('Predictor Set', fontsize=16)
plt.ylabel(r'$\Delta$BIC relative to Predictor Set 1', fontsize=16)

plt.xticks(
    x_positions,
    predictor_labels,
    fontsize=14
)

plt.yticks(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Catchment', fontsize=14, title_fontsize=14)

plt.tight_layout()
plt.show()
