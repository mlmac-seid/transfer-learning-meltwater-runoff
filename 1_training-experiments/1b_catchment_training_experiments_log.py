#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:12:43 2026

@author: mlm211

Create file that logs results of catchment-scale training experiments.
"""

import os
import csv

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale/catchment_training_experiment_logs')

# Create log file
catchment_training_log_rio_behar = 'catchment_training_experiment_log_rio_behar.csv'
catchment_training_log_minturn = 'catchment_training_experiment_log_minturn.csv'
catchment_training_log_ak4 = 'catchment_training_experiment_log_ak4.csv'
header1 = ['mlp_type',
           'predictors',
           'nodes',
           'activation',
           'dropout',
           'optimizer',
           'learning_rate',
           'epochs',
           'MSE',
           'R^2',
           'observed_total_runoff',
           'predicted_total_runoff',
           'proportion_runoff_predicted']
header2 = ['mlp_type',
           'training_size',
           'predictors',
           'nodes',
           'activation',
           'dropout',
           'optimizer',
           'learning_rate',
           'epochs',
           'MSE',
           'R^2',
           'observed_total_runoff',
           'predicted_total_runoff',
           'proportion_runoff_predicted']


def log_catchment_mlp_results(log_file, mlp_type, predictors, nodes, activation, dropout,
                              optimizer, learning_rate, epochs, mse_full, R_2,
                              obs_mru, pred_mru, prop_mru_modeled):

    # check the file exists
    file_exists = os.path.isfile(log_file)

    # write results to the file
    with open(log_file, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header1)
        writer.writerow([mlp_type, predictors, nodes, activation, dropout,
                         optimizer, learning_rate, epochs, mse_full, R_2,
                         obs_mru, pred_mru, prop_mru_modeled])


def log_catchment_training_experiment(log_file, mlp_type, training_size, predictors,
                                           nodes, activation, dropout, optimizer,
                                           learning_rate, epochs, mse_full, R_2, obs_mru,
                                           pred_mru, prop_mru_modeled):

    # check the file exists
    file_exists = os.path.isfile(log_file)

    # write results to the file
    with open(log_file, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header2)
        writer.writerow([mlp_type, training_size, predictors, nodes,
                         activation, dropout, optimizer, learning_rate, epochs,
                         mse_full, R_2, obs_mru, pred_mru, prop_mru_modeled])
