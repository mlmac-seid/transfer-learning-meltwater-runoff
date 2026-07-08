#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:57:34 2026

@author: mlm211
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import matplotlib.colors as mcolors

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/catchment-scale')

# Open 2000-2024 Rio Behar MAR data and add meltwater runoff column
rb_mar_2000 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2000.nc')
rb_mar_2000_df = rb_mar_2000.to_dataframe().reset_index()
rb_mar_2000_df['MRU'] = rb_mar_2000_df['RU'] - rb_mar_2000_df['RF']

rb_mar_2001 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2001.nc')
rb_mar_2001_df = rb_mar_2001.to_dataframe().reset_index()
rb_mar_2001_df['MRU'] = rb_mar_2001_df['RU'] - rb_mar_2001_df['RF']

rb_mar_2002 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2002.nc')
rb_mar_2002_df = rb_mar_2002.to_dataframe().reset_index()
rb_mar_2002_df['MRU'] = rb_mar_2002_df['RU'] - rb_mar_2002_df['RF']

rb_mar_2003 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2003.nc')
rb_mar_2003_df = rb_mar_2003.to_dataframe().reset_index()
rb_mar_2003_df['MRU'] = rb_mar_2003_df['RU'] - rb_mar_2003_df['RF']

rb_mar_2004 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2004.nc')
rb_mar_2004_df = rb_mar_2004.to_dataframe().reset_index()
rb_mar_2004_df['MRU'] = rb_mar_2004_df['RU'] - rb_mar_2004_df['RF']

rb_mar_2005 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2005.nc')
rb_mar_2005_df = rb_mar_2005.to_dataframe().reset_index()
rb_mar_2005_df['MRU'] = rb_mar_2005_df['RU'] - rb_mar_2005_df['RF']

rb_mar_2006 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2006.nc')
rb_mar_2006_df = rb_mar_2006.to_dataframe().reset_index()
rb_mar_2006_df['MRU'] = rb_mar_2006_df['RU'] - rb_mar_2006_df['RF']

rb_mar_2007 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2007.nc')
rb_mar_2007_df = rb_mar_2007.to_dataframe().reset_index()
rb_mar_2007_df['MRU'] = rb_mar_2007_df['RU'] - rb_mar_2007_df['RF']

rb_mar_2008 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2008.nc')
rb_mar_2008_df = rb_mar_2008.to_dataframe().reset_index()
rb_mar_2008_df['MRU'] = rb_mar_2008_df['RU'] - rb_mar_2008_df['RF']

rb_mar_2009 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2009.nc')
rb_mar_2009_df = rb_mar_2009.to_dataframe().reset_index()
rb_mar_2009_df['MRU'] = rb_mar_2009_df['RU'] - rb_mar_2009_df['RF']

rb_mar_2010 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2010.nc')
rb_mar_2010_df = rb_mar_2010.to_dataframe().reset_index()
rb_mar_2010_df['MRU'] = rb_mar_2010_df['RU'] - rb_mar_2010_df['RF']

rb_mar_2011 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2011.nc')
rb_mar_2011_df = rb_mar_2011.to_dataframe().reset_index()
rb_mar_2011_df['MRU'] = rb_mar_2011_df['RU'] - rb_mar_2011_df['RF']

rb_mar_2012 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2012.nc')
rb_mar_2012_df = rb_mar_2012.to_dataframe().reset_index()
rb_mar_2012_df['MRU'] = rb_mar_2012_df['RU'] - rb_mar_2012_df['RF']

rb_mar_2013 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2013.nc')
rb_mar_2013_df = rb_mar_2013.to_dataframe().reset_index()
rb_mar_2013_df['MRU'] = rb_mar_2013_df['RU'] - rb_mar_2013_df['RF']

rb_mar_2014 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2014.nc')
rb_mar_2014_df = rb_mar_2014.to_dataframe().reset_index()
rb_mar_2014_df['MRU'] = rb_mar_2014_df['RU'] - rb_mar_2014_df['RF']

rb_mar_2015 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2015.nc')
rb_mar_2015_df = rb_mar_2015.to_dataframe().reset_index()
rb_mar_2015_df['MRU'] = rb_mar_2015_df['RU'] - rb_mar_2015_df['RF']

rb_mar_2016 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2016.nc')
rb_mar_2016_df = rb_mar_2016.to_dataframe().reset_index()
rb_mar_2016_df['MRU'] = rb_mar_2016_df['RU'] - rb_mar_2016_df['RF']

rb_mar_2017 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2017.nc')
rb_mar_2017_df = rb_mar_2017.to_dataframe().reset_index()
rb_mar_2017_df['MRU'] = rb_mar_2017_df['RU'] - rb_mar_2017_df['RF']

rb_mar_2018 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2018.nc')
rb_mar_2018_df = rb_mar_2018.to_dataframe().reset_index()
rb_mar_2018_df['MRU'] = rb_mar_2018_df['RU'] - rb_mar_2018_df['RF']

rb_mar_2019 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2019.nc')
rb_mar_2019_df = rb_mar_2019.to_dataframe().reset_index()
rb_mar_2019_df['MRU'] = rb_mar_2019_df['RU'] - rb_mar_2019_df['RF']

rb_mar_2020 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2020.nc')
rb_mar_2020_df = rb_mar_2020.to_dataframe().reset_index()
rb_mar_2020_df['MRU'] = rb_mar_2020_df['RU'] - rb_mar_2020_df['RF']

rb_mar_2021 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2021.nc')
rb_mar_2021_df = rb_mar_2021.to_dataframe().reset_index()
rb_mar_2021_df['MRU'] = rb_mar_2021_df['RU'] - rb_mar_2021_df['RF']

rb_mar_2022 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2022.nc')
rb_mar_2022_df = rb_mar_2022.to_dataframe().reset_index()
rb_mar_2022_df['MRU'] = rb_mar_2022_df['RU'] - rb_mar_2022_df['RF']

rb_mar_2023 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2023.nc')
rb_mar_2023_df = rb_mar_2023.to_dataframe().reset_index()
rb_mar_2023_df['MRU'] = rb_mar_2023_df['RU'] - rb_mar_2023_df['RF']

rb_mar_2024 = xr.open_dataset('./MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2024.nc')
rb_mar_2024_df = rb_mar_2024.to_dataframe().reset_index()
rb_mar_2024_df['MRU'] = rb_mar_2024_df['RU'] - rb_mar_2024_df['RF']

# Combine into 2000-2024 dataframe
rb_mar_2000_2024_df = pd.concat([rb_mar_2000_df,
                                 rb_mar_2001_df,
                                 rb_mar_2002_df,
                                 rb_mar_2003_df,
                                 rb_mar_2004_df,
                                 rb_mar_2005_df,
                                 rb_mar_2006_df,
                                 rb_mar_2007_df,
                                 rb_mar_2008_df,
                                 rb_mar_2009_df,
                                 rb_mar_2010_df,
                                 rb_mar_2011_df,
                                 rb_mar_2012_df,
                                 rb_mar_2013_df,
                                 rb_mar_2014_df,
                                 rb_mar_2015_df,
                                 rb_mar_2016_df,
                                 rb_mar_2017_df,
                                 rb_mar_2018_df,
                                 rb_mar_2019_df,
                                 rb_mar_2020_df,
                                 rb_mar_2021_df,
                                 rb_mar_2022_df,
                                 rb_mar_2023_df,
                                 rb_mar_2024_df], ignore_index=True)

# Omit MAR variables that aren't pertinent atmospheric and climate variables
rb_mar_2000_2024_df = rb_mar_2000_2024_df.drop(columns=['AREA', 
                                                        'ATMLAY3_3', 
                                                        'crs', 
                                                        'DATE', 
                                                        'DD', 
                                                        'DX', 
                                                        'DY',
                                                        'LAT',
                                                        'LON',
                                                        'MM',
                                                        'MSK',
                                                        'OUTLAY',
                                                        'OUTLAY_bnds',
                                                        'SECTOR',
                                                        'SECTOR1_1',
                                                        'TIME',
                                                        'x',
                                                        'y',
                                                        'YYYY',
                                                        'ZTQLEV',
                                                        'ZTQLEV_bnds',
                                                        'ZUVLEV',
                                                        'ZUVLEV_bnds',
                                                        'spatial_ref',
                                                        'SOL',
                                                        'SRF',
                                                        'VEG',
                                                        'VV',
                                                        'VVZ',
                                                        'SH',
                                                        'UUZ',
                                                        'UU',
                                                        'FRV',
                                                        'QQZ',
                                                        'RU',
                                                        'ZN5',
                                                        'ZN6',
                                                        'SHSN2',
                                                        'ZN4',
                                                        'SHSN3',
                                                        'SU',
                                                        'SMB',
                                                        'WA1',
                                                        'CD',
                                                        'CM',
                                                        'CU',
                                                        'RH',
                                                        'RU2',
                                                        'QQ',
                                                        'RO1',
                                                        'SP',
                                                        'TI1',
                                                        'LWU',
                                                        'SWU',
                                                        'U2Z',
                                                        'V2Z',
                                                        'RHZ',
                                                        'RZ',
                                                        'UVZ',
                                                        'AL1',
                                                        'COD',
                                                        'ME'], errors='ignore')

# Rename MAR variable columns
rb_mar_2000_2024_df = rb_mar_2000_2024_df.rename(columns={
    'SMB': 'surface mass balance',
    'AL2': 'albedo',
    'SF': 'snowfall',
    'RF': 'rainfall',
    'WA1': 'liquid water content',
    'SHF': 'sensible heat flux',
    'LHF': 'latent heat flux',
    'LWD': 'long wave downward',
    'ST2': 'surface temperature',
    'SWD': 'short wave downward',
    'TTZ': '2m air temperature'})


# Pearson correlation between MAR variables and meltwater runoff
corr = rb_mar_2000_2024_df.corr(numeric_only=True)['MRU'].drop('MRU')

# Convert to R^2
r2 = corr**2

corr_df = r2.sort_values().reset_index()
corr_df.columns = ['variable', 'R2']

# Plot R^2
plt.figure(figsize=(8,6))
sns.barplot(data=corr_df, x='R2', y='variable', color='steelblue', alpha=0.75, edgecolor='black', linewidth=1.2)
plt.xlabel('Explained variance with meltwater runoff (R²)', fontsize=14)
plt.ylabel('MAR Output', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7, color='grey', alpha=0.6)
plt.tight_layout()
plt.show()
