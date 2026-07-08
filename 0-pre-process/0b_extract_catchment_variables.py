#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 13:05:25 2026

@author: mlm211

Extract pertinent variables from Rio Behar, AK4, Minturn, and North catchments 
from MAR version 3.14 to prepare for modeling.
"""


import os
import xarray as xr
import pandas as pd
import numpy as np

# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt')
# Working directory on personal computer:
# os.chdir('/Users/mayam/OneDrive/Documents/Duke University/DeepMelt')

# Load Rio Behar catchments
rb_catchment_2000 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2000.nc')
rb_catchment_2001 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2001.nc')
rb_catchment_2002 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2002.nc')
rb_catchment_2003 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2003.nc')
rb_catchment_2004 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2004.nc')
rb_catchment_2005 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2005.nc')
rb_catchment_2006 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2006.nc')
rb_catchment_2007 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2007.nc')
rb_catchment_2008 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2008.nc')
rb_catchment_2009 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2009.nc')
rb_catchment_2010 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2010.nc')
rb_catchment_2011 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2011.nc')
rb_catchment_2012 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2012.nc')
rb_catchment_2013 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2013.nc')
rb_catchment_2014 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2014.nc')
rb_catchment_2015 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2015.nc')
rb_catchment_2016 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2016.nc')
rb_catchment_2017 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2017.nc')
rb_catchment_2018 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2018.nc')
rb_catchment_2019 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2019.nc')
rb_catchment_2020 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2020.nc')
rb_catchment_2021 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2021.nc')
rb_catchment_2022 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2022.nc')
rb_catchment_2023 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2023.nc')
rb_catchment_2024 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rio_behar_catchment_2024.nc')

# Load AK4 catchments
ak4_catchment_2000 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2000.nc')
ak4_catchment_2001 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2001.nc')
ak4_catchment_2002 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2002.nc')
ak4_catchment_2003 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2003.nc')
ak4_catchment_2004 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2004.nc')
ak4_catchment_2005 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2005.nc')
ak4_catchment_2006 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2006.nc')
ak4_catchment_2007 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2007.nc')
ak4_catchment_2008 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2008.nc')
ak4_catchment_2009 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2009.nc')
ak4_catchment_2010 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2010.nc')
ak4_catchment_2011 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2011.nc')
ak4_catchment_2012 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2012.nc')
ak4_catchment_2013 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2013.nc')
ak4_catchment_2014 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2014.nc')
ak4_catchment_2015 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2015.nc')
ak4_catchment_2016 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2016.nc')
ak4_catchment_2017 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2017.nc')
ak4_catchment_2018 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2018.nc')
ak4_catchment_2019 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2019.nc')
ak4_catchment_2020 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2020.nc')
ak4_catchment_2021 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2021.nc')
ak4_catchment_2022 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2022.nc')
ak4_catchment_2023 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2023.nc')
ak4_catchment_2024 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_catchment_2024.nc')

# Load Minturn catchments
minturn_catchment_2000 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2000.nc')
minturn_catchment_2001 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2001.nc')
minturn_catchment_2002 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2002.nc')
minturn_catchment_2003 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2003.nc')
minturn_catchment_2004 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2004.nc')
minturn_catchment_2005 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2005.nc')
minturn_catchment_2006 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2006.nc')
minturn_catchment_2007 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2007.nc')
minturn_catchment_2008 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2008.nc')
minturn_catchment_2009 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2009.nc')
minturn_catchment_2010 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2010.nc')
minturn_catchment_2011 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2011.nc')
minturn_catchment_2012 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2012.nc')
minturn_catchment_2013 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2013.nc')
minturn_catchment_2014 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2014.nc')
minturn_catchment_2015 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2015.nc')
minturn_catchment_2016 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2016.nc')
minturn_catchment_2017 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2017.nc')
minturn_catchment_2018 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2018.nc')
minturn_catchment_2019 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2019.nc')
minturn_catchment_2020 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2020.nc')
minturn_catchment_2021 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2021.nc')
minturn_catchment_2022 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2022.nc')
minturn_catchment_2023 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2023.nc')
minturn_catchment_2024 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_catchment_2024.nc')

# Load North catchments
north_catchment_2000 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2000.nc')
north_catchment_2001 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2001.nc')
north_catchment_2002 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2002.nc')
north_catchment_2003 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2003.nc')
north_catchment_2004 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2004.nc')
north_catchment_2005 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2005.nc')
north_catchment_2006 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2006.nc')
north_catchment_2007 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2007.nc')
north_catchment_2008 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2008.nc')
north_catchment_2009 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2009.nc')
north_catchment_2010 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2010.nc')
north_catchment_2011 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2011.nc')
north_catchment_2012 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2012.nc')
north_catchment_2013 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2013.nc')
north_catchment_2014 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2014.nc')
north_catchment_2015 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2015.nc')
north_catchment_2016 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2016.nc')
north_catchment_2017 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2017.nc')
north_catchment_2018 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2018.nc')
north_catchment_2019 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2019.nc')
north_catchment_2020 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2020.nc')
north_catchment_2021 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2021.nc')
north_catchment_2022 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2022.nc')
north_catchment_2023 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2023.nc')
north_catchment_2024 = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_catchment_2024.nc')

# Load catchment fractions
rb_fraction = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment/rb_fraction.nc')
ak4_fraction = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment/ak4_fraction.nc')
minturn_fraction = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment/minturn_fraction.nc')
north_fraction = xr.open_dataset(
    '/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/north_catchment/north_fraction.nc')

# Rio Behar datetime array
rb_2000_time = rb_catchment_2000['TIME'].values
rb_2000_time = pd.to_datetime(rb_catchment_2000['TIME'].values).to_pydatetime()

rb_2001_time = rb_catchment_2001['TIME'].values
rb_2001_time = pd.to_datetime(rb_catchment_2001['TIME'].values).to_pydatetime()

rb_2002_time = rb_catchment_2002['TIME'].values
rb_2002_time = pd.to_datetime(rb_catchment_2002['TIME'].values).to_pydatetime()

rb_2003_time = rb_catchment_2003['TIME'].values
rb_2003_time = pd.to_datetime(rb_catchment_2003['TIME'].values).to_pydatetime()

rb_2004_time = rb_catchment_2004['TIME'].values
rb_2004_time = pd.to_datetime(rb_catchment_2004['TIME'].values).to_pydatetime()

rb_2005_time = rb_catchment_2005['TIME'].values
rb_2005_time = pd.to_datetime(rb_catchment_2005['TIME'].values).to_pydatetime()

rb_2006_time = rb_catchment_2006['TIME'].values
rb_2006_time = pd.to_datetime(rb_catchment_2006['TIME'].values).to_pydatetime()

rb_2007_time = rb_catchment_2007['TIME'].values
rb_2007_time = pd.to_datetime(rb_catchment_2007['TIME'].values).to_pydatetime()

rb_2008_time = rb_catchment_2008['TIME'].values
rb_2008_time = pd.to_datetime(rb_catchment_2008['TIME'].values).to_pydatetime()

rb_2009_time = rb_catchment_2009['TIME'].values
rb_2009_time = pd.to_datetime(rb_catchment_2009['TIME'].values).to_pydatetime()

rb_2010_time = rb_catchment_2010['TIME'].values
rb_2010_time = pd.to_datetime(rb_catchment_2010['TIME'].values).to_pydatetime()

rb_2011_time = rb_catchment_2011['TIME'].values
rb_2011_time = pd.to_datetime(rb_catchment_2011['TIME'].values).to_pydatetime()

rb_2012_time = rb_catchment_2012['TIME'].values
rb_2012_time = pd.to_datetime(rb_catchment_2012['TIME'].values).to_pydatetime()

rb_2013_time = rb_catchment_2013['TIME'].values
rb_2013_time = pd.to_datetime(rb_catchment_2013['TIME'].values).to_pydatetime()

rb_2014_time = rb_catchment_2014['TIME'].values
rb_2014_time = pd.to_datetime(rb_catchment_2014['TIME'].values).to_pydatetime()

rb_2015_time = rb_catchment_2015['TIME'].values
rb_2015_time = pd.to_datetime(rb_catchment_2015['TIME'].values).to_pydatetime()

rb_2016_time = rb_catchment_2016['TIME'].values
rb_2016_time = pd.to_datetime(rb_catchment_2016['TIME'].values).to_pydatetime()

rb_2017_time = rb_catchment_2017['TIME'].values
rb_2017_time = pd.to_datetime(rb_catchment_2017['TIME'].values).to_pydatetime()

rb_2018_time = rb_catchment_2018['TIME'].values
rb_2018_time = pd.to_datetime(rb_catchment_2018['TIME'].values).to_pydatetime()

rb_2019_time = rb_catchment_2019['TIME'].values
rb_2019_time = pd.to_datetime(rb_catchment_2019['TIME'].values).to_pydatetime()

rb_2020_time = rb_catchment_2020['TIME'].values
rb_2020_time = pd.to_datetime(rb_catchment_2020['TIME'].values).to_pydatetime()

rb_2021_time = rb_catchment_2021['TIME'].values
rb_2021_time = pd.to_datetime(rb_catchment_2021['TIME'].values).to_pydatetime()

rb_2022_time = rb_catchment_2022['TIME'].values
rb_2022_time = pd.to_datetime(rb_catchment_2022['TIME'].values).to_pydatetime()

rb_2023_time = rb_catchment_2023['TIME'].values
rb_2023_time = pd.to_datetime(rb_catchment_2023['TIME'].values).to_pydatetime()

rb_2024_time = rb_catchment_2024['TIME'].values
rb_2024_time = pd.to_datetime(rb_catchment_2024['TIME'].values).to_pydatetime()

# AK4 datetime array
ak4_2000_time = ak4_catchment_2000['TIME'].values
ak4_2000_time = pd.to_datetime(
    ak4_catchment_2000['TIME'].values).to_pydatetime()

ak4_2001_time = ak4_catchment_2001['TIME'].values
ak4_2001_time = pd.to_datetime(
    ak4_catchment_2001['TIME'].values).to_pydatetime()

ak4_2002_time = ak4_catchment_2002['TIME'].values
ak4_2002_time = pd.to_datetime(
    ak4_catchment_2002['TIME'].values).to_pydatetime()

ak4_2003_time = ak4_catchment_2003['TIME'].values
ak4_2003_time = pd.to_datetime(
    ak4_catchment_2003['TIME'].values).to_pydatetime()

ak4_2004_time = ak4_catchment_2004['TIME'].values
ak4_2004_time = pd.to_datetime(
    ak4_catchment_2004['TIME'].values).to_pydatetime()

ak4_2005_time = ak4_catchment_2005['TIME'].values
ak4_2005_time = pd.to_datetime(
    ak4_catchment_2005['TIME'].values).to_pydatetime()

ak4_2006_time = ak4_catchment_2006['TIME'].values
ak4_2006_time = pd.to_datetime(
    ak4_catchment_2006['TIME'].values).to_pydatetime()

ak4_2007_time = ak4_catchment_2007['TIME'].values
ak4_2007_time = pd.to_datetime(
    ak4_catchment_2007['TIME'].values).to_pydatetime()

ak4_2008_time = ak4_catchment_2008['TIME'].values
ak4_2008_time = pd.to_datetime(
    ak4_catchment_2008['TIME'].values).to_pydatetime()

ak4_2009_time = ak4_catchment_2009['TIME'].values
ak4_2009_time = pd.to_datetime(
    ak4_catchment_2009['TIME'].values).to_pydatetime()

ak4_2010_time = ak4_catchment_2010['TIME'].values
ak4_2010_time = pd.to_datetime(
    ak4_catchment_2010['TIME'].values).to_pydatetime()

ak4_2011_time = ak4_catchment_2011['TIME'].values
ak4_2011_time = pd.to_datetime(
    ak4_catchment_2011['TIME'].values).to_pydatetime()

ak4_2012_time = ak4_catchment_2012['TIME'].values
ak4_2012_time = pd.to_datetime(
    ak4_catchment_2012['TIME'].values).to_pydatetime()

ak4_2013_time = ak4_catchment_2013['TIME'].values
ak4_2013_time = pd.to_datetime(
    ak4_catchment_2013['TIME'].values).to_pydatetime()

ak4_2014_time = ak4_catchment_2014['TIME'].values
ak4_2014_time = pd.to_datetime(
    ak4_catchment_2014['TIME'].values).to_pydatetime()

ak4_2015_time = ak4_catchment_2015['TIME'].values
ak4_2015_time = pd.to_datetime(
    ak4_catchment_2015['TIME'].values).to_pydatetime()

ak4_2016_time = ak4_catchment_2016['TIME'].values
ak4_2016_time = pd.to_datetime(
    ak4_catchment_2016['TIME'].values).to_pydatetime()

ak4_2017_time = ak4_catchment_2017['TIME'].values
ak4_2017_time = pd.to_datetime(
    ak4_catchment_2017['TIME'].values).to_pydatetime()

ak4_2018_time = ak4_catchment_2018['TIME'].values
ak4_2018_time = pd.to_datetime(
    ak4_catchment_2018['TIME'].values).to_pydatetime()

ak4_2019_time = ak4_catchment_2019['TIME'].values
ak4_2019_time = pd.to_datetime(
    ak4_catchment_2019['TIME'].values).to_pydatetime()

ak4_2020_time = ak4_catchment_2020['TIME'].values
ak4_2020_time = pd.to_datetime(
    ak4_catchment_2020['TIME'].values).to_pydatetime()

ak4_2021_time = ak4_catchment_2021['TIME'].values
ak4_2021_time = pd.to_datetime(
    ak4_catchment_2021['TIME'].values).to_pydatetime()

ak4_2022_time = ak4_catchment_2022['TIME'].values
ak4_2022_time = pd.to_datetime(
    ak4_catchment_2022['TIME'].values).to_pydatetime()

ak4_2023_time = ak4_catchment_2023['TIME'].values
ak4_2023_time = pd.to_datetime(
    ak4_catchment_2023['TIME'].values).to_pydatetime()

ak4_2024_time = ak4_catchment_2024['TIME'].values
ak4_2024_time = pd.to_datetime(
    ak4_catchment_2024['TIME'].values).to_pydatetime()

# Minturn datetime array
minturn_2000_time = minturn_catchment_2000['TIME'].values
minturn_2000_time = pd.to_datetime(
    minturn_catchment_2000['TIME'].values).to_pydatetime()

minturn_2001_time = minturn_catchment_2001['TIME'].values
minturn_2001_time = pd.to_datetime(
    minturn_catchment_2001['TIME'].values).to_pydatetime()

minturn_2002_time = minturn_catchment_2002['TIME'].values
minturn_2002_time = pd.to_datetime(
    minturn_catchment_2002['TIME'].values).to_pydatetime()

minturn_2003_time = minturn_catchment_2003['TIME'].values
minturn_2003_time = pd.to_datetime(
    minturn_catchment_2003['TIME'].values).to_pydatetime()

minturn_2004_time = minturn_catchment_2004['TIME'].values
minturn_2004_time = pd.to_datetime(
    minturn_catchment_2004['TIME'].values).to_pydatetime()

minturn_2005_time = minturn_catchment_2005['TIME'].values
minturn_2005_time = pd.to_datetime(
    minturn_catchment_2005['TIME'].values).to_pydatetime()

minturn_2006_time = minturn_catchment_2006['TIME'].values
minturn_2006_time = pd.to_datetime(
    minturn_catchment_2006['TIME'].values).to_pydatetime()

minturn_2007_time = minturn_catchment_2007['TIME'].values
minturn_2007_time = pd.to_datetime(
    minturn_catchment_2007['TIME'].values).to_pydatetime()

minturn_2008_time = minturn_catchment_2008['TIME'].values
minturn_2008_time = pd.to_datetime(
    minturn_catchment_2008['TIME'].values).to_pydatetime()

minturn_2009_time = minturn_catchment_2009['TIME'].values
minturn_2009_time = pd.to_datetime(
    minturn_catchment_2009['TIME'].values).to_pydatetime()

minturn_2010_time = minturn_catchment_2010['TIME'].values
minturn_2010_time = pd.to_datetime(
    minturn_catchment_2010['TIME'].values).to_pydatetime()

minturn_2011_time = minturn_catchment_2011['TIME'].values
minturn_2011_time = pd.to_datetime(
    minturn_catchment_2011['TIME'].values).to_pydatetime()

minturn_2012_time = minturn_catchment_2012['TIME'].values
minturn_2012_time = pd.to_datetime(
    minturn_catchment_2012['TIME'].values).to_pydatetime()

minturn_2013_time = minturn_catchment_2013['TIME'].values
minturn_2013_time = pd.to_datetime(
    minturn_catchment_2013['TIME'].values).to_pydatetime()

minturn_2014_time = minturn_catchment_2014['TIME'].values
minturn_2014_time = pd.to_datetime(
    minturn_catchment_2014['TIME'].values).to_pydatetime()

minturn_2015_time = minturn_catchment_2015['TIME'].values
minturn_2015_time = pd.to_datetime(
    minturn_catchment_2015['TIME'].values).to_pydatetime()

minturn_2016_time = minturn_catchment_2016['TIME'].values
minturn_2016_time = pd.to_datetime(
    minturn_catchment_2016['TIME'].values).to_pydatetime()

minturn_2017_time = minturn_catchment_2017['TIME'].values
minturn_2017_time = pd.to_datetime(
    minturn_catchment_2017['TIME'].values).to_pydatetime()

minturn_2018_time = minturn_catchment_2018['TIME'].values
minturn_2018_time = pd.to_datetime(
    minturn_catchment_2018['TIME'].values).to_pydatetime()

minturn_2019_time = minturn_catchment_2019['TIME'].values
minturn_2019_time = pd.to_datetime(
    minturn_catchment_2019['TIME'].values).to_pydatetime()

minturn_2020_time = minturn_catchment_2020['TIME'].values
minturn_2020_time = pd.to_datetime(
    minturn_catchment_2020['TIME'].values).to_pydatetime()

minturn_2021_time = minturn_catchment_2021['TIME'].values
minturn_2021_time = pd.to_datetime(
    minturn_catchment_2021['TIME'].values).to_pydatetime()

minturn_2022_time = minturn_catchment_2022['TIME'].values
minturn_2022_time = pd.to_datetime(
    minturn_catchment_2022['TIME'].values).to_pydatetime()

minturn_2023_time = minturn_catchment_2023['TIME'].values
minturn_2023_time = pd.to_datetime(
    minturn_catchment_2023['TIME'].values).to_pydatetime()

minturn_2024_time = minturn_catchment_2024['TIME'].values
minturn_2024_time = pd.to_datetime(
    minturn_catchment_2024['TIME'].values).to_pydatetime()

# North datetime array
north_2000_time = north_catchment_2000['TIME'].values
north_2000_time = pd.to_datetime(
    north_catchment_2000['TIME'].values).to_pydatetime()

north_2001_time = north_catchment_2001['TIME'].values
north_2001_time = pd.to_datetime(
    north_catchment_2001['TIME'].values).to_pydatetime()

north_2002_time = north_catchment_2002['TIME'].values
north_2002_time = pd.to_datetime(
    north_catchment_2002['TIME'].values).to_pydatetime()

north_2003_time = north_catchment_2003['TIME'].values
north_2003_time = pd.to_datetime(
    north_catchment_2003['TIME'].values).to_pydatetime()

north_2004_time = north_catchment_2004['TIME'].values
north_2004_time = pd.to_datetime(
    north_catchment_2004['TIME'].values).to_pydatetime()

north_2005_time = north_catchment_2005['TIME'].values
north_2005_time = pd.to_datetime(
    north_catchment_2005['TIME'].values).to_pydatetime()

north_2006_time = north_catchment_2006['TIME'].values
north_2006_time = pd.to_datetime(
    north_catchment_2006['TIME'].values).to_pydatetime()

north_2007_time = north_catchment_2007['TIME'].values
north_2007_time = pd.to_datetime(
    north_catchment_2007['TIME'].values).to_pydatetime()

north_2008_time = north_catchment_2008['TIME'].values
north_2008_time = pd.to_datetime(
    north_catchment_2008['TIME'].values).to_pydatetime()

north_2009_time = north_catchment_2009['TIME'].values
north_2009_time = pd.to_datetime(
    north_catchment_2009['TIME'].values).to_pydatetime()

north_2010_time = north_catchment_2010['TIME'].values
north_2010_time = pd.to_datetime(
    north_catchment_2010['TIME'].values).to_pydatetime()

north_2011_time = north_catchment_2011['TIME'].values
north_2011_time = pd.to_datetime(
    north_catchment_2011['TIME'].values).to_pydatetime()

north_2012_time = north_catchment_2012['TIME'].values
north_2012_time = pd.to_datetime(
    north_catchment_2012['TIME'].values).to_pydatetime()

north_2013_time = north_catchment_2013['TIME'].values
north_2013_time = pd.to_datetime(
    north_catchment_2013['TIME'].values).to_pydatetime()

north_2014_time = north_catchment_2014['TIME'].values
north_2014_time = pd.to_datetime(
    north_catchment_2014['TIME'].values).to_pydatetime()

north_2015_time = north_catchment_2015['TIME'].values
north_2015_time = pd.to_datetime(
    north_catchment_2015['TIME'].values).to_pydatetime()

north_2016_time = north_catchment_2016['TIME'].values
north_2016_time = pd.to_datetime(
    north_catchment_2016['TIME'].values).to_pydatetime()

north_2017_time = north_catchment_2017['TIME'].values
north_2017_time = pd.to_datetime(
    north_catchment_2017['TIME'].values).to_pydatetime()

north_2018_time = north_catchment_2018['TIME'].values
north_2018_time = pd.to_datetime(
    north_catchment_2018['TIME'].values).to_pydatetime()

north_2019_time = north_catchment_2019['TIME'].values
north_2019_time = pd.to_datetime(
    north_catchment_2019['TIME'].values).to_pydatetime()

north_2020_time = north_catchment_2020['TIME'].values
north_2020_time = pd.to_datetime(
    north_catchment_2020['TIME'].values).to_pydatetime()

north_2021_time = north_catchment_2021['TIME'].values
north_2021_time = pd.to_datetime(
    north_catchment_2021['TIME'].values).to_pydatetime()

north_2022_time = north_catchment_2022['TIME'].values
north_2022_time = pd.to_datetime(
    north_catchment_2022['TIME'].values).to_pydatetime()

north_2023_time = north_catchment_2023['TIME'].values
north_2023_time = pd.to_datetime(
    north_catchment_2023['TIME'].values).to_pydatetime()

north_2024_time = north_catchment_2024['TIME'].values
north_2024_time = pd.to_datetime(
    north_catchment_2024['TIME'].values).to_pydatetime()

# Rio Behar catchment mean air temp
rb_2000_air_temp = rb_catchment_2000['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2001_air_temp = rb_catchment_2001['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2002_air_temp = rb_catchment_2002['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2003_air_temp = rb_catchment_2003['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2004_air_temp = rb_catchment_2004['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2005_air_temp = rb_catchment_2005['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2006_air_temp = rb_catchment_2006['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2007_air_temp = rb_catchment_2007['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2008_air_temp = rb_catchment_2008['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2009_air_temp = rb_catchment_2009['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2010_air_temp = rb_catchment_2010['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2011_air_temp = rb_catchment_2011['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2012_air_temp = rb_catchment_2012['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2013_air_temp = rb_catchment_2013['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2014_air_temp = rb_catchment_2014['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2015_air_temp = rb_catchment_2015['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2016_air_temp = rb_catchment_2016['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2017_air_temp = rb_catchment_2017['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2018_air_temp = rb_catchment_2018['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2019_air_temp = rb_catchment_2019['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2020_air_temp = rb_catchment_2020['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2021_air_temp = rb_catchment_2021['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2022_air_temp = rb_catchment_2022['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2023_air_temp = rb_catchment_2023['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
rb_2024_air_temp = rb_catchment_2024['TTZ'].mean(
    dim=("y", "x"), skipna=True).values

# AK4 catchment mean air temp
ak4_2000_air_temp = ak4_catchment_2000['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2001_air_temp = ak4_catchment_2001['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2002_air_temp = ak4_catchment_2002['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2003_air_temp = ak4_catchment_2003['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2004_air_temp = ak4_catchment_2004['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2005_air_temp = ak4_catchment_2005['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2006_air_temp = ak4_catchment_2006['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2007_air_temp = ak4_catchment_2007['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2008_air_temp = ak4_catchment_2008['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2009_air_temp = ak4_catchment_2009['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2010_air_temp = ak4_catchment_2010['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2011_air_temp = ak4_catchment_2011['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2012_air_temp = ak4_catchment_2012['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2013_air_temp = ak4_catchment_2013['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2014_air_temp = ak4_catchment_2014['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2015_air_temp = ak4_catchment_2015['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2016_air_temp = ak4_catchment_2016['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2017_air_temp = ak4_catchment_2017['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2018_air_temp = ak4_catchment_2018['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2019_air_temp = ak4_catchment_2019['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2020_air_temp = ak4_catchment_2020['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2021_air_temp = ak4_catchment_2021['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2022_air_temp = ak4_catchment_2022['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2023_air_temp = ak4_catchment_2023['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2024_air_temp = ak4_catchment_2024['TTZ'].mean(
    dim=("y", "x"), skipna=True).values

# Minturn catchment mean air temp
minturn_2000_air_temp = minturn_catchment_2000['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2001_air_temp = minturn_catchment_2001['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2002_air_temp = minturn_catchment_2002['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2003_air_temp = minturn_catchment_2003['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2004_air_temp = minturn_catchment_2004['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2005_air_temp = minturn_catchment_2005['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2006_air_temp = minturn_catchment_2006['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2007_air_temp = minturn_catchment_2007['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2008_air_temp = minturn_catchment_2008['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2009_air_temp = minturn_catchment_2009['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2010_air_temp = minturn_catchment_2010['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2011_air_temp = minturn_catchment_2011['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2012_air_temp = minturn_catchment_2012['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2013_air_temp = minturn_catchment_2013['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2014_air_temp = minturn_catchment_2014['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2015_air_temp = minturn_catchment_2015['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2016_air_temp = minturn_catchment_2016['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2017_air_temp = minturn_catchment_2017['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2018_air_temp = minturn_catchment_2018['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2019_air_temp = minturn_catchment_2019['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2020_air_temp = minturn_catchment_2020['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2021_air_temp = minturn_catchment_2021['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2022_air_temp = minturn_catchment_2022['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2023_air_temp = minturn_catchment_2023['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2024_air_temp = minturn_catchment_2024['TTZ'].mean(
    dim=("y", "x"), skipna=True).values

# North catchment mean air temp
north_2000_air_temp = north_catchment_2000['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2001_air_temp = north_catchment_2001['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2002_air_temp = north_catchment_2002['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2003_air_temp = north_catchment_2003['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2004_air_temp = north_catchment_2004['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2005_air_temp = north_catchment_2005['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2006_air_temp = north_catchment_2006['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2007_air_temp = north_catchment_2007['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2008_air_temp = north_catchment_2008['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2009_air_temp = north_catchment_2009['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2010_air_temp = north_catchment_2010['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2011_air_temp = north_catchment_2011['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2012_air_temp = north_catchment_2012['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2013_air_temp = north_catchment_2013['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2014_air_temp = north_catchment_2014['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2015_air_temp = north_catchment_2015['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2016_air_temp = north_catchment_2016['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2017_air_temp = north_catchment_2017['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2018_air_temp = north_catchment_2018['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2019_air_temp = north_catchment_2019['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2020_air_temp = north_catchment_2020['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2021_air_temp = north_catchment_2021['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2022_air_temp = north_catchment_2022['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2023_air_temp = north_catchment_2023['TTZ'].mean(
    dim=("y", "x"), skipna=True).values
north_2024_air_temp = north_catchment_2024['TTZ'].mean(
    dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean ice surface temp
rb_2000_ice_temp = rb_catchment_2000['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2001_ice_temp = rb_catchment_2001['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2002_ice_temp = rb_catchment_2002['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2003_ice_temp = rb_catchment_2003['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2004_ice_temp = rb_catchment_2004['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2005_ice_temp = rb_catchment_2005['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2006_ice_temp = rb_catchment_2006['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2007_ice_temp = rb_catchment_2007['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2008_ice_temp = rb_catchment_2008['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2009_ice_temp = rb_catchment_2009['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2010_ice_temp = rb_catchment_2010['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2011_ice_temp = rb_catchment_2011['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2012_ice_temp = rb_catchment_2012['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2013_ice_temp = rb_catchment_2013['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2014_ice_temp = rb_catchment_2014['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2015_ice_temp = rb_catchment_2015['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2016_ice_temp = rb_catchment_2016['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2017_ice_temp = rb_catchment_2017['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2018_ice_temp = rb_catchment_2018['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2019_ice_temp = rb_catchment_2019['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2020_ice_temp = rb_catchment_2020['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2021_ice_temp = rb_catchment_2021['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2022_ice_temp = rb_catchment_2022['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2023_ice_temp = rb_catchment_2023['ST2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2024_ice_temp = rb_catchment_2024['ST2'].mean(
    dim=("y", "x"), skipna=True).values

# AK4 catchment mean ice surface temp
ak4_2000_ice_temp = ak4_catchment_2000['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2001_ice_temp = ak4_catchment_2001['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2002_ice_temp = ak4_catchment_2002['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2003_ice_temp = ak4_catchment_2003['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2004_ice_temp = ak4_catchment_2004['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2005_ice_temp = ak4_catchment_2005['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2006_ice_temp = ak4_catchment_2006['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2007_ice_temp = ak4_catchment_2007['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2008_ice_temp = ak4_catchment_2008['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2009_ice_temp = ak4_catchment_2009['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2010_ice_temp = ak4_catchment_2010['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2011_ice_temp = ak4_catchment_2011['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2012_ice_temp = ak4_catchment_2012['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2013_ice_temp = ak4_catchment_2013['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2014_ice_temp = ak4_catchment_2014['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2015_ice_temp = ak4_catchment_2015['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2016_ice_temp = ak4_catchment_2016['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2017_ice_temp = ak4_catchment_2017['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2018_ice_temp = ak4_catchment_2018['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2019_ice_temp = ak4_catchment_2019['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2020_ice_temp = ak4_catchment_2020['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2021_ice_temp = ak4_catchment_2021['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2022_ice_temp = ak4_catchment_2022['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2023_ice_temp = ak4_catchment_2023['ST2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2024_ice_temp = ak4_catchment_2024['ST2'].mean(
    dim=("y", "x"), skipna=True).values

# Minturn catchment mean ice surface temp
minturn_2000_ice_temp = minturn_catchment_2000['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2001_ice_temp = minturn_catchment_2001['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2002_ice_temp = minturn_catchment_2002['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2003_ice_temp = minturn_catchment_2003['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2004_ice_temp = minturn_catchment_2004['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2005_ice_temp = minturn_catchment_2005['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2006_ice_temp = minturn_catchment_2006['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2007_ice_temp = minturn_catchment_2007['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2008_ice_temp = minturn_catchment_2008['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2009_ice_temp = minturn_catchment_2009['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2010_ice_temp = minturn_catchment_2010['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2011_ice_temp = minturn_catchment_2011['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2012_ice_temp = minturn_catchment_2012['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2013_ice_temp = minturn_catchment_2013['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2014_ice_temp = minturn_catchment_2014['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2015_ice_temp = minturn_catchment_2015['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2016_ice_temp = minturn_catchment_2016['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2017_ice_temp = minturn_catchment_2017['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2018_ice_temp = minturn_catchment_2018['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2019_ice_temp = minturn_catchment_2019['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2020_ice_temp = minturn_catchment_2020['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2021_ice_temp = minturn_catchment_2021['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2022_ice_temp = minturn_catchment_2022['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2023_ice_temp = minturn_catchment_2023['ST2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2024_ice_temp = minturn_catchment_2024['ST2'].mean(
    dim=("y", "x"), skipna=True).values

# North catchment mean ice surface temp
north_2000_ice_temp = north_catchment_2000['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2001_ice_temp = north_catchment_2001['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2002_ice_temp = north_catchment_2002['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2003_ice_temp = north_catchment_2003['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2004_ice_temp = north_catchment_2004['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2005_ice_temp = north_catchment_2005['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2006_ice_temp = north_catchment_2006['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2007_ice_temp = north_catchment_2007['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2008_ice_temp = north_catchment_2008['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2009_ice_temp = north_catchment_2009['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2010_ice_temp = north_catchment_2010['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2011_ice_temp = north_catchment_2011['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2012_ice_temp = north_catchment_2012['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2013_ice_temp = north_catchment_2013['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2014_ice_temp = north_catchment_2014['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2015_ice_temp = north_catchment_2015['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2016_ice_temp = north_catchment_2016['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2017_ice_temp = north_catchment_2017['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2018_ice_temp = north_catchment_2018['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2019_ice_temp = north_catchment_2019['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2020_ice_temp = north_catchment_2020['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2021_ice_temp = north_catchment_2021['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2022_ice_temp = north_catchment_2022['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2023_ice_temp = north_catchment_2023['ST2'].mean(
    dim=("y", "x"), skipna=True).values
north_2024_ice_temp = north_catchment_2024['ST2'].mean(
    dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean albedo
rb_2000_albedo = rb_catchment_2000['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2001_albedo = rb_catchment_2001['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2002_albedo = rb_catchment_2002['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2003_albedo = rb_catchment_2003['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2004_albedo = rb_catchment_2004['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2005_albedo = rb_catchment_2005['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2006_albedo = rb_catchment_2006['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2007_albedo = rb_catchment_2007['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2008_albedo = rb_catchment_2008['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2009_albedo = rb_catchment_2009['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2010_albedo = rb_catchment_2010['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2011_albedo = rb_catchment_2011['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2012_albedo = rb_catchment_2012['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2013_albedo = rb_catchment_2013['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2014_albedo = rb_catchment_2014['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2015_albedo = rb_catchment_2015['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2016_albedo = rb_catchment_2016['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2017_albedo = rb_catchment_2017['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2018_albedo = rb_catchment_2018['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2019_albedo = rb_catchment_2019['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2020_albedo = rb_catchment_2020['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2021_albedo = rb_catchment_2021['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2022_albedo = rb_catchment_2022['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2023_albedo = rb_catchment_2023['AL2'].mean(
    dim=("y", "x"), skipna=True).values
rb_2024_albedo = rb_catchment_2024['AL2'].mean(
    dim=("y", "x"), skipna=True).values

# AK4 catchment mean albedo
ak4_2000_albedo = ak4_catchment_2000['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2001_albedo = ak4_catchment_2001['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2002_albedo = ak4_catchment_2002['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2003_albedo = ak4_catchment_2003['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2004_albedo = ak4_catchment_2004['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2005_albedo = ak4_catchment_2005['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2006_albedo = ak4_catchment_2006['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2007_albedo = ak4_catchment_2007['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2008_albedo = ak4_catchment_2008['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2009_albedo = ak4_catchment_2009['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2010_albedo = ak4_catchment_2010['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2011_albedo = ak4_catchment_2011['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2012_albedo = ak4_catchment_2012['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2013_albedo = ak4_catchment_2013['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2014_albedo = ak4_catchment_2014['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2015_albedo = ak4_catchment_2015['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2016_albedo = ak4_catchment_2016['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2017_albedo = ak4_catchment_2017['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2018_albedo = ak4_catchment_2018['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2019_albedo = ak4_catchment_2019['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2020_albedo = ak4_catchment_2020['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2021_albedo = ak4_catchment_2021['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2022_albedo = ak4_catchment_2022['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2023_albedo = ak4_catchment_2023['AL2'].mean(
    dim=("y", "x"), skipna=True).values
ak4_2024_albedo = ak4_catchment_2024['AL2'].mean(
    dim=("y", "x"), skipna=True).values

# Minturn catchment mean albedo
minturn_2000_albedo = minturn_catchment_2000['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2001_albedo = minturn_catchment_2001['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2002_albedo = minturn_catchment_2002['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2003_albedo = minturn_catchment_2003['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2004_albedo = minturn_catchment_2004['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2005_albedo = minturn_catchment_2005['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2006_albedo = minturn_catchment_2006['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2007_albedo = minturn_catchment_2007['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2008_albedo = minturn_catchment_2008['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2009_albedo = minturn_catchment_2009['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2010_albedo = minturn_catchment_2010['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2011_albedo = minturn_catchment_2011['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2012_albedo = minturn_catchment_2012['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2013_albedo = minturn_catchment_2013['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2014_albedo = minturn_catchment_2014['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2015_albedo = minturn_catchment_2015['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2016_albedo = minturn_catchment_2016['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2017_albedo = minturn_catchment_2017['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2018_albedo = minturn_catchment_2018['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2019_albedo = minturn_catchment_2019['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2020_albedo = minturn_catchment_2020['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2021_albedo = minturn_catchment_2021['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2022_albedo = minturn_catchment_2022['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2023_albedo = minturn_catchment_2023['AL2'].mean(
    dim=("y", "x"), skipna=True).values
minturn_2024_albedo = minturn_catchment_2024['AL2'].mean(
    dim=("y", "x"), skipna=True).values

# North catchment mean albedo
north_2000_albedo = north_catchment_2000['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2001_albedo = north_catchment_2001['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2002_albedo = north_catchment_2002['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2003_albedo = north_catchment_2003['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2004_albedo = north_catchment_2004['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2005_albedo = north_catchment_2005['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2006_albedo = north_catchment_2006['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2007_albedo = north_catchment_2007['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2008_albedo = north_catchment_2008['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2009_albedo = north_catchment_2009['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2010_albedo = north_catchment_2010['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2011_albedo = north_catchment_2011['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2012_albedo = north_catchment_2012['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2013_albedo = north_catchment_2013['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2014_albedo = north_catchment_2014['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2015_albedo = north_catchment_2015['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2016_albedo = north_catchment_2016['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2017_albedo = north_catchment_2017['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2018_albedo = north_catchment_2018['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2019_albedo = north_catchment_2019['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2020_albedo = north_catchment_2020['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2021_albedo = north_catchment_2021['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2022_albedo = north_catchment_2022['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2023_albedo = north_catchment_2023['AL2'].mean(
    dim=("y", "x"), skipna=True).values
north_2024_albedo = north_catchment_2024['AL2'].mean(
    dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean shortwave downward
rb_2000_swd = rb_catchment_2000['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2001_swd = rb_catchment_2001['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2002_swd = rb_catchment_2002['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2003_swd = rb_catchment_2003['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2004_swd = rb_catchment_2004['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2005_swd = rb_catchment_2005['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2006_swd = rb_catchment_2006['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2007_swd = rb_catchment_2007['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2008_swd = rb_catchment_2008['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2009_swd = rb_catchment_2009['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2010_swd = rb_catchment_2010['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2011_swd = rb_catchment_2011['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2012_swd = rb_catchment_2012['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2013_swd = rb_catchment_2013['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2014_swd = rb_catchment_2014['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2015_swd = rb_catchment_2015['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2016_swd = rb_catchment_2016['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2017_swd = rb_catchment_2017['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2018_swd = rb_catchment_2018['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2019_swd = rb_catchment_2019['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2020_swd = rb_catchment_2020['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2021_swd = rb_catchment_2021['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2021_swd = rb_catchment_2021['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2022_swd = rb_catchment_2022['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2023_swd = rb_catchment_2023['SWD'].mean(dim=("y", "x"), skipna=True).values
rb_2024_swd = rb_catchment_2024['SWD'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean shortwave downward
ak4_2000_swd = ak4_catchment_2000['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_swd = ak4_catchment_2001['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_swd = ak4_catchment_2002['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_swd = ak4_catchment_2003['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_swd = ak4_catchment_2004['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_swd = ak4_catchment_2005['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_swd = ak4_catchment_2006['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_swd = ak4_catchment_2007['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_swd = ak4_catchment_2008['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_swd = ak4_catchment_2009['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_swd = ak4_catchment_2010['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_swd = ak4_catchment_2011['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_swd = ak4_catchment_2012['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_swd = ak4_catchment_2013['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_swd = ak4_catchment_2014['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_swd = ak4_catchment_2015['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_swd = ak4_catchment_2016['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_swd = ak4_catchment_2017['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_swd = ak4_catchment_2018['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_swd = ak4_catchment_2019['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_swd = ak4_catchment_2020['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_swd = ak4_catchment_2021['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_swd = ak4_catchment_2022['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_swd = ak4_catchment_2023['SWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_swd = ak4_catchment_2024['SWD'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean shortwave downward
minturn_2000_swd = minturn_catchment_2000['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_swd = minturn_catchment_2001['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_swd = minturn_catchment_2002['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_swd = minturn_catchment_2003['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_swd = minturn_catchment_2004['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_swd = minturn_catchment_2005['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_swd = minturn_catchment_2006['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_swd = minturn_catchment_2007['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_swd = minturn_catchment_2008['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_swd = minturn_catchment_2009['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_swd = minturn_catchment_2010['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_swd = minturn_catchment_2011['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_swd = minturn_catchment_2012['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_swd = minturn_catchment_2013['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_swd = minturn_catchment_2014['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_swd = minturn_catchment_2015['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_swd = minturn_catchment_2016['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_swd = minturn_catchment_2017['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_swd = minturn_catchment_2018['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_swd = minturn_catchment_2019['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_swd = minturn_catchment_2020['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_swd = minturn_catchment_2021['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_swd = minturn_catchment_2022['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_swd = minturn_catchment_2023['SWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_swd = minturn_catchment_2024['SWD'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean shortwave downward
north_2000_swd = north_catchment_2000['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2001_swd = north_catchment_2001['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2002_swd = north_catchment_2002['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2003_swd = north_catchment_2003['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2004_swd = north_catchment_2004['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2005_swd = north_catchment_2005['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2006_swd = north_catchment_2006['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2007_swd = north_catchment_2007['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2008_swd = north_catchment_2008['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2009_swd = north_catchment_2009['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2010_swd = north_catchment_2010['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2011_swd = north_catchment_2011['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2012_swd = north_catchment_2012['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2013_swd = north_catchment_2013['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2014_swd = north_catchment_2014['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2015_swd = north_catchment_2015['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2016_swd = north_catchment_2016['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2017_swd = north_catchment_2017['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2018_swd = north_catchment_2018['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2019_swd = north_catchment_2019['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2020_swd = north_catchment_2020['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2021_swd = north_catchment_2021['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2022_swd = north_catchment_2022['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2023_swd = north_catchment_2023['SWD'].mean(dim=("y", "x"), skipna=True).values
north_2024_swd = north_catchment_2024['SWD'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean shortwave upward
rb_2000_swu = rb_catchment_2000['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2001_swu = rb_catchment_2001['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2002_swu = rb_catchment_2002['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2003_swu = rb_catchment_2003['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2004_swu = rb_catchment_2004['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2005_swu = rb_catchment_2005['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2006_swu = rb_catchment_2006['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2007_swu = rb_catchment_2007['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2008_swu = rb_catchment_2008['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2009_swu = rb_catchment_2009['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2010_swu = rb_catchment_2010['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2011_swu = rb_catchment_2011['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2012_swu = rb_catchment_2012['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2013_swu = rb_catchment_2013['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2014_swu = rb_catchment_2014['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2015_swu = rb_catchment_2015['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2016_swu = rb_catchment_2016['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2017_swu = rb_catchment_2017['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2018_swu = rb_catchment_2018['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2019_swu = rb_catchment_2019['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2020_swu = rb_catchment_2020['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2021_swu = rb_catchment_2021['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2022_swu = rb_catchment_2022['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2023_swu = rb_catchment_2023['SWU'].mean(dim=("y", "x"), skipna=True).values
rb_2024_swu = rb_catchment_2024['SWU'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean shortwave upward
ak4_2000_swu = ak4_catchment_2000['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_swu = ak4_catchment_2001['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_swu = ak4_catchment_2002['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_swu = ak4_catchment_2003['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_swu = ak4_catchment_2004['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_swu = ak4_catchment_2005['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_swu = ak4_catchment_2006['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_swu = ak4_catchment_2007['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_swu = ak4_catchment_2008['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_swu = ak4_catchment_2009['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_swu = ak4_catchment_2010['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_swu = ak4_catchment_2011['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_swu = ak4_catchment_2012['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_swu = ak4_catchment_2013['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_swu = ak4_catchment_2014['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_swu = ak4_catchment_2015['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_swu = ak4_catchment_2016['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_swu = ak4_catchment_2017['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_swu = ak4_catchment_2018['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_swu = ak4_catchment_2019['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_swu = ak4_catchment_2020['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_swu = ak4_catchment_2021['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_swu = ak4_catchment_2022['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_swu = ak4_catchment_2023['SWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_swu = ak4_catchment_2024['SWU'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean shortwave upward
minturn_2000_swu = minturn_catchment_2000['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_swu = minturn_catchment_2001['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_swu = minturn_catchment_2002['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_swu = minturn_catchment_2003['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_swu = minturn_catchment_2004['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_swu = minturn_catchment_2005['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_swu = minturn_catchment_2006['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_swu = minturn_catchment_2007['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_swu = minturn_catchment_2008['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_swu = minturn_catchment_2009['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_swu = minturn_catchment_2010['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_swu = minturn_catchment_2011['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_swu = minturn_catchment_2012['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_swu = minturn_catchment_2013['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_swu = minturn_catchment_2014['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_swu = minturn_catchment_2015['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_swu = minturn_catchment_2016['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_swu = minturn_catchment_2017['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_swu = minturn_catchment_2018['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_swu = minturn_catchment_2019['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_swu = minturn_catchment_2020['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_swu = minturn_catchment_2021['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_swu = minturn_catchment_2022['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_swu = minturn_catchment_2023['SWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_swu = minturn_catchment_2024['SWU'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean shortwave upward
north_2000_swu = north_catchment_2000['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2001_swu = north_catchment_2001['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2002_swu = north_catchment_2002['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2003_swu = north_catchment_2003['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2004_swu = north_catchment_2004['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2005_swu = north_catchment_2005['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2006_swu = north_catchment_2006['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2007_swu = north_catchment_2007['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2008_swu = north_catchment_2008['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2009_swu = north_catchment_2009['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2010_swu = north_catchment_2010['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2011_swu = north_catchment_2011['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2012_swu = north_catchment_2012['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2013_swu = north_catchment_2013['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2014_swu = north_catchment_2014['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2015_swu = north_catchment_2015['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2016_swu = north_catchment_2016['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2017_swu = north_catchment_2017['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2018_swu = north_catchment_2018['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2019_swu = north_catchment_2019['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2020_swu = north_catchment_2020['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2021_swu = north_catchment_2021['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2022_swu = north_catchment_2022['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2023_swu = north_catchment_2023['SWU'].mean(dim=("y", "x"), skipna=True).values
north_2024_swu = north_catchment_2024['SWU'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean longwave downward
rb_2000_lwd = rb_catchment_2000['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2001_lwd = rb_catchment_2001['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2002_lwd = rb_catchment_2002['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2003_lwd = rb_catchment_2003['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2004_lwd = rb_catchment_2004['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2005_lwd = rb_catchment_2005['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2006_lwd = rb_catchment_2006['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2007_lwd = rb_catchment_2007['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2008_lwd = rb_catchment_2008['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2009_lwd = rb_catchment_2009['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2010_lwd = rb_catchment_2010['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2011_lwd = rb_catchment_2011['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2012_lwd = rb_catchment_2012['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2013_lwd = rb_catchment_2013['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2014_lwd = rb_catchment_2014['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2015_lwd = rb_catchment_2015['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2016_lwd = rb_catchment_2016['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2017_lwd = rb_catchment_2017['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2018_lwd = rb_catchment_2018['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2019_lwd = rb_catchment_2019['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2020_lwd = rb_catchment_2020['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2021_lwd = rb_catchment_2021['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2022_lwd = rb_catchment_2022['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2023_lwd = rb_catchment_2023['LWD'].mean(dim=("y", "x"), skipna=True).values
rb_2024_lwd = rb_catchment_2024['LWD'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean longwave downward
ak4_2000_lwd = ak4_catchment_2000['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_lwd = ak4_catchment_2001['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_lwd = ak4_catchment_2002['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_lwd = ak4_catchment_2003['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_lwd = ak4_catchment_2004['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_lwd = ak4_catchment_2005['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_lwd = ak4_catchment_2006['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_lwd = ak4_catchment_2007['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_lwd = ak4_catchment_2008['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_lwd = ak4_catchment_2009['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_lwd = ak4_catchment_2010['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_lwd = ak4_catchment_2011['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_lwd = ak4_catchment_2012['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_lwd = ak4_catchment_2013['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_lwd = ak4_catchment_2014['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_lwd = ak4_catchment_2015['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_lwd = ak4_catchment_2016['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_lwd = ak4_catchment_2017['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_lwd = ak4_catchment_2018['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_lwd = ak4_catchment_2019['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_lwd = ak4_catchment_2020['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_lwd = ak4_catchment_2021['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_lwd = ak4_catchment_2022['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_lwd = ak4_catchment_2023['LWD'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_lwd = ak4_catchment_2024['LWD'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean longwave downward
minturn_2000_lwd = minturn_catchment_2000['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_lwd = minturn_catchment_2001['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_lwd = minturn_catchment_2002['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_lwd = minturn_catchment_2003['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_lwd = minturn_catchment_2004['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_lwd = minturn_catchment_2005['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_lwd = minturn_catchment_2006['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_lwd = minturn_catchment_2007['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_lwd = minturn_catchment_2008['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_lwd = minturn_catchment_2009['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_lwd = minturn_catchment_2010['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_lwd = minturn_catchment_2011['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_lwd = minturn_catchment_2012['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_lwd = minturn_catchment_2013['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_lwd = minturn_catchment_2014['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_lwd = minturn_catchment_2015['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_lwd = minturn_catchment_2016['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_lwd = minturn_catchment_2017['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_lwd = minturn_catchment_2018['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_lwd = minturn_catchment_2019['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_lwd = minturn_catchment_2020['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_lwd = minturn_catchment_2021['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_lwd = minturn_catchment_2022['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_lwd = minturn_catchment_2023['LWD'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_lwd = minturn_catchment_2024['LWD'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean longwave downward
north_2000_lwd = north_catchment_2000['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2001_lwd = north_catchment_2001['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2002_lwd = north_catchment_2002['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2003_lwd = north_catchment_2003['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2004_lwd = north_catchment_2004['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2005_lwd = north_catchment_2005['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2006_lwd = north_catchment_2006['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2007_lwd = north_catchment_2007['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2008_lwd = north_catchment_2008['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2009_lwd = north_catchment_2009['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2010_lwd = north_catchment_2010['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2011_lwd = north_catchment_2011['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2012_lwd = north_catchment_2012['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2013_lwd = north_catchment_2013['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2014_lwd = north_catchment_2014['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2015_lwd = north_catchment_2015['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2016_lwd = north_catchment_2016['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2017_lwd = north_catchment_2017['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2018_lwd = north_catchment_2018['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2019_lwd = north_catchment_2019['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2020_lwd = north_catchment_2020['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2021_lwd = north_catchment_2021['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2022_lwd = north_catchment_2022['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2023_lwd = north_catchment_2023['LWD'].mean(dim=("y", "x"), skipna=True).values
north_2024_lwd = north_catchment_2024['LWD'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean longwave upward
rb_2000_lwu = rb_catchment_2000['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2001_lwu = rb_catchment_2001['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2002_lwu = rb_catchment_2002['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2003_lwu = rb_catchment_2003['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2004_lwu = rb_catchment_2004['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2005_lwu = rb_catchment_2005['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2006_lwu = rb_catchment_2006['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2007_lwu = rb_catchment_2007['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2008_lwu = rb_catchment_2008['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2009_lwu = rb_catchment_2009['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2010_lwu = rb_catchment_2010['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2011_lwu = rb_catchment_2011['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2012_lwu = rb_catchment_2012['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2013_lwu = rb_catchment_2013['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2014_lwu = rb_catchment_2014['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2015_lwu = rb_catchment_2015['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2016_lwu = rb_catchment_2016['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2017_lwu = rb_catchment_2017['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2018_lwu = rb_catchment_2018['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2019_lwu = rb_catchment_2019['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2020_lwu = rb_catchment_2020['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2021_lwu = rb_catchment_2021['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2022_lwu = rb_catchment_2022['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2023_lwu = rb_catchment_2023['LWU'].mean(dim=("y", "x"), skipna=True).values
rb_2024_lwu = rb_catchment_2024['LWU'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean longwave upward
ak4_2000_lwu = ak4_catchment_2000['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_lwu = ak4_catchment_2001['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_lwu = ak4_catchment_2002['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_lwu = ak4_catchment_2003['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_lwu = ak4_catchment_2004['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_lwu = ak4_catchment_2005['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_lwu = ak4_catchment_2006['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_lwu = ak4_catchment_2007['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_lwu = ak4_catchment_2008['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_lwu = ak4_catchment_2009['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_lwu = ak4_catchment_2010['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_lwu = ak4_catchment_2011['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_lwu = ak4_catchment_2012['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_lwu = ak4_catchment_2013['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_lwu = ak4_catchment_2014['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_lwu = ak4_catchment_2015['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_lwu = ak4_catchment_2016['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_lwu = ak4_catchment_2017['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_lwu = ak4_catchment_2018['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_lwu = ak4_catchment_2019['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_lwu = ak4_catchment_2020['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_lwu = ak4_catchment_2021['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_lwu = ak4_catchment_2022['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_lwu = ak4_catchment_2023['LWU'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_lwu = ak4_catchment_2024['LWU'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean longwave upward
minturn_2000_lwu = minturn_catchment_2000['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_lwu = minturn_catchment_2001['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_lwu = minturn_catchment_2002['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_lwu = minturn_catchment_2003['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_lwu = minturn_catchment_2004['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_lwu = minturn_catchment_2005['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_lwu = minturn_catchment_2006['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_lwu = minturn_catchment_2007['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_lwu = minturn_catchment_2008['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_lwu = minturn_catchment_2009['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_lwu = minturn_catchment_2010['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_lwu = minturn_catchment_2011['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_lwu = minturn_catchment_2012['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_lwu = minturn_catchment_2013['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_lwu = minturn_catchment_2014['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_lwu = minturn_catchment_2015['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_lwu = minturn_catchment_2016['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_lwu = minturn_catchment_2017['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_lwu = minturn_catchment_2018['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_lwu = minturn_catchment_2019['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_lwu = minturn_catchment_2020['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_lwu = minturn_catchment_2021['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_lwu = minturn_catchment_2022['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_lwu = minturn_catchment_2023['LWU'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_lwu = minturn_catchment_2024['LWU'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean longwave upward
north_2000_lwu = north_catchment_2000['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2001_lwu = north_catchment_2001['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2002_lwu = north_catchment_2002['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2003_lwu = north_catchment_2003['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2004_lwu = north_catchment_2004['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2005_lwu = north_catchment_2005['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2006_lwu = north_catchment_2006['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2007_lwu = north_catchment_2007['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2008_lwu = north_catchment_2008['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2009_lwu = north_catchment_2009['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2010_lwu = north_catchment_2010['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2011_lwu = north_catchment_2011['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2012_lwu = north_catchment_2012['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2013_lwu = north_catchment_2013['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2014_lwu = north_catchment_2014['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2015_lwu = north_catchment_2015['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2016_lwu = north_catchment_2016['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2017_lwu = north_catchment_2017['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2018_lwu = north_catchment_2018['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2019_lwu = north_catchment_2019['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2020_lwu = north_catchment_2020['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2021_lwu = north_catchment_2021['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2022_lwu = north_catchment_2022['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2023_lwu = north_catchment_2023['LWU'].mean(dim=("y", "x"), skipna=True).values
north_2024_lwu = north_catchment_2024['LWU'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean sensible heat flux
rb_2000_shf = rb_catchment_2000['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2001_shf = rb_catchment_2001['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2002_shf = rb_catchment_2002['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2003_shf = rb_catchment_2003['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2004_shf = rb_catchment_2004['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2005_shf = rb_catchment_2005['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2006_shf = rb_catchment_2006['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2007_shf = rb_catchment_2007['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2008_shf = rb_catchment_2008['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2009_shf = rb_catchment_2009['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2010_shf = rb_catchment_2010['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2011_shf = rb_catchment_2011['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2012_shf = rb_catchment_2012['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2013_shf = rb_catchment_2013['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2014_shf = rb_catchment_2014['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2015_shf = rb_catchment_2015['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2016_shf = rb_catchment_2016['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2017_shf = rb_catchment_2017['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2018_shf = rb_catchment_2018['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2019_shf = rb_catchment_2019['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2020_shf = rb_catchment_2020['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2021_shf = rb_catchment_2021['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2022_shf = rb_catchment_2022['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2023_shf = rb_catchment_2023['SHF'].mean(dim=("y", "x"), skipna=True).values
rb_2024_shf = rb_catchment_2024['SHF'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean sensible heat flux
ak4_2000_shf = ak4_catchment_2000['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_shf = ak4_catchment_2001['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_shf = ak4_catchment_2002['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_shf = ak4_catchment_2003['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_shf = ak4_catchment_2004['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_shf = ak4_catchment_2005['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_shf = ak4_catchment_2006['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_shf = ak4_catchment_2007['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_shf = ak4_catchment_2008['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_shf = ak4_catchment_2009['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_shf = ak4_catchment_2010['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_shf = ak4_catchment_2011['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_shf = ak4_catchment_2012['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_shf = ak4_catchment_2013['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_shf = ak4_catchment_2014['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_shf = ak4_catchment_2015['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_shf = ak4_catchment_2016['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_shf = ak4_catchment_2017['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_shf = ak4_catchment_2018['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_shf = ak4_catchment_2019['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_shf = ak4_catchment_2020['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_shf = ak4_catchment_2021['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_shf = ak4_catchment_2022['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_shf = ak4_catchment_2023['SHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_shf = ak4_catchment_2024['SHF'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean sensible heat flux
minturn_2000_shf = minturn_catchment_2000['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_shf = minturn_catchment_2001['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_shf = minturn_catchment_2002['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_shf = minturn_catchment_2003['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_shf = minturn_catchment_2004['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_shf = minturn_catchment_2005['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_shf = minturn_catchment_2006['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_shf = minturn_catchment_2007['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_shf = minturn_catchment_2008['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_shf = minturn_catchment_2009['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_shf = minturn_catchment_2010['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_shf = minturn_catchment_2011['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_shf = minturn_catchment_2012['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_shf = minturn_catchment_2013['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_shf = minturn_catchment_2014['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_shf = minturn_catchment_2015['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_shf = minturn_catchment_2016['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_shf = minturn_catchment_2017['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_shf = minturn_catchment_2018['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_shf = minturn_catchment_2019['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_shf = minturn_catchment_2020['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_shf = minturn_catchment_2021['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_shf = minturn_catchment_2022['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_shf = minturn_catchment_2023['SHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_shf = minturn_catchment_2024['SHF'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean sensible heat flux
north_2000_shf = north_catchment_2000['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2001_shf = north_catchment_2001['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2002_shf = north_catchment_2002['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2003_shf = north_catchment_2003['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2004_shf = north_catchment_2004['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2005_shf = north_catchment_2005['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2006_shf = north_catchment_2006['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2007_shf = north_catchment_2007['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2008_shf = north_catchment_2008['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2009_shf = north_catchment_2009['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2010_shf = north_catchment_2010['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2011_shf = north_catchment_2011['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2012_shf = north_catchment_2012['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2013_shf = north_catchment_2013['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2014_shf = north_catchment_2014['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2015_shf = north_catchment_2015['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2016_shf = north_catchment_2016['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2017_shf = north_catchment_2017['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2018_shf = north_catchment_2018['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2019_shf = north_catchment_2019['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2020_shf = north_catchment_2020['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2021_shf = north_catchment_2021['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2022_shf = north_catchment_2022['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2023_shf = north_catchment_2023['SHF'].mean(dim=("y", "x"), skipna=True).values
north_2024_shf = north_catchment_2024['SHF'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean latent heat flux
rb_2000_lhf = rb_catchment_2000['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2001_lhf = rb_catchment_2001['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2002_lhf = rb_catchment_2002['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2003_lhf = rb_catchment_2003['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2004_lhf = rb_catchment_2004['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2005_lhf = rb_catchment_2005['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2006_lhf = rb_catchment_2006['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2007_lhf = rb_catchment_2007['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2008_lhf = rb_catchment_2008['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2009_lhf = rb_catchment_2009['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2010_lhf = rb_catchment_2010['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2011_lhf = rb_catchment_2011['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2012_lhf = rb_catchment_2012['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2013_lhf = rb_catchment_2013['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2014_lhf = rb_catchment_2014['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2015_lhf = rb_catchment_2015['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2016_lhf = rb_catchment_2016['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2017_lhf = rb_catchment_2017['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2018_lhf = rb_catchment_2018['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2019_lhf = rb_catchment_2019['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2020_lhf = rb_catchment_2020['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2021_lhf = rb_catchment_2021['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2022_lhf = rb_catchment_2022['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2023_lhf = rb_catchment_2023['LHF'].mean(dim=("y", "x"), skipna=True).values
rb_2024_lhf = rb_catchment_2024['LHF'].mean(dim=("y", "x"), skipna=True).values

# AK4 catchment mean latent heat flux
ak4_2000_lhf = ak4_catchment_2000['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2001_lhf = ak4_catchment_2001['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2002_lhf = ak4_catchment_2002['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2003_lhf = ak4_catchment_2003['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2004_lhf = ak4_catchment_2004['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2005_lhf = ak4_catchment_2005['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2006_lhf = ak4_catchment_2006['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2007_lhf = ak4_catchment_2007['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2008_lhf = ak4_catchment_2008['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2009_lhf = ak4_catchment_2009['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2010_lhf = ak4_catchment_2010['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2011_lhf = ak4_catchment_2011['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2012_lhf = ak4_catchment_2012['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2013_lhf = ak4_catchment_2013['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2014_lhf = ak4_catchment_2014['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2015_lhf = ak4_catchment_2015['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2016_lhf = ak4_catchment_2016['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2017_lhf = ak4_catchment_2017['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2018_lhf = ak4_catchment_2018['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2019_lhf = ak4_catchment_2019['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2020_lhf = ak4_catchment_2020['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2021_lhf = ak4_catchment_2021['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2022_lhf = ak4_catchment_2022['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2023_lhf = ak4_catchment_2023['LHF'].mean(dim=("y", "x"), skipna=True).values
ak4_2024_lhf = ak4_catchment_2024['LHF'].mean(dim=("y", "x"), skipna=True).values

# Minturn catchment mean latent heat flux
minturn_2000_lhf = minturn_catchment_2000['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2001_lhf = minturn_catchment_2001['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2002_lhf = minturn_catchment_2002['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2003_lhf = minturn_catchment_2003['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2004_lhf = minturn_catchment_2004['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2005_lhf = minturn_catchment_2005['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2006_lhf = minturn_catchment_2006['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2007_lhf = minturn_catchment_2007['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2008_lhf = minturn_catchment_2008['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2009_lhf = minturn_catchment_2009['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2010_lhf = minturn_catchment_2010['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2011_lhf = minturn_catchment_2011['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2012_lhf = minturn_catchment_2012['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2013_lhf = minturn_catchment_2013['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2014_lhf = minturn_catchment_2014['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2015_lhf = minturn_catchment_2015['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2016_lhf = minturn_catchment_2016['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2017_lhf = minturn_catchment_2017['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2018_lhf = minturn_catchment_2018['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2019_lhf = minturn_catchment_2019['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2020_lhf = minturn_catchment_2020['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2021_lhf = minturn_catchment_2021['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2022_lhf = minturn_catchment_2022['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2023_lhf = minturn_catchment_2023['LHF'].mean(dim=("y", "x"), skipna=True).values
minturn_2024_lhf = minturn_catchment_2024['LHF'].mean(dim=("y", "x"), skipna=True).values

# North catchment mean latent heat flux
north_2000_lhf = north_catchment_2000['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2001_lhf = north_catchment_2001['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2002_lhf = north_catchment_2002['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2003_lhf = north_catchment_2003['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2004_lhf = north_catchment_2004['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2005_lhf = north_catchment_2005['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2006_lhf = north_catchment_2006['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2007_lhf = north_catchment_2007['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2008_lhf = north_catchment_2008['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2009_lhf = north_catchment_2009['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2010_lhf = north_catchment_2010['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2011_lhf = north_catchment_2011['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2012_lhf = north_catchment_2012['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2013_lhf = north_catchment_2013['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2014_lhf = north_catchment_2014['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2015_lhf = north_catchment_2015['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2016_lhf = north_catchment_2016['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2017_lhf = north_catchment_2017['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2018_lhf = north_catchment_2018['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2019_lhf = north_catchment_2019['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2020_lhf = north_catchment_2020['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2021_lhf = north_catchment_2021['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2022_lhf = north_catchment_2022['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2023_lhf = north_catchment_2023['LHF'].mean(dim=("y", "x"), skipna=True).values
north_2024_lhf = north_catchment_2024['LHF'].mean(dim=("y", "x"), skipna=True).values

# Rio Behar catchment mean surface energy balance
# SEB = (SWD - SWU) + (LWD - LWU) + SHF + LHF
rb_2000_seb = (rb_2000_swd - rb_2000_swu) + (rb_2000_lwd - rb_2000_lwu) + rb_2000_shf + rb_2000_lhf
rb_2001_seb = (rb_2001_swd - rb_2001_swu) + (rb_2001_lwd - rb_2001_lwu) + rb_2001_shf + rb_2001_lhf
rb_2002_seb = (rb_2002_swd - rb_2002_swu) + (rb_2002_lwd - rb_2002_lwu) + rb_2002_shf + rb_2002_lhf
rb_2003_seb = (rb_2003_swd - rb_2003_swu) + (rb_2003_lwd - rb_2003_lwu) + rb_2003_shf + rb_2003_lhf
rb_2004_seb = (rb_2004_swd - rb_2004_swu) + (rb_2004_lwd - rb_2004_lwu) + rb_2004_shf + rb_2004_lhf
rb_2005_seb = (rb_2005_swd - rb_2005_swu) + (rb_2005_lwd - rb_2005_lwu) + rb_2005_shf + rb_2005_lhf
rb_2006_seb = (rb_2006_swd - rb_2006_swu) + (rb_2006_lwd - rb_2006_lwu) + rb_2006_shf + rb_2006_lhf
rb_2007_seb = (rb_2007_swd - rb_2007_swu) + (rb_2007_lwd - rb_2007_lwu) + rb_2007_shf + rb_2007_lhf
rb_2008_seb = (rb_2008_swd - rb_2008_swu) + (rb_2008_lwd - rb_2008_lwu) + rb_2008_shf + rb_2008_lhf
rb_2009_seb = (rb_2009_swd - rb_2009_swu) + (rb_2009_lwd - rb_2009_lwu) + rb_2009_shf + rb_2009_lhf
rb_2010_seb = (rb_2010_swd - rb_2010_swu) + (rb_2010_lwd - rb_2010_lwu) + rb_2010_shf + rb_2010_lhf
rb_2011_seb = (rb_2011_swd - rb_2011_swu) + (rb_2011_lwd - rb_2011_lwu) + rb_2011_shf + rb_2011_lhf
rb_2012_seb = (rb_2012_swd - rb_2012_swu) + (rb_2012_lwd - rb_2012_lwu) + rb_2012_shf + rb_2012_lhf
rb_2013_seb = (rb_2013_swd - rb_2013_swu) + (rb_2013_lwd - rb_2013_lwu) + rb_2013_shf + rb_2013_lhf
rb_2014_seb = (rb_2014_swd - rb_2014_swu) + (rb_2014_lwd - rb_2014_lwu) + rb_2014_shf + rb_2014_lhf
rb_2015_seb = (rb_2015_swd - rb_2015_swu) + (rb_2015_lwd - rb_2015_lwu) + rb_2015_shf + rb_2015_lhf
rb_2016_seb = (rb_2016_swd - rb_2016_swu) + (rb_2016_lwd - rb_2016_lwu) + rb_2016_shf + rb_2016_lhf
rb_2017_seb = (rb_2017_swd - rb_2017_swu) + (rb_2017_lwd - rb_2017_lwu) + rb_2017_shf + rb_2017_lhf
rb_2018_seb = (rb_2018_swd - rb_2018_swu) + (rb_2018_lwd - rb_2018_lwu) + rb_2018_shf + rb_2018_lhf
rb_2019_seb = (rb_2019_swd - rb_2019_swu) + (rb_2019_lwd - rb_2019_lwu) + rb_2019_shf + rb_2019_lhf
rb_2020_seb = (rb_2020_swd - rb_2020_swu) + (rb_2020_lwd - rb_2020_lwu) + rb_2020_shf + rb_2020_lhf
rb_2021_seb = (rb_2021_swd - rb_2021_swu) + (rb_2021_lwd - rb_2021_lwu) + rb_2021_shf + rb_2021_lhf
rb_2022_seb = (rb_2022_swd - rb_2022_swu) + (rb_2022_lwd - rb_2022_lwu) + rb_2022_shf + rb_2022_lhf
rb_2023_seb = (rb_2023_swd - rb_2023_swu) + (rb_2023_lwd - rb_2023_lwu) + rb_2023_shf + rb_2023_lhf
rb_2024_seb = (rb_2024_swd - rb_2024_swu) + (rb_2024_lwd - rb_2024_lwu) + rb_2024_shf + rb_2024_lhf

# AK4 catchment mean surface energy balance
# SEB = (SWD - SWU) + (LWD - LWU) + SHF + LHF
ak4_2000_seb = (ak4_2000_swd - ak4_2000_swu) + (ak4_2000_lwd - ak4_2000_lwu) + ak4_2000_shf + ak4_2000_lhf
ak4_2001_seb = (ak4_2001_swd - ak4_2001_swu) + (ak4_2001_lwd - ak4_2001_lwu) + ak4_2001_shf + ak4_2001_lhf
ak4_2002_seb = (ak4_2002_swd - ak4_2002_swu) + (ak4_2002_lwd - ak4_2002_lwu) + ak4_2002_shf + ak4_2002_lhf
ak4_2003_seb = (ak4_2003_swd - ak4_2003_swu) + (ak4_2003_lwd - ak4_2003_lwu) + ak4_2003_shf + ak4_2003_lhf
ak4_2004_seb = (ak4_2004_swd - ak4_2004_swu) + (ak4_2004_lwd - ak4_2004_lwu) + ak4_2004_shf + ak4_2004_lhf
ak4_2005_seb = (ak4_2005_swd - ak4_2005_swu) + (ak4_2005_lwd - ak4_2005_lwu) + ak4_2005_shf + ak4_2005_lhf
ak4_2006_seb = (ak4_2006_swd - ak4_2006_swu) + (ak4_2006_lwd - ak4_2006_lwu) + ak4_2006_shf + ak4_2006_lhf
ak4_2007_seb = (ak4_2007_swd - ak4_2007_swu) + (ak4_2007_lwd - ak4_2007_lwu) + ak4_2007_shf + ak4_2007_lhf
ak4_2008_seb = (ak4_2008_swd - ak4_2008_swu) + (ak4_2008_lwd - ak4_2008_lwu) + ak4_2008_shf + ak4_2008_lhf
ak4_2009_seb = (ak4_2009_swd - ak4_2009_swu) + (ak4_2009_lwd - ak4_2009_lwu) + ak4_2009_shf + ak4_2009_lhf
ak4_2010_seb = (ak4_2010_swd - ak4_2010_swu) + (ak4_2010_lwd - ak4_2010_lwu) + ak4_2010_shf + ak4_2010_lhf
ak4_2011_seb = (ak4_2011_swd - ak4_2011_swu) + (ak4_2011_lwd - ak4_2011_lwu) + ak4_2011_shf + ak4_2011_lhf
ak4_2012_seb = (ak4_2012_swd - ak4_2012_swu) + (ak4_2012_lwd - ak4_2012_lwu) + ak4_2012_shf + ak4_2012_lhf
ak4_2013_seb = (ak4_2013_swd - ak4_2013_swu) + (ak4_2013_lwd - ak4_2013_lwu) + ak4_2013_shf + ak4_2013_lhf
ak4_2014_seb = (ak4_2014_swd - ak4_2014_swu) + (ak4_2014_lwd - ak4_2014_lwu) + ak4_2014_shf + ak4_2014_lhf
ak4_2015_seb = (ak4_2015_swd - ak4_2015_swu) + (ak4_2015_lwd - ak4_2015_lwu) + ak4_2015_shf + ak4_2015_lhf
ak4_2016_seb = (ak4_2016_swd - ak4_2016_swu) + (ak4_2016_lwd - ak4_2016_lwu) + ak4_2016_shf + ak4_2016_lhf
ak4_2017_seb = (ak4_2017_swd - ak4_2017_swu) + (ak4_2017_lwd - ak4_2017_lwu) + ak4_2017_shf + ak4_2017_lhf
ak4_2018_seb = (ak4_2018_swd - ak4_2018_swu) + (ak4_2018_lwd - ak4_2018_lwu) + ak4_2018_shf + ak4_2018_lhf
ak4_2019_seb = (ak4_2019_swd - ak4_2019_swu) + (ak4_2019_lwd - ak4_2019_lwu) + ak4_2019_shf + ak4_2019_lhf
ak4_2020_seb = (ak4_2020_swd - ak4_2020_swu) + (ak4_2020_lwd - ak4_2020_lwu) + ak4_2020_shf + ak4_2020_lhf
ak4_2021_seb = (ak4_2021_swd - ak4_2021_swu) + (ak4_2021_lwd - ak4_2021_lwu) + ak4_2021_shf + ak4_2021_lhf
ak4_2022_seb = (ak4_2022_swd - ak4_2022_swu) + (ak4_2022_lwd - ak4_2022_lwu) + ak4_2022_shf + ak4_2022_lhf
ak4_2023_seb = (ak4_2023_swd - ak4_2023_swu) + (ak4_2023_lwd - ak4_2023_lwu) + ak4_2023_shf + ak4_2023_lhf
ak4_2024_seb = (ak4_2024_swd - ak4_2024_swu) + (ak4_2024_lwd - ak4_2024_lwu) + ak4_2024_shf + ak4_2024_lhf

# Minturn catchment mean surface energy balance
# SEB = (SWD - SWU) + (LWD - LWU) + SHF + LHF
minturn_2000_seb = (minturn_2000_swd - minturn_2000_swu) + (minturn_2000_lwd - minturn_2000_lwu) + minturn_2000_shf + minturn_2000_lhf
minturn_2001_seb = (minturn_2001_swd - minturn_2001_swu) + (minturn_2001_lwd - minturn_2001_lwu) + minturn_2001_shf + minturn_2001_lhf
minturn_2002_seb = (minturn_2002_swd - minturn_2002_swu) + (minturn_2002_lwd - minturn_2002_lwu) + minturn_2002_shf + minturn_2002_lhf
minturn_2003_seb = (minturn_2003_swd - minturn_2003_swu) + (minturn_2003_lwd - minturn_2003_lwu) + minturn_2003_shf + minturn_2003_lhf
minturn_2004_seb = (minturn_2004_swd - minturn_2004_swu) + (minturn_2004_lwd - minturn_2004_lwu) + minturn_2004_shf + minturn_2004_lhf
minturn_2005_seb = (minturn_2005_swd - minturn_2005_swu) + (minturn_2005_lwd - minturn_2005_lwu) + minturn_2005_shf + minturn_2005_lhf
minturn_2006_seb = (minturn_2006_swd - minturn_2006_swu) + (minturn_2006_lwd - minturn_2006_lwu) + minturn_2006_shf + minturn_2006_lhf
minturn_2007_seb = (minturn_2007_swd - minturn_2007_swu) + (minturn_2007_lwd - minturn_2007_lwu) + minturn_2007_shf + minturn_2007_lhf
minturn_2008_seb = (minturn_2008_swd - minturn_2008_swu) + (minturn_2008_lwd - minturn_2008_lwu) + minturn_2008_shf + minturn_2008_lhf
minturn_2009_seb = (minturn_2009_swd - minturn_2009_swu) + (minturn_2009_lwd - minturn_2009_lwu) + minturn_2009_shf + minturn_2009_lhf
minturn_2010_seb = (minturn_2010_swd - minturn_2010_swu) + (minturn_2010_lwd - minturn_2010_lwu) + minturn_2010_shf + minturn_2010_lhf
minturn_2011_seb = (minturn_2011_swd - minturn_2011_swu) + (minturn_2011_lwd - minturn_2011_lwu) + minturn_2011_shf + minturn_2011_lhf
minturn_2012_seb = (minturn_2012_swd - minturn_2012_swu) + (minturn_2012_lwd - minturn_2012_lwu) + minturn_2012_shf + minturn_2012_lhf
minturn_2013_seb = (minturn_2013_swd - minturn_2013_swu) + (minturn_2013_lwd - minturn_2013_lwu) + minturn_2013_shf + minturn_2013_lhf
minturn_2014_seb = (minturn_2014_swd - minturn_2014_swu) + (minturn_2014_lwd - minturn_2014_lwu) + minturn_2014_shf + minturn_2014_lhf
minturn_2015_seb = (minturn_2015_swd - minturn_2015_swu) + (minturn_2015_lwd - minturn_2015_lwu) + minturn_2015_shf + minturn_2015_lhf
minturn_2016_seb = (minturn_2016_swd - minturn_2016_swu) + (minturn_2016_lwd - minturn_2016_lwu) + minturn_2016_shf + minturn_2016_lhf
minturn_2017_seb = (minturn_2017_swd - minturn_2017_swu) + (minturn_2017_lwd - minturn_2017_lwu) + minturn_2017_shf + minturn_2017_lhf
minturn_2018_seb = (minturn_2018_swd - minturn_2018_swu) + (minturn_2018_lwd - minturn_2018_lwu) + minturn_2018_shf + minturn_2018_lhf
minturn_2019_seb = (minturn_2019_swd - minturn_2019_swu) + (minturn_2019_lwd - minturn_2019_lwu) + minturn_2019_shf + minturn_2019_lhf
minturn_2020_seb = (minturn_2020_swd - minturn_2020_swu) + (minturn_2020_lwd - minturn_2020_lwu) + minturn_2020_shf + minturn_2020_lhf
minturn_2021_seb = (minturn_2021_swd - minturn_2021_swu) + (minturn_2021_lwd - minturn_2021_lwu) + minturn_2021_shf + minturn_2021_lhf
minturn_2022_seb = (minturn_2022_swd - minturn_2022_swu) + (minturn_2022_lwd - minturn_2022_lwu) + minturn_2022_shf + minturn_2022_lhf
minturn_2023_seb = (minturn_2023_swd - minturn_2023_swu) + (minturn_2023_lwd - minturn_2023_lwu) + minturn_2023_shf + minturn_2023_lhf
minturn_2024_seb = (minturn_2024_swd - minturn_2024_swu) + (minturn_2024_lwd - minturn_2024_lwu) + minturn_2024_shf + minturn_2024_lhf

# North catchment mean surface energy balance
# SEB = (SWD - SWU) + (LWD - LWU) + SHF + LHF
north_2000_seb = (north_2000_swd - north_2000_swu) + (north_2000_lwd - north_2000_lwu) + north_2000_shf + north_2000_lhf
north_2001_seb = (north_2001_swd - north_2001_swu) + (north_2001_lwd - north_2001_lwu) + north_2001_shf + north_2001_lhf
north_2002_seb = (north_2002_swd - north_2002_swu) + (north_2002_lwd - north_2002_lwu) + north_2002_shf + north_2002_lhf
north_2003_seb = (north_2003_swd - north_2003_swu) + (north_2003_lwd - north_2003_lwu) + north_2003_shf + north_2003_lhf
north_2004_seb = (north_2004_swd - north_2004_swu) + (north_2004_lwd - north_2004_lwu) + north_2004_shf + north_2004_lhf
north_2005_seb = (north_2005_swd - north_2005_swu) + (north_2005_lwd - north_2005_lwu) + north_2005_shf + north_2005_lhf
north_2006_seb = (north_2006_swd - north_2006_swu) + (north_2006_lwd - north_2006_lwu) + north_2006_shf + north_2006_lhf
north_2007_seb = (north_2007_swd - north_2007_swu) + (north_2007_lwd - north_2007_lwu) + north_2007_shf + north_2007_lhf
north_2008_seb = (north_2008_swd - north_2008_swu) + (north_2008_lwd - north_2008_lwu) + north_2008_shf + north_2008_lhf
north_2009_seb = (north_2009_swd - north_2009_swu) + (north_2009_lwd - north_2009_lwu) + north_2009_shf + north_2009_lhf
north_2010_seb = (north_2010_swd - north_2010_swu) + (north_2010_lwd - north_2010_lwu) + north_2010_shf + north_2010_lhf
north_2011_seb = (north_2011_swd - north_2011_swu) + (north_2011_lwd - north_2011_lwu) + north_2011_shf + north_2011_lhf
north_2012_seb = (north_2012_swd - north_2012_swu) + (north_2012_lwd - north_2012_lwu) + north_2012_shf + north_2012_lhf
north_2013_seb = (north_2013_swd - north_2013_swu) + (north_2013_lwd - north_2013_lwu) + north_2013_shf + north_2013_lhf
north_2014_seb = (north_2014_swd - north_2014_swu) + (north_2014_lwd - north_2014_lwu) + north_2014_shf + north_2014_lhf
north_2015_seb = (north_2015_swd - north_2015_swu) + (north_2015_lwd - north_2015_lwu) + north_2015_shf + north_2015_lhf
north_2016_seb = (north_2016_swd - north_2016_swu) + (north_2016_lwd - north_2016_lwu) + north_2016_shf + north_2016_lhf
north_2017_seb = (north_2017_swd - north_2017_swu) + (north_2017_lwd - north_2017_lwu) + north_2017_shf + north_2017_lhf
north_2018_seb = (north_2018_swd - north_2018_swu) + (north_2018_lwd - north_2018_lwu) + north_2018_shf + north_2018_lhf
north_2019_seb = (north_2019_swd - north_2019_swu) + (north_2019_lwd - north_2019_lwu) + north_2019_shf + north_2019_lhf
north_2020_seb = (north_2020_swd - north_2020_swu) + (north_2020_lwd - north_2020_lwu) + north_2020_shf + north_2020_lhf
north_2021_seb = (north_2021_swd - north_2021_swu) + (north_2021_lwd - north_2021_lwu) + north_2021_shf + north_2021_lhf
north_2022_seb = (north_2022_swd - north_2022_swu) + (north_2022_lwd - north_2022_lwu) + north_2022_shf + north_2022_lhf
north_2023_seb = (north_2023_swd - north_2023_swu) + (north_2023_lwd - north_2023_lwu) + north_2023_shf + north_2023_lhf
north_2024_seb = (north_2024_swd - north_2024_swu) + (north_2024_lwd - north_2024_lwu) + north_2024_shf + north_2024_lhf

# Rio Behar catchment area-weighted mean runoff = meltwater + rainfall
# Use Sector 0 for runoff
rb_effective_area_2000 = rb_catchment_2000['AREA'] * rb_fraction
rb_2000_ru = ((rb_catchment_2000['RU'].isel(SECTOR=0) * rb_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
rb_2000_ru = rb_2000_ru.to_array().to_numpy().T

rb_effective_area_2001 = rb_catchment_2001['AREA'] * rb_fraction
rb_2001_ru = ((rb_catchment_2001['RU'].isel(SECTOR=0) * rb_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
rb_2001_ru = rb_2001_ru.to_array().to_numpy().T

rb_effective_area_2002 = rb_catchment_2002['AREA'] * rb_fraction
rb_2002_ru = ((rb_catchment_2002['RU'].isel(SECTOR=0) * rb_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
rb_2002_ru = rb_2002_ru.to_array().to_numpy().T

rb_effective_area_2003 = rb_catchment_2003['AREA'] * rb_fraction
rb_2003_ru = ((rb_catchment_2003['RU'].isel(SECTOR=0) * rb_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
rb_2003_ru = rb_2003_ru.to_array().to_numpy().T

rb_effective_area_2004 = rb_catchment_2004['AREA'] * rb_fraction
rb_2004_ru = ((rb_catchment_2004['RU'].isel(SECTOR=0) * rb_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
rb_2004_ru = rb_2004_ru.to_array().to_numpy().T

rb_effective_area_2005 = rb_catchment_2005['AREA'] * rb_fraction
rb_2005_ru = ((rb_catchment_2005['RU'].isel(SECTOR=0) * rb_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
rb_2005_ru = rb_2005_ru.to_array().to_numpy().T

rb_effective_area_2006 = rb_catchment_2006['AREA'] * rb_fraction
rb_2006_ru = ((rb_catchment_2006['RU'].isel(SECTOR=0) * rb_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
rb_2006_ru = rb_2006_ru.to_array().to_numpy().T

rb_effective_area_2007 = rb_catchment_2007['AREA'] * rb_fraction
rb_2007_ru = ((rb_catchment_2007['RU'].isel(SECTOR=0) * rb_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
rb_2007_ru = rb_2007_ru.to_array().to_numpy().T

rb_effective_area_2008 = rb_catchment_2008['AREA'] * rb_fraction
rb_2008_ru = ((rb_catchment_2008['RU'].isel(SECTOR=0) * rb_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
rb_2008_ru = rb_2008_ru.to_array().to_numpy().T

rb_effective_area_2009 = rb_catchment_2009['AREA'] * rb_fraction
rb_2009_ru = ((rb_catchment_2009['RU'].isel(SECTOR=0) * rb_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
rb_2009_ru = rb_2009_ru.to_array().to_numpy().T

rb_effective_area_2010 = rb_catchment_2010['AREA'] * rb_fraction
rb_2010_ru = ((rb_catchment_2010['RU'].isel(SECTOR=0) * rb_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
rb_2010_ru = rb_2010_ru.to_array().to_numpy().T

rb_effective_area_2011 = rb_catchment_2011['AREA'] * rb_fraction
rb_2011_ru = ((rb_catchment_2011['RU'].isel(SECTOR=0) * rb_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
rb_2011_ru = rb_2011_ru.to_array().to_numpy().T

rb_effective_area_2012 = rb_catchment_2012['AREA'] * rb_fraction
rb_2012_ru = ((rb_catchment_2012['RU'].isel(SECTOR=0) * rb_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
rb_2012_ru = rb_2012_ru.to_array().to_numpy().T

rb_effective_area_2013 = rb_catchment_2013['AREA'] * rb_fraction
rb_2013_ru = ((rb_catchment_2013['RU'].isel(SECTOR=0) * rb_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
rb_2013_ru = rb_2013_ru.to_array().to_numpy().T

rb_effective_area_2014 = rb_catchment_2014['AREA'] * rb_fraction
rb_2014_ru = ((rb_catchment_2014['RU'].isel(SECTOR=0) * rb_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
rb_2014_ru = rb_2014_ru.to_array().to_numpy().T

rb_effective_area_2015 = rb_catchment_2015['AREA'] * rb_fraction
rb_2015_ru = ((rb_catchment_2015['RU'].isel(SECTOR=0) * rb_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
rb_2015_ru = rb_2015_ru.to_array().to_numpy().T

rb_effective_area_2016 = rb_catchment_2016['AREA'] * rb_fraction
rb_2016_ru = ((rb_catchment_2016['RU'].isel(SECTOR=0) * rb_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
rb_2016_ru = rb_2016_ru.to_array().to_numpy().T

rb_effective_area_2017 = rb_catchment_2017['AREA'] * rb_fraction
rb_2017_ru = ((rb_catchment_2017['RU'].isel(SECTOR=0) * rb_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
rb_2017_ru = rb_2017_ru.to_array().to_numpy().T

rb_effective_area_2018 = rb_catchment_2018['AREA'] * rb_fraction
rb_2018_ru = ((rb_catchment_2018['RU'].isel(SECTOR=0) * rb_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
rb_2018_ru = rb_2018_ru.to_array().to_numpy().T

rb_effective_area_2019 = rb_catchment_2019['AREA'] * rb_fraction
rb_2019_ru = ((rb_catchment_2019['RU'].isel(SECTOR=0) * rb_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
rb_2019_ru = rb_2019_ru.to_array().to_numpy().T

rb_effective_area_2020 = rb_catchment_2020['AREA'] * rb_fraction
rb_2020_ru = ((rb_catchment_2020['RU'].isel(SECTOR=0) * rb_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
rb_2020_ru = rb_2020_ru.to_array().to_numpy().T

rb_effective_area_2021 = rb_catchment_2021['AREA'] * rb_fraction
rb_2021_ru = ((rb_catchment_2021['RU'].isel(SECTOR=0) * rb_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
rb_2021_ru = rb_2021_ru.to_array().to_numpy().T

rb_effective_area_2022 = rb_catchment_2022['AREA'] * rb_fraction
rb_2022_ru = ((rb_catchment_2022['RU'].isel(SECTOR=0) * rb_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
rb_2022_ru = rb_2022_ru.to_array().to_numpy().T

rb_effective_area_2023 = rb_catchment_2023['AREA'] * rb_fraction
rb_2023_ru = ((rb_catchment_2023['RU'].isel(SECTOR=0) * rb_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
rb_2023_ru = rb_2023_ru.to_array().to_numpy().T

rb_effective_area_2024 = rb_catchment_2024['AREA'] * rb_fraction
rb_2024_ru = ((rb_catchment_2024['RU'].isel(SECTOR=0) * rb_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
rb_2024_ru = rb_2024_ru.to_array().to_numpy().T

# AK4 catchment area-weighted mean runoff = meltwater + rainfall
# Use Sector 0 for runoff
ak4_effective_area_2000 = ak4_catchment_2000['AREA'] * ak4_fraction
ak4_2000_ru = ((ak4_catchment_2000['RU'].isel(SECTOR=0) * ak4_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
ak4_2000_ru = ak4_2000_ru.to_array().to_numpy().T

ak4_effective_area_2001 = ak4_catchment_2001['AREA'] * ak4_fraction
ak4_2001_ru = ((ak4_catchment_2001['RU'].isel(SECTOR=0) * ak4_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
ak4_2001_ru = ak4_2001_ru.to_array().to_numpy().T

ak4_effective_area_2002 = ak4_catchment_2002['AREA'] * ak4_fraction
ak4_2002_ru = ((ak4_catchment_2002['RU'].isel(SECTOR=0) * ak4_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
ak4_2002_ru = ak4_2002_ru.to_array().to_numpy().T

ak4_effective_area_2003 = ak4_catchment_2003['AREA'] * ak4_fraction
ak4_2003_ru = ((ak4_catchment_2003['RU'].isel(SECTOR=0) * ak4_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
ak4_2003_ru = ak4_2003_ru.to_array().to_numpy().T

ak4_effective_area_2004 = ak4_catchment_2004['AREA'] * ak4_fraction
ak4_2004_ru = ((ak4_catchment_2004['RU'].isel(SECTOR=0) * ak4_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
ak4_2004_ru = ak4_2004_ru.to_array().to_numpy().T

ak4_effective_area_2005 = ak4_catchment_2005['AREA'] * ak4_fraction
ak4_2005_ru = ((ak4_catchment_2005['RU'].isel(SECTOR=0) * ak4_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
ak4_2005_ru = ak4_2005_ru.to_array().to_numpy().T

ak4_effective_area_2006 = ak4_catchment_2006['AREA'] * ak4_fraction
ak4_2006_ru = ((ak4_catchment_2006['RU'].isel(SECTOR=0) * ak4_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
ak4_2006_ru = ak4_2006_ru.to_array().to_numpy().T

ak4_effective_area_2007 = ak4_catchment_2007['AREA'] * ak4_fraction
ak4_2007_ru = ((ak4_catchment_2007['RU'].isel(SECTOR=0) * ak4_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
ak4_2007_ru = ak4_2007_ru.to_array().to_numpy().T

ak4_effective_area_2008 = ak4_catchment_2008['AREA'] * ak4_fraction
ak4_2008_ru = ((ak4_catchment_2008['RU'].isel(SECTOR=0) * ak4_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
ak4_2008_ru = ak4_2008_ru.to_array().to_numpy().T

ak4_effective_area_2009 = ak4_catchment_2009['AREA'] * ak4_fraction
ak4_2009_ru = ((ak4_catchment_2009['RU'].isel(SECTOR=0) * ak4_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
ak4_2009_ru = ak4_2009_ru.to_array().to_numpy().T

ak4_effective_area_2010 = ak4_catchment_2010['AREA'] * ak4_fraction
ak4_2010_ru = ((ak4_catchment_2010['RU'].isel(SECTOR=0) * ak4_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
ak4_2010_ru = ak4_2010_ru.to_array().to_numpy().T

ak4_effective_area_2011 = ak4_catchment_2011['AREA'] * ak4_fraction
ak4_2011_ru = ((ak4_catchment_2011['RU'].isel(SECTOR=0) * ak4_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
ak4_2011_ru = ak4_2011_ru.to_array().to_numpy().T

ak4_effective_area_2012 = ak4_catchment_2012['AREA'] * ak4_fraction
ak4_2012_ru = ((ak4_catchment_2012['RU'].isel(SECTOR=0) * ak4_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
ak4_2012_ru = ak4_2012_ru.to_array().to_numpy().T

ak4_effective_area_2013 = ak4_catchment_2013['AREA'] * ak4_fraction
ak4_2013_ru = ((ak4_catchment_2013['RU'].isel(SECTOR=0) * ak4_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
ak4_2013_ru = ak4_2013_ru.to_array().to_numpy().T

ak4_effective_area_2014 = ak4_catchment_2014['AREA'] * ak4_fraction
ak4_2014_ru = ((ak4_catchment_2014['RU'].isel(SECTOR=0) * ak4_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
ak4_2014_ru = ak4_2014_ru.to_array().to_numpy().T

ak4_effective_area_2015 = ak4_catchment_2015['AREA'] * ak4_fraction
ak4_2015_ru = ((ak4_catchment_2015['RU'].isel(SECTOR=0) * ak4_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
ak4_2015_ru = ak4_2015_ru.to_array().to_numpy().T

ak4_effective_area_2016 = ak4_catchment_2016['AREA'] * ak4_fraction
ak4_2016_ru = ((ak4_catchment_2016['RU'].isel(SECTOR=0) * ak4_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
ak4_2016_ru = ak4_2016_ru.to_array().to_numpy().T

ak4_effective_area_2017 = ak4_catchment_2017['AREA'] * ak4_fraction
ak4_2017_ru = ((ak4_catchment_2017['RU'].isel(SECTOR=0) * ak4_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
ak4_2017_ru = ak4_2017_ru.to_array().to_numpy().T

ak4_effective_area_2018 = ak4_catchment_2018['AREA'] * ak4_fraction
ak4_2018_ru = ((ak4_catchment_2018['RU'].isel(SECTOR=0) * ak4_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
ak4_2018_ru = ak4_2018_ru.to_array().to_numpy().T

ak4_effective_area_2019 = ak4_catchment_2019['AREA'] * ak4_fraction
ak4_2019_ru = ((ak4_catchment_2019['RU'].isel(SECTOR=0) * ak4_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
ak4_2019_ru = ak4_2019_ru.to_array().to_numpy().T

ak4_effective_area_2020 = ak4_catchment_2020['AREA'] * ak4_fraction
ak4_2020_ru = ((ak4_catchment_2020['RU'].isel(SECTOR=0) * ak4_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
ak4_2020_ru = ak4_2020_ru.to_array().to_numpy().T

ak4_effective_area_2021 = ak4_catchment_2021['AREA'] * ak4_fraction
ak4_2021_ru = ((ak4_catchment_2021['RU'].isel(SECTOR=0) * ak4_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
ak4_2021_ru = ak4_2021_ru.to_array().to_numpy().T

ak4_effective_area_2022 = ak4_catchment_2022['AREA'] * ak4_fraction
ak4_2022_ru = ((ak4_catchment_2022['RU'].isel(SECTOR=0) * ak4_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
ak4_2022_ru = ak4_2022_ru.to_array().to_numpy().T

ak4_effective_area_2023 = ak4_catchment_2023['AREA'] * ak4_fraction
ak4_2023_ru = ((ak4_catchment_2023['RU'].isel(SECTOR=0) * ak4_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
ak4_2023_ru = ak4_2023_ru.to_array().to_numpy().T

ak4_effective_area_2024 = ak4_catchment_2024['AREA'] * ak4_fraction
ak4_2024_ru = ((ak4_catchment_2024['RU'].isel(SECTOR=0) * ak4_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
ak4_2024_ru = ak4_2024_ru.to_array().to_numpy().T

# Minturn catchment area-weighted mean runoff = meltwater + rainfall
# Use Sector 0 for runoff
minturn_effective_area_2000 = minturn_catchment_2000['AREA'] * minturn_fraction
minturn_2000_ru = ((minturn_catchment_2000['RU'].isel(SECTOR=0) * minturn_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
minturn_2000_ru = minturn_2000_ru.to_array().to_numpy().T

minturn_effective_area_2001 = minturn_catchment_2001['AREA'] * minturn_fraction
minturn_2001_ru = ((minturn_catchment_2001['RU'].isel(SECTOR=0) * minturn_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
minturn_2001_ru = minturn_2001_ru.to_array().to_numpy().T

minturn_effective_area_2002 = minturn_catchment_2002['AREA'] * minturn_fraction
minturn_2002_ru = ((minturn_catchment_2002['RU'].isel(SECTOR=0) * minturn_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
minturn_2002_ru = minturn_2002_ru.to_array().to_numpy().T

minturn_effective_area_2003 = minturn_catchment_2003['AREA'] * minturn_fraction
minturn_2003_ru = ((minturn_catchment_2003['RU'].isel(SECTOR=0) * minturn_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
minturn_2003_ru = minturn_2003_ru.to_array().to_numpy().T

minturn_effective_area_2004 = minturn_catchment_2004['AREA'] * minturn_fraction
minturn_2004_ru = ((minturn_catchment_2004['RU'].isel(SECTOR=0) * minturn_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
minturn_2004_ru = minturn_2004_ru.to_array().to_numpy().T

minturn_effective_area_2005 = minturn_catchment_2005['AREA'] * minturn_fraction
minturn_2005_ru = ((minturn_catchment_2005['RU'].isel(SECTOR=0) * minturn_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
minturn_2005_ru = minturn_2005_ru.to_array().to_numpy().T

minturn_effective_area_2006 = minturn_catchment_2006['AREA'] * minturn_fraction
minturn_2006_ru = ((minturn_catchment_2006['RU'].isel(SECTOR=0) * minturn_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
minturn_2006_ru = minturn_2006_ru.to_array().to_numpy().T

minturn_effective_area_2007 = minturn_catchment_2007['AREA'] * minturn_fraction
minturn_2007_ru = ((minturn_catchment_2007['RU'].isel(SECTOR=0) * minturn_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
minturn_2007_ru = minturn_2007_ru.to_array().to_numpy().T

minturn_effective_area_2008 = minturn_catchment_2008['AREA'] * minturn_fraction
minturn_2008_ru = ((minturn_catchment_2008['RU'].isel(SECTOR=0) * minturn_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
minturn_2008_ru = minturn_2008_ru.to_array().to_numpy().T

minturn_effective_area_2009 = minturn_catchment_2009['AREA'] * minturn_fraction
minturn_2009_ru = ((minturn_catchment_2009['RU'].isel(SECTOR=0) * minturn_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
minturn_2009_ru = minturn_2009_ru.to_array().to_numpy().T

minturn_effective_area_2010 = minturn_catchment_2010['AREA'] * minturn_fraction
minturn_2010_ru = ((minturn_catchment_2010['RU'].isel(SECTOR=0) * minturn_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
minturn_2010_ru = minturn_2010_ru.to_array().to_numpy().T

minturn_effective_area_2011 = minturn_catchment_2011['AREA'] * minturn_fraction
minturn_2011_ru = ((minturn_catchment_2011['RU'].isel(SECTOR=0) * minturn_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
minturn_2011_ru = minturn_2011_ru.to_array().to_numpy().T

minturn_effective_area_2012 = minturn_catchment_2012['AREA'] * minturn_fraction
minturn_2012_ru = ((minturn_catchment_2012['RU'].isel(SECTOR=0) * minturn_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
minturn_2012_ru = minturn_2012_ru.to_array().to_numpy().T

minturn_effective_area_2013 = minturn_catchment_2013['AREA'] * minturn_fraction
minturn_2013_ru = ((minturn_catchment_2013['RU'].isel(SECTOR=0) * minturn_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
minturn_2013_ru = minturn_2013_ru.to_array().to_numpy().T

minturn_effective_area_2014 = minturn_catchment_2014['AREA'] * minturn_fraction
minturn_2014_ru = ((minturn_catchment_2014['RU'].isel(SECTOR=0) * minturn_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
minturn_2014_ru = minturn_2014_ru.to_array().to_numpy().T

minturn_effective_area_2015 = minturn_catchment_2015['AREA'] * minturn_fraction
minturn_2015_ru = ((minturn_catchment_2015['RU'].isel(SECTOR=0) * minturn_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
minturn_2015_ru = minturn_2015_ru.to_array().to_numpy().T

minturn_effective_area_2016 = minturn_catchment_2016['AREA'] * minturn_fraction
minturn_2016_ru = ((minturn_catchment_2016['RU'].isel(SECTOR=0) * minturn_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
minturn_2016_ru = minturn_2016_ru.to_array().to_numpy().T

minturn_effective_area_2017 = minturn_catchment_2017['AREA'] * minturn_fraction
minturn_2017_ru = ((minturn_catchment_2017['RU'].isel(SECTOR=0) * minturn_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
minturn_2017_ru = minturn_2017_ru.to_array().to_numpy().T

minturn_effective_area_2018 = minturn_catchment_2018['AREA'] * minturn_fraction
minturn_2018_ru = ((minturn_catchment_2018['RU'].isel(SECTOR=0) * minturn_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
minturn_2018_ru = minturn_2018_ru.to_array().to_numpy().T

minturn_effective_area_2019 = minturn_catchment_2019['AREA'] * minturn_fraction
minturn_2019_ru = ((minturn_catchment_2019['RU'].isel(SECTOR=0) * minturn_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
minturn_2019_ru = minturn_2019_ru.to_array().to_numpy().T

minturn_effective_area_2020 = minturn_catchment_2020['AREA'] * minturn_fraction
minturn_2020_ru = ((minturn_catchment_2020['RU'].isel(SECTOR=0) * minturn_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
minturn_2020_ru = minturn_2020_ru.to_array().to_numpy().T

minturn_effective_area_2021 = minturn_catchment_2021['AREA'] * minturn_fraction
minturn_2021_ru = ((minturn_catchment_2021['RU'].isel(SECTOR=0) * minturn_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
minturn_2021_ru = minturn_2021_ru.to_array().to_numpy().T

minturn_effective_area_2022 = minturn_catchment_2022['AREA'] * minturn_fraction
minturn_2022_ru = ((minturn_catchment_2022['RU'].isel(SECTOR=0) * minturn_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
minturn_2022_ru = minturn_2022_ru.to_array().to_numpy().T

minturn_effective_area_2023 = minturn_catchment_2023['AREA'] * minturn_fraction
minturn_2023_ru = ((minturn_catchment_2023['RU'].isel(SECTOR=0) * minturn_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
minturn_2023_ru = minturn_2023_ru.to_array().to_numpy().T

minturn_effective_area_2024 = minturn_catchment_2024['AREA'] * minturn_fraction
minturn_2024_ru = ((minturn_catchment_2024['RU'].isel(SECTOR=0) * minturn_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
minturn_2024_ru = minturn_2024_ru.to_array().to_numpy().T

# North catchment area-weighted mean runoff = meltwater + rainfall
# Use Sector 0 for runoff
north_effective_area_2000 = north_catchment_2000['AREA'] * north_fraction
north_2000_ru = ((north_catchment_2000['RU'].isel(SECTOR=0) * north_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
north_2000_ru = north_2000_ru.to_array().to_numpy().T

north_effective_area_2001 = north_catchment_2001['AREA'] * north_fraction
north_2001_ru = ((north_catchment_2001['RU'].isel(SECTOR=0) * north_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
north_2001_ru = north_2001_ru.to_array().to_numpy().T

north_effective_area_2002 = north_catchment_2002['AREA'] * north_fraction
north_2002_ru = ((north_catchment_2002['RU'].isel(SECTOR=0) * north_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
north_2002_ru = north_2002_ru.to_array().to_numpy().T

north_effective_area_2003 = north_catchment_2003['AREA'] * north_fraction
north_2003_ru = ((north_catchment_2003['RU'].isel(SECTOR=0) * north_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
north_2003_ru = north_2003_ru.to_array().to_numpy().T

north_effective_area_2004 = north_catchment_2004['AREA'] * north_fraction
north_2004_ru = ((north_catchment_2004['RU'].isel(SECTOR=0) * north_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
north_2004_ru = north_2004_ru.to_array().to_numpy().T

north_effective_area_2005 = north_catchment_2005['AREA'] * north_fraction
north_2005_ru = ((north_catchment_2005['RU'].isel(SECTOR=0) * north_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
north_2005_ru = north_2005_ru.to_array().to_numpy().T

north_effective_area_2006 = north_catchment_2006['AREA'] * north_fraction
north_2006_ru = ((north_catchment_2006['RU'].isel(SECTOR=0) * north_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
north_2006_ru = north_2006_ru.to_array().to_numpy().T

north_effective_area_2007 = north_catchment_2007['AREA'] * north_fraction
north_2007_ru = ((north_catchment_2007['RU'].isel(SECTOR=0) * north_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
north_2007_ru = north_2007_ru.to_array().to_numpy().T

north_effective_area_2008 = north_catchment_2008['AREA'] * north_fraction
north_2008_ru = ((north_catchment_2008['RU'].isel(SECTOR=0) * north_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
north_2008_ru = north_2008_ru.to_array().to_numpy().T

north_effective_area_2009 = north_catchment_2009['AREA'] * north_fraction
north_2009_ru = ((north_catchment_2009['RU'].isel(SECTOR=0) * north_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
north_2009_ru = north_2009_ru.to_array().to_numpy().T

north_effective_area_2010 = north_catchment_2010['AREA'] * north_fraction
north_2010_ru = ((north_catchment_2010['RU'].isel(SECTOR=0) * north_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
north_2010_ru = north_2010_ru.to_array().to_numpy().T

north_effective_area_2011 = north_catchment_2011['AREA'] * north_fraction
north_2011_ru = ((north_catchment_2011['RU'].isel(SECTOR=0) * north_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
north_2011_ru = north_2011_ru.to_array().to_numpy().T

north_effective_area_2012 = north_catchment_2012['AREA'] * north_fraction
north_2012_ru = ((north_catchment_2012['RU'].isel(SECTOR=0) * north_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
north_2012_ru = north_2012_ru.to_array().to_numpy().T

north_effective_area_2013 = north_catchment_2013['AREA'] * north_fraction
north_2013_ru = ((north_catchment_2013['RU'].isel(SECTOR=0) * north_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
north_2013_ru = north_2013_ru.to_array().to_numpy().T

north_effective_area_2014 = north_catchment_2014['AREA'] * north_fraction
north_2014_ru = ((north_catchment_2014['RU'].isel(SECTOR=0) * north_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
north_2014_ru = north_2014_ru.to_array().to_numpy().T

north_effective_area_2015 = north_catchment_2015['AREA'] * north_fraction
north_2015_ru = ((north_catchment_2015['RU'].isel(SECTOR=0) * north_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
north_2015_ru = north_2015_ru.to_array().to_numpy().T

north_effective_area_2016 = north_catchment_2016['AREA'] * north_fraction
north_2016_ru = ((north_catchment_2016['RU'].isel(SECTOR=0) * north_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
north_2016_ru = north_2016_ru.to_array().to_numpy().T

north_effective_area_2017 = north_catchment_2017['AREA'] * north_fraction
north_2017_ru = ((north_catchment_2017['RU'].isel(SECTOR=0) * north_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
north_2017_ru = north_2017_ru.to_array().to_numpy().T

north_effective_area_2018 = north_catchment_2018['AREA'] * north_fraction
north_2018_ru = ((north_catchment_2018['RU'].isel(SECTOR=0) * north_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
north_2018_ru = north_2018_ru.to_array().to_numpy().T

north_effective_area_2019 = north_catchment_2019['AREA'] * north_fraction
north_2019_ru = ((north_catchment_2019['RU'].isel(SECTOR=0) * north_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
north_2019_ru = north_2019_ru.to_array().to_numpy().T

north_effective_area_2020 = north_catchment_2020['AREA'] * north_fraction
north_2020_ru = ((north_catchment_2020['RU'].isel(SECTOR=0) * north_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
north_2020_ru = north_2020_ru.to_array().to_numpy().T

north_effective_area_2021 = north_catchment_2021['AREA'] * north_fraction
north_2021_ru = ((north_catchment_2021['RU'].isel(SECTOR=0) * north_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
north_2021_ru = north_2021_ru.to_array().to_numpy().T

north_effective_area_2022 = north_catchment_2022['AREA'] * north_fraction
north_2022_ru = ((north_catchment_2022['RU'].isel(SECTOR=0) * north_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
north_2022_ru = north_2022_ru.to_array().to_numpy().T

north_effective_area_2023 = north_catchment_2023['AREA'] * north_fraction
north_2023_ru = ((north_catchment_2023['RU'].isel(SECTOR=0) * north_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
north_2023_ru = north_2023_ru.to_array().to_numpy().T

north_effective_area_2024 = north_catchment_2024['AREA'] * north_fraction
north_2024_ru = ((north_catchment_2024['RU'].isel(SECTOR=0) * north_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
north_2024_ru = north_2024_ru.to_array().to_numpy().T

# Rio Behar catchment area-weighted mean rainfall
rb_2000_rf = ((rb_catchment_2000['RF'] * rb_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
rb_2000_rf = rb_2000_rf.to_array().to_numpy().T

rb_2001_rf = ((rb_catchment_2001['RF'] * rb_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
rb_2001_rf = rb_2001_rf.to_array().to_numpy().T

rb_2002_rf = ((rb_catchment_2002['RF'] * rb_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
rb_2002_rf = rb_2002_rf.to_array().to_numpy().T

rb_2003_rf = ((rb_catchment_2003['RF'] * rb_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
rb_2003_rf = rb_2003_rf.to_array().to_numpy().T

rb_2004_rf = ((rb_catchment_2004['RF'] * rb_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
rb_2004_rf = rb_2004_rf.to_array().to_numpy().T

rb_2005_rf = ((rb_catchment_2005['RF'] * rb_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
rb_2005_rf = rb_2005_rf.to_array().to_numpy().T

rb_2006_rf = ((rb_catchment_2006['RF'] * rb_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
rb_2006_rf = rb_2006_rf.to_array().to_numpy().T

rb_2007_rf = ((rb_catchment_2007['RF'] * rb_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
rb_2007_rf = rb_2007_rf.to_array().to_numpy().T

rb_2008_rf = ((rb_catchment_2008['RF'] * rb_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
rb_2008_rf = rb_2008_rf.to_array().to_numpy().T

rb_2009_rf = ((rb_catchment_2009['RF'] * rb_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
rb_2009_rf = rb_2009_rf.to_array().to_numpy().T

rb_2010_rf = ((rb_catchment_2010['RF'] * rb_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
rb_2010_rf = rb_2010_rf.to_array().to_numpy().T

rb_2011_rf = ((rb_catchment_2011['RF'] * rb_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
rb_2011_rf = rb_2011_rf.to_array().to_numpy().T

rb_2012_rf = ((rb_catchment_2012['RF'] * rb_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
rb_2012_rf = rb_2012_rf.to_array().to_numpy().T

rb_2013_rf = ((rb_catchment_2013['RF'] * rb_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
rb_2013_rf = rb_2013_rf.to_array().to_numpy().T

rb_2014_rf = ((rb_catchment_2014['RF'] * rb_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
rb_2014_rf = rb_2014_rf.to_array().to_numpy().T

rb_2015_rf = ((rb_catchment_2015['RF'] * rb_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
rb_2015_rf = rb_2015_rf.to_array().to_numpy().T

rb_2016_rf = ((rb_catchment_2016['RF'] * rb_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
rb_2016_rf = rb_2016_rf.to_array().to_numpy().T

rb_2017_rf = ((rb_catchment_2017['RF'] * rb_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
rb_2017_rf = rb_2017_rf.to_array().to_numpy().T

rb_2018_rf = ((rb_catchment_2018['RF'] * rb_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
rb_2018_rf = rb_2018_rf.to_array().to_numpy().T

rb_2019_rf = ((rb_catchment_2019['RF'] * rb_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
rb_2019_rf = rb_2019_rf.to_array().to_numpy().T

rb_2020_rf = ((rb_catchment_2020['RF'] * rb_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
rb_2020_rf = rb_2020_rf.to_array().to_numpy().T

rb_2021_rf = ((rb_catchment_2021['RF'] * rb_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
rb_2021_rf = rb_2021_rf.to_array().to_numpy().T

rb_2022_rf = ((rb_catchment_2022['RF'] * rb_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
rb_2022_rf = rb_2022_rf.to_array().to_numpy().T

rb_2023_rf = ((rb_catchment_2023['RF'] * rb_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
rb_2023_rf = rb_2023_rf.to_array().to_numpy().T

rb_2024_rf = ((rb_catchment_2024['RF'] * rb_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / rb_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
rb_2024_rf = rb_2024_rf.to_array().to_numpy().T

# AK4 catchment area-weighted mean rainfall
ak4_2000_rf = ((ak4_catchment_2000['RF'] * ak4_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
ak4_2000_rf = ak4_2000_rf.to_array().to_numpy().T

ak4_2001_rf = ((ak4_catchment_2001['RF'] * ak4_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
ak4_2001_rf = ak4_2001_rf.to_array().to_numpy().T

ak4_2002_rf = ((ak4_catchment_2002['RF'] * ak4_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
ak4_2002_rf = ak4_2002_rf.to_array().to_numpy().T

ak4_2003_rf = ((ak4_catchment_2003['RF'] * ak4_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
ak4_2003_rf = ak4_2003_rf.to_array().to_numpy().T

ak4_2004_rf = ((ak4_catchment_2004['RF'] * ak4_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
ak4_2004_rf = ak4_2004_rf.to_array().to_numpy().T

ak4_2005_rf = ((ak4_catchment_2005['RF'] * ak4_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
ak4_2005_rf = ak4_2005_rf.to_array().to_numpy().T

ak4_2006_rf = ((ak4_catchment_2006['RF'] * ak4_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
ak4_2006_rf = ak4_2006_rf.to_array().to_numpy().T

ak4_2007_rf = ((ak4_catchment_2007['RF'] * ak4_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
ak4_2007_rf = ak4_2007_rf.to_array().to_numpy().T

ak4_2008_rf = ((ak4_catchment_2008['RF'] * ak4_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
ak4_2008_rf = ak4_2008_rf.to_array().to_numpy().T

ak4_2009_rf = ((ak4_catchment_2009['RF'] * ak4_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
ak4_2009_rf = ak4_2009_rf.to_array().to_numpy().T

ak4_2010_rf = ((ak4_catchment_2010['RF'] * ak4_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
ak4_2010_rf = ak4_2010_rf.to_array().to_numpy().T

ak4_2011_rf = ((ak4_catchment_2011['RF'] * ak4_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
ak4_2011_rf = ak4_2011_rf.to_array().to_numpy().T

ak4_2012_rf = ((ak4_catchment_2012['RF'] * ak4_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
ak4_2012_rf = ak4_2012_rf.to_array().to_numpy().T

ak4_2013_rf = ((ak4_catchment_2013['RF'] * ak4_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
ak4_2013_rf = ak4_2013_rf.to_array().to_numpy().T

ak4_2014_rf = ((ak4_catchment_2014['RF'] * ak4_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
ak4_2014_rf = ak4_2014_rf.to_array().to_numpy().T

ak4_2015_rf = ((ak4_catchment_2015['RF'] * ak4_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
ak4_2015_rf = ak4_2015_rf.to_array().to_numpy().T

ak4_2016_rf = ((ak4_catchment_2016['RF'] * ak4_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
ak4_2016_rf = ak4_2016_rf.to_array().to_numpy().T

ak4_2017_rf = ((ak4_catchment_2017['RF'] * ak4_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
ak4_2017_rf = ak4_2017_rf.to_array().to_numpy().T

ak4_2018_rf = ((ak4_catchment_2018['RF'] * ak4_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
ak4_2018_rf = ak4_2018_rf.to_array().to_numpy().T

ak4_2019_rf = ((ak4_catchment_2019['RF'] * ak4_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
ak4_2019_rf = ak4_2019_rf.to_array().to_numpy().T

ak4_2020_rf = ((ak4_catchment_2020['RF'] * ak4_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
ak4_2020_rf = ak4_2020_rf.to_array().to_numpy().T

ak4_2021_rf = ((ak4_catchment_2021['RF'] * ak4_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
ak4_2021_rf = ak4_2021_rf.to_array().to_numpy().T

ak4_2022_rf = ((ak4_catchment_2022['RF'] * ak4_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
ak4_2022_rf = ak4_2022_rf.to_array().to_numpy().T

ak4_2023_rf = ((ak4_catchment_2023['RF'] * ak4_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
ak4_2023_rf = ak4_2023_rf.to_array().to_numpy().T

ak4_2024_rf = ((ak4_catchment_2024['RF'] * ak4_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / ak4_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
ak4_2024_rf = ak4_2024_rf.to_array().to_numpy().T

# Minturn catchment area-weighted mean rainfall
minturn_2000_rf = ((minturn_catchment_2000['RF'] * minturn_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
minturn_2000_rf = minturn_2000_rf.to_array().to_numpy().T

minturn_2001_rf = ((minturn_catchment_2001['RF'] * minturn_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
minturn_2001_rf = minturn_2001_rf.to_array().to_numpy().T

minturn_2002_rf = ((minturn_catchment_2002['RF'] * minturn_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
minturn_2002_rf = minturn_2002_rf.to_array().to_numpy().T

minturn_2003_rf = ((minturn_catchment_2003['RF'] * minturn_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
minturn_2003_rf = minturn_2003_rf.to_array().to_numpy().T

minturn_2004_rf = ((minturn_catchment_2004['RF'] * minturn_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
minturn_2004_rf = minturn_2004_rf.to_array().to_numpy().T

minturn_2005_rf = ((minturn_catchment_2005['RF'] * minturn_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
minturn_2005_rf = minturn_2005_rf.to_array().to_numpy().T

minturn_2006_rf = ((minturn_catchment_2006['RF'] * minturn_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
minturn_2006_rf = minturn_2006_rf.to_array().to_numpy().T

minturn_2007_rf = ((minturn_catchment_2007['RF'] * minturn_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
minturn_2007_rf = minturn_2007_rf.to_array().to_numpy().T

minturn_2008_rf = ((minturn_catchment_2008['RF'] * minturn_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
minturn_2008_rf = minturn_2008_rf.to_array().to_numpy().T

minturn_2009_rf = ((minturn_catchment_2009['RF'] * minturn_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
minturn_2009_rf = minturn_2009_rf.to_array().to_numpy().T

minturn_2010_rf = ((minturn_catchment_2010['RF'] * minturn_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
minturn_2010_rf = minturn_2010_rf.to_array().to_numpy().T

minturn_2011_rf = ((minturn_catchment_2011['RF'] * minturn_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
minturn_2011_rf = minturn_2011_rf.to_array().to_numpy().T

minturn_2012_rf = ((minturn_catchment_2012['RF'] * minturn_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
minturn_2012_rf = minturn_2012_rf.to_array().to_numpy().T

minturn_2013_rf = ((minturn_catchment_2013['RF'] * minturn_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
minturn_2013_rf = minturn_2013_rf.to_array().to_numpy().T

minturn_2014_rf = ((minturn_catchment_2014['RF'] * minturn_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
minturn_2014_rf = minturn_2014_rf.to_array().to_numpy().T

minturn_2015_rf = ((minturn_catchment_2015['RF'] * minturn_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
minturn_2015_rf = minturn_2015_rf.to_array().to_numpy().T

minturn_2016_rf = ((minturn_catchment_2016['RF'] * minturn_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
minturn_2016_rf = minturn_2016_rf.to_array().to_numpy().T

minturn_2017_rf = ((minturn_catchment_2017['RF'] * minturn_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
minturn_2017_rf = minturn_2017_rf.to_array().to_numpy().T

minturn_2018_rf = ((minturn_catchment_2018['RF'] * minturn_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
minturn_2018_rf = minturn_2018_rf.to_array().to_numpy().T

minturn_2019_rf = ((minturn_catchment_2019['RF'] * minturn_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
minturn_2019_rf = minturn_2019_rf.to_array().to_numpy().T

minturn_2020_rf = ((minturn_catchment_2020['RF'] * minturn_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
minturn_2020_rf = minturn_2020_rf.to_array().to_numpy().T

minturn_2021_rf = ((minturn_catchment_2021['RF'] * minturn_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
minturn_2021_rf = minturn_2021_rf.to_array().to_numpy().T

minturn_2022_rf = ((minturn_catchment_2022['RF'] * minturn_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
minturn_2022_rf = minturn_2022_rf.to_array().to_numpy().T

minturn_2023_rf = ((minturn_catchment_2023['RF'] * minturn_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
minturn_2023_rf = minturn_2023_rf.to_array().to_numpy().T

minturn_2024_rf = ((minturn_catchment_2024['RF'] * minturn_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / minturn_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
minturn_2024_rf = minturn_2024_rf.to_array().to_numpy().T

# North catchment area-weighted mean rainfall
north_2000_rf = ((north_catchment_2000['RF'] * north_effective_area_2000).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2000.sum(dim=('y', 'x'), skipna=True))
north_2000_rf = north_2000_rf.to_array().to_numpy().T

north_2001_rf = ((north_catchment_2001['RF'] * north_effective_area_2001).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2001.sum(dim=('y', 'x'), skipna=True))
north_2001_rf = north_2001_rf.to_array().to_numpy().T

north_2002_rf = ((north_catchment_2002['RF'] * north_effective_area_2002).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2002.sum(dim=('y', 'x'), skipna=True))
north_2002_rf = north_2002_rf.to_array().to_numpy().T

north_2003_rf = ((north_catchment_2003['RF'] * north_effective_area_2003).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2003.sum(dim=('y', 'x'), skipna=True))
north_2003_rf = north_2003_rf.to_array().to_numpy().T

north_2004_rf = ((north_catchment_2004['RF'] * north_effective_area_2004).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2004.sum(dim=('y', 'x'), skipna=True))
north_2004_rf = north_2004_rf.to_array().to_numpy().T

north_2005_rf = ((north_catchment_2005['RF'] * north_effective_area_2005).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2005.sum(dim=('y', 'x'), skipna=True))
north_2005_rf = north_2005_rf.to_array().to_numpy().T

north_2006_rf = ((north_catchment_2006['RF'] * north_effective_area_2006).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2006.sum(dim=('y', 'x'), skipna=True))
north_2006_rf = north_2006_rf.to_array().to_numpy().T

north_2007_rf = ((north_catchment_2007['RF'] * north_effective_area_2007).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2007.sum(dim=('y', 'x'), skipna=True))
north_2007_rf = north_2007_rf.to_array().to_numpy().T

north_2008_rf = ((north_catchment_2008['RF'] * north_effective_area_2008).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2008.sum(dim=('y', 'x'), skipna=True))
north_2008_rf = north_2008_rf.to_array().to_numpy().T

north_2009_rf = ((north_catchment_2009['RF'] * north_effective_area_2009).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2009.sum(dim=('y', 'x'), skipna=True))
north_2009_rf = north_2009_rf.to_array().to_numpy().T

north_2010_rf = ((north_catchment_2010['RF'] * north_effective_area_2010).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2010.sum(dim=('y', 'x'), skipna=True))
north_2010_rf = north_2010_rf.to_array().to_numpy().T

north_2011_rf = ((north_catchment_2011['RF'] * north_effective_area_2011).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2011.sum(dim=('y', 'x'), skipna=True))
north_2011_rf = north_2011_rf.to_array().to_numpy().T

north_2012_rf = ((north_catchment_2012['RF'] * north_effective_area_2012).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2012.sum(dim=('y', 'x'), skipna=True))
north_2012_rf = north_2012_rf.to_array().to_numpy().T

north_2013_rf = ((north_catchment_2013['RF'] * north_effective_area_2013).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2013.sum(dim=('y', 'x'), skipna=True))
north_2013_rf = north_2013_rf.to_array().to_numpy().T

north_2014_rf = ((north_catchment_2014['RF'] * north_effective_area_2014).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2014.sum(dim=('y', 'x'), skipna=True))
north_2014_rf = north_2014_rf.to_array().to_numpy().T

north_2015_rf = ((north_catchment_2015['RF'] * north_effective_area_2015).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2015.sum(dim=('y', 'x'), skipna=True))
north_2015_rf = north_2015_rf.to_array().to_numpy().T

north_2016_rf = ((north_catchment_2016['RF'] * north_effective_area_2016).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2016.sum(dim=('y', 'x'), skipna=True))
north_2016_rf = north_2016_rf.to_array().to_numpy().T

north_2017_rf = ((north_catchment_2017['RF'] * north_effective_area_2017).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2017.sum(dim=('y', 'x'), skipna=True))
north_2017_rf = north_2017_rf.to_array().to_numpy().T

north_2018_rf = ((north_catchment_2018['RF'] * north_effective_area_2018).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2018.sum(dim=('y', 'x'), skipna=True))
north_2018_rf = north_2018_rf.to_array().to_numpy().T

north_2019_rf = ((north_catchment_2019['RF'] * north_effective_area_2019).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2019.sum(dim=('y', 'x'), skipna=True))
north_2019_rf = north_2019_rf.to_array().to_numpy().T

north_2020_rf = ((north_catchment_2020['RF'] * north_effective_area_2020).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2020.sum(dim=('y', 'x'), skipna=True))
north_2020_rf = north_2020_rf.to_array().to_numpy().T

north_2021_rf = ((north_catchment_2021['RF'] * north_effective_area_2021).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2021.sum(dim=('y', 'x'), skipna=True))
north_2021_rf = north_2021_rf.to_array().to_numpy().T

north_2022_rf = ((north_catchment_2022['RF'] * north_effective_area_2022).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2022.sum(dim=('y', 'x'), skipna=True))
north_2022_rf = north_2022_rf.to_array().to_numpy().T

north_2023_rf = ((north_catchment_2023['RF'] * north_effective_area_2023).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2023.sum(dim=('y', 'x'), skipna=True))
north_2023_rf = north_2023_rf.to_array().to_numpy().T

north_2024_rf = ((north_catchment_2024['RF'] * north_effective_area_2024).sum(dim=('y', 'x'), skipna=True) / north_effective_area_2024.sum(dim=('y', 'x'), skipna=True))
north_2024_rf = north_2024_rf.to_array().to_numpy().T

# Rio Behar catchment area-weighted mean meltwater runoff = runoff - rainfall
rb_2000_mru = rb_2000_ru - rb_2000_rf
rb_2001_mru = rb_2001_ru - rb_2001_rf
rb_2002_mru = rb_2002_ru - rb_2002_rf
rb_2003_mru = rb_2003_ru - rb_2003_rf
rb_2004_mru = rb_2004_ru - rb_2004_rf
rb_2005_mru = rb_2005_ru - rb_2005_rf
rb_2006_mru = rb_2006_ru - rb_2006_rf
rb_2007_mru = rb_2007_ru - rb_2007_rf
rb_2008_mru = rb_2008_ru - rb_2008_rf
rb_2009_mru = rb_2009_ru - rb_2009_rf
rb_2010_mru = rb_2010_ru - rb_2010_rf
rb_2011_mru = rb_2011_ru - rb_2011_rf
rb_2012_mru = rb_2012_ru - rb_2012_rf
rb_2013_mru = rb_2013_ru - rb_2013_rf
rb_2014_mru = rb_2014_ru - rb_2014_rf
rb_2015_mru = rb_2015_ru - rb_2015_rf
rb_2016_mru = rb_2016_ru - rb_2016_rf
rb_2017_mru = rb_2017_ru - rb_2017_rf
rb_2018_mru = rb_2018_ru - rb_2018_rf
rb_2019_mru = rb_2019_ru - rb_2019_rf
rb_2020_mru = rb_2020_ru - rb_2020_rf
rb_2021_mru = rb_2021_ru - rb_2021_rf
rb_2022_mru = rb_2022_ru - rb_2022_rf
rb_2023_mru = rb_2023_ru - rb_2023_rf
rb_2024_mru = rb_2024_ru - rb_2024_rf

# AK4 catchment area-weighted mean meltwater runoff = runoff - rainfall
ak4_2000_mru = ak4_2000_ru - ak4_2000_rf
ak4_2001_mru = ak4_2001_ru - ak4_2001_rf
ak4_2002_mru = ak4_2002_ru - ak4_2002_rf
ak4_2003_mru = ak4_2003_ru - ak4_2003_rf
ak4_2004_mru = ak4_2004_ru - ak4_2004_rf
ak4_2005_mru = ak4_2005_ru - ak4_2005_rf
ak4_2006_mru = ak4_2006_ru - ak4_2006_rf
ak4_2007_mru = ak4_2007_ru - ak4_2007_rf
ak4_2008_mru = ak4_2008_ru - ak4_2008_rf
ak4_2009_mru = ak4_2009_ru - ak4_2009_rf
ak4_2010_mru = ak4_2010_ru - ak4_2010_rf
ak4_2011_mru = ak4_2011_ru - ak4_2011_rf
ak4_2012_mru = ak4_2012_ru - ak4_2012_rf
ak4_2013_mru = ak4_2013_ru - ak4_2013_rf
ak4_2014_mru = ak4_2014_ru - ak4_2014_rf
ak4_2015_mru = ak4_2015_ru - ak4_2015_rf
ak4_2016_mru = ak4_2016_ru - ak4_2016_rf
ak4_2017_mru = ak4_2017_ru - ak4_2017_rf
ak4_2018_mru = ak4_2018_ru - ak4_2018_rf
ak4_2019_mru = ak4_2019_ru - ak4_2019_rf
ak4_2020_mru = ak4_2020_ru - ak4_2020_rf
ak4_2021_mru = ak4_2021_ru - ak4_2021_rf
ak4_2022_mru = ak4_2022_ru - ak4_2022_rf
ak4_2023_mru = ak4_2023_ru - ak4_2023_rf
ak4_2024_mru = ak4_2024_ru - ak4_2024_rf

# Minturn catchment area-weighted mean meltwater runoff = runoff - rainfall
minturn_2000_mru = minturn_2000_ru - minturn_2000_rf
minturn_2001_mru = minturn_2001_ru - minturn_2001_rf
minturn_2002_mru = minturn_2002_ru - minturn_2002_rf
minturn_2003_mru = minturn_2003_ru - minturn_2003_rf
minturn_2004_mru = minturn_2004_ru - minturn_2004_rf
minturn_2005_mru = minturn_2005_ru - minturn_2005_rf
minturn_2006_mru = minturn_2006_ru - minturn_2006_rf
minturn_2007_mru = minturn_2007_ru - minturn_2007_rf
minturn_2008_mru = minturn_2008_ru - minturn_2008_rf
minturn_2009_mru = minturn_2009_ru - minturn_2009_rf
minturn_2010_mru = minturn_2010_ru - minturn_2010_rf
minturn_2011_mru = minturn_2011_ru - minturn_2011_rf
minturn_2012_mru = minturn_2012_ru - minturn_2012_rf
minturn_2013_mru = minturn_2013_ru - minturn_2013_rf
minturn_2014_mru = minturn_2014_ru - minturn_2014_rf
minturn_2015_mru = minturn_2015_ru - minturn_2015_rf
minturn_2016_mru = minturn_2016_ru - minturn_2016_rf
minturn_2017_mru = minturn_2017_ru - minturn_2017_rf
minturn_2018_mru = minturn_2018_ru - minturn_2018_rf
minturn_2019_mru = minturn_2019_ru - minturn_2019_rf
minturn_2020_mru = minturn_2020_ru - minturn_2020_rf
minturn_2021_mru = minturn_2021_ru - minturn_2021_rf
minturn_2022_mru = minturn_2022_ru - minturn_2022_rf
minturn_2023_mru = minturn_2023_ru - minturn_2023_rf
minturn_2024_mru = minturn_2024_ru - minturn_2024_rf

# North catchment area-weighted mean meltwater runoff = runoff - rainfall
north_2000_mru = north_2000_ru - north_2000_rf
north_2001_mru = north_2001_ru - north_2001_rf
north_2002_mru = north_2002_ru - north_2002_rf
north_2003_mru = north_2003_ru - north_2003_rf
north_2004_mru = north_2004_ru - north_2004_rf
north_2005_mru = north_2005_ru - north_2005_rf
north_2006_mru = north_2006_ru - north_2006_rf
north_2007_mru = north_2007_ru - north_2007_rf
north_2008_mru = north_2008_ru - north_2008_rf
north_2009_mru = north_2009_ru - north_2009_rf
north_2010_mru = north_2010_ru - north_2010_rf
north_2011_mru = north_2011_ru - north_2011_rf
north_2012_mru = north_2012_ru - north_2012_rf
north_2013_mru = north_2013_ru - north_2013_rf
north_2014_mru = north_2014_ru - north_2014_rf
north_2015_mru = north_2015_ru - north_2015_rf
north_2016_mru = north_2016_ru - north_2016_rf
north_2017_mru = north_2017_ru - north_2017_rf
north_2018_mru = north_2018_ru - north_2018_rf
north_2019_mru = north_2019_ru - north_2019_rf
north_2020_mru = north_2020_ru - north_2020_rf
north_2021_mru = north_2021_ru - north_2021_rf
north_2022_mru = north_2022_ru - north_2022_rf
north_2023_mru = north_2023_ru - north_2023_rf
north_2024_mru = north_2024_ru - north_2024_rf

# Function to make arrays 1D before putting into df

def to_1d(var):
    array = np.asarray(var)
    if array.ndim == 1:
        return array
    if array.ndim == 2 and 1 in array.shape:
        return array.reshape(-1)
    return array.ravel()


# Save Rio Behar variables to dataframe
rb_catchment_2000_df = pd.DataFrame({"time": to_1d(rb_2000_time),
                                     "air_temp": to_1d(rb_2000_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2000_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2000_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2000_swd),
                                     "shortwave_up": to_1d(rb_2000_swu),
                                     "longwave_down": to_1d(rb_2000_lwd),
                                     "longwave_up": to_1d(rb_2000_lwu),
                                     "sensible_heat_flux": to_1d(rb_2000_shf),
                                     "latent_heat_flux": to_1d(rb_2000_lhf),
                                     "surface_energy_balance": to_1d(rb_2000_seb),
                                     "meltwater_runoff": to_1d(rb_2000_mru)})

rb_catchment_2001_df = pd.DataFrame({"time": to_1d(rb_2001_time),
                                     "air_temp": to_1d(rb_2001_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2001_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2001_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2001_swd),
                                     "shortwave_up": to_1d(rb_2001_swu),
                                     "longwave_down": to_1d(rb_2001_lwd),
                                     "longwave_up": to_1d(rb_2001_lwu),
                                     "sensible_heat_flux": to_1d(rb_2001_shf),
                                     "latent_heat_flux": to_1d(rb_2001_lhf),
                                     "surface_energy_balance": to_1d(rb_2001_seb),
                                     "meltwater_runoff": to_1d(rb_2001_mru)})

rb_catchment_2002_df = pd.DataFrame({"time": to_1d(rb_2002_time),
                                     "air_temp": to_1d(rb_2002_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2002_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2002_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2002_swd),
                                     "shortwave_up": to_1d(rb_2002_swu),
                                     "longwave_down": to_1d(rb_2002_lwd),
                                     "longwave_up": to_1d(rb_2002_lwu),
                                     "sensible_heat_flux": to_1d(rb_2002_shf),
                                     "latent_heat_flux": to_1d(rb_2002_lhf),
                                     "surface_energy_balance": to_1d(rb_2002_seb),
                                     "meltwater_runoff": to_1d(rb_2002_mru)})

rb_catchment_2003_df = pd.DataFrame({"time": to_1d(rb_2003_time),
                                     "air_temp": to_1d(rb_2003_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2003_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2003_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2003_swd),
                                     "shortwave_up": to_1d(rb_2003_swu),
                                     "longwave_down": to_1d(rb_2003_lwd),
                                     "longwave_up": to_1d(rb_2003_lwu),
                                     "sensible_heat_flux": to_1d(rb_2003_shf),
                                     "latent_heat_flux": to_1d(rb_2003_lhf),
                                     "surface_energy_balance": to_1d(rb_2003_seb),
                                     "meltwater_runoff": to_1d(rb_2003_mru)})

rb_catchment_2004_df = pd.DataFrame({"time": to_1d(rb_2004_time),
                                     "air_temp": to_1d(rb_2004_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2004_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2004_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2004_swd),
                                     "shortwave_up": to_1d(rb_2004_swu),
                                     "longwave_down": to_1d(rb_2004_lwd),
                                     "longwave_up": to_1d(rb_2004_lwu),
                                     "sensible_heat_flux": to_1d(rb_2004_shf),
                                     "latent_heat_flux": to_1d(rb_2004_lhf),
                                     "surface_energy_balance": to_1d(rb_2004_seb),
                                     "meltwater_runoff": to_1d(rb_2004_mru)})

rb_catchment_2005_df = pd.DataFrame({"time": to_1d(rb_2005_time),
                                     "air_temp": to_1d(rb_2005_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2005_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2005_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2005_swd),
                                     "shortwave_up": to_1d(rb_2005_swu),
                                     "longwave_down": to_1d(rb_2005_lwd),
                                     "longwave_up": to_1d(rb_2005_lwu),
                                     "sensible_heat_flux": to_1d(rb_2005_shf),
                                     "latent_heat_flux": to_1d(rb_2005_lhf),
                                     "surface_energy_balance": to_1d(rb_2005_seb),
                                     "meltwater_runoff": to_1d(rb_2005_mru)})

rb_catchment_2006_df = pd.DataFrame({"time": to_1d(rb_2006_time),
                                     "air_temp": to_1d(rb_2006_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2006_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2006_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2006_swd),
                                     "shortwave_up": to_1d(rb_2006_swu),
                                     "longwave_down": to_1d(rb_2006_lwd),
                                     "longwave_up": to_1d(rb_2006_lwu),
                                     "sensible_heat_flux": to_1d(rb_2006_shf),
                                     "latent_heat_flux": to_1d(rb_2006_lhf),
                                     "surface_energy_balance": to_1d(rb_2006_seb),
                                     "meltwater_runoff": to_1d(rb_2006_mru)})

rb_catchment_2007_df = pd.DataFrame({"time": to_1d(rb_2007_time),
                                     "air_temp": to_1d(rb_2007_air_temp[:, 0]),
                                     "ice_temp": to_1d(rb_2007_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2007_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2007_swd),
                                     "shortwave_up": to_1d(rb_2007_swu),
                                     "longwave_down": to_1d(rb_2007_lwd),
                                     "longwave_up": to_1d(rb_2007_lwu),
                                     "sensible_heat_flux": to_1d(rb_2007_shf),
                                     "latent_heat_flux": to_1d(rb_2007_lhf),
                                     "surface_energy_balance": to_1d(rb_2007_seb),
                                     "meltwater_runoff": to_1d(rb_2007_mru)})

rb_catchment_2008_df = pd.DataFrame({"time": to_1d(rb_2008_time),
                                     "air_temp": to_1d(rb_2008_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2008_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2008_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2008_swd),
                                     "shortwave_up": to_1d(rb_2008_swu),
                                     "longwave_down": to_1d(rb_2008_lwd),
                                     "longwave_up": to_1d(rb_2008_lwu),
                                     "sensible_heat_flux": to_1d(rb_2008_shf),
                                     "latent_heat_flux": to_1d(rb_2008_lhf),
                                     "surface_energy_balance": to_1d(rb_2008_seb),
                                     "meltwater_runoff": to_1d(rb_2008_mru)})

rb_catchment_2009_df = pd.DataFrame({"time": to_1d(rb_2009_time),
                                     "air_temp": to_1d(rb_2009_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2009_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2009_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2009_swd),
                                     "shortwave_up": to_1d(rb_2009_swu),
                                     "longwave_down": to_1d(rb_2009_lwd),
                                     "longwave_up": to_1d(rb_2009_lwu),
                                     "sensible_heat_flux": to_1d(rb_2009_shf),
                                     "latent_heat_flux": to_1d(rb_2009_lhf),
                                     "surface_energy_balance": to_1d(rb_2009_seb),
                                     "meltwater_runoff": to_1d(rb_2009_mru)})

rb_catchment_2010_df = pd.DataFrame({"time": to_1d(rb_2010_time),
                                     "air_temp": to_1d(rb_2010_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2010_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2010_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2010_swd),
                                     "shortwave_up": to_1d(rb_2010_swu),
                                     "longwave_down": to_1d(rb_2010_lwd),
                                     "longwave_up": to_1d(rb_2010_lwu),
                                     "sensible_heat_flux": to_1d(rb_2010_shf),
                                     "latent_heat_flux": to_1d(rb_2010_lhf),
                                     "surface_energy_balance": to_1d(rb_2010_seb),
                                     "meltwater_runoff": to_1d(rb_2010_mru)})

rb_catchment_2011_df = pd.DataFrame({"time": to_1d(rb_2011_time),
                                     "air_temp": to_1d(rb_2011_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2011_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2011_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2011_swd),
                                     "shortwave_up": to_1d(rb_2011_swu),
                                     "longwave_down": to_1d(rb_2011_lwd),
                                     "longwave_up": to_1d(rb_2011_lwu),
                                     "sensible_heat_flux": to_1d(rb_2011_shf),
                                     "latent_heat_flux": to_1d(rb_2011_lhf),
                                     "surface_energy_balance": to_1d(rb_2011_seb),
                                     "meltwater_runoff": to_1d(rb_2011_mru)})

rb_catchment_2012_df = pd.DataFrame({"time": to_1d(rb_2012_time),
                                     "air_temp": to_1d(rb_2012_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2012_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2012_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2012_swd),
                                     "shortwave_up": to_1d(rb_2012_swu),
                                     "longwave_down": to_1d(rb_2012_lwd),
                                     "longwave_up": to_1d(rb_2012_lwu),
                                     "sensible_heat_flux": to_1d(rb_2012_shf),
                                     "latent_heat_flux": to_1d(rb_2012_lhf),
                                     "surface_energy_balance": to_1d(rb_2012_seb),
                                     "meltwater_runoff": to_1d(rb_2012_mru)})

rb_catchment_2013_df = pd.DataFrame({"time": to_1d(rb_2013_time),
                                     "air_temp": to_1d(rb_2013_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2013_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2013_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2013_swd),
                                     "shortwave_up": to_1d(rb_2013_swu),
                                     "longwave_down": to_1d(rb_2013_lwd),
                                     "longwave_up": to_1d(rb_2013_lwu),
                                     "sensible_heat_flux": to_1d(rb_2013_shf),
                                     "latent_heat_flux": to_1d(rb_2013_lhf),
                                     "surface_energy_balance": to_1d(rb_2013_seb),
                                     "meltwater_runoff": to_1d(rb_2013_mru)})

rb_catchment_2014_df = pd.DataFrame({"time": to_1d(rb_2014_time),
                                     "air_temp": to_1d(rb_2014_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2014_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2014_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2014_swd),
                                     "shortwave_up": to_1d(rb_2014_swu),
                                     "longwave_down": to_1d(rb_2014_lwd),
                                     "longwave_up": to_1d(rb_2014_lwu),
                                     "sensible_heat_flux": to_1d(rb_2014_shf),
                                     "latent_heat_flux": to_1d(rb_2014_lhf),
                                     "surface_energy_balance": to_1d(rb_2014_seb),
                                     "meltwater_runoff": to_1d(rb_2014_mru)})

rb_catchment_2015_df = pd.DataFrame({"time": to_1d(rb_2015_time),
                                     "air_temp": to_1d(rb_2015_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2015_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2015_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2015_swd),
                                     "shortwave_up": to_1d(rb_2015_swu),
                                     "longwave_down": to_1d(rb_2015_lwd),
                                     "longwave_up": to_1d(rb_2015_lwu),
                                     "sensible_heat_flux": to_1d(rb_2015_shf),
                                     "latent_heat_flux": to_1d(rb_2015_lhf),
                                     "surface_energy_balance": to_1d(rb_2015_seb),
                                     "meltwater_runoff": to_1d(rb_2015_mru)})

rb_catchment_2016_df = pd.DataFrame({"time": to_1d(rb_2016_time),
                                     "air_temp": to_1d(rb_2016_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2016_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2016_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2016_swd),
                                     "shortwave_up": to_1d(rb_2016_swu),
                                     "longwave_down": to_1d(rb_2016_lwd),
                                     "longwave_up": to_1d(rb_2016_lwu),
                                     "sensible_heat_flux": to_1d(rb_2016_shf),
                                     "latent_heat_flux": to_1d(rb_2016_lhf),
                                     "surface_energy_balance": to_1d(rb_2016_seb),
                                     "meltwater_runoff": to_1d(rb_2016_mru)})

rb_catchment_2017_df = pd.DataFrame({"time": to_1d(rb_2017_time),
                                     "air_temp": to_1d(rb_2017_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2017_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2017_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2017_swd),
                                     "shortwave_up": to_1d(rb_2017_swu),
                                     "longwave_down": to_1d(rb_2017_lwd),
                                     "longwave_up": to_1d(rb_2017_lwu),
                                     "sensible_heat_flux": to_1d(rb_2017_shf),
                                     "latent_heat_flux": to_1d(rb_2017_lhf),
                                     "surface_energy_balance": to_1d(rb_2017_seb),
                                     "meltwater_runoff": to_1d(rb_2017_mru)})

rb_catchment_2018_df = pd.DataFrame({"time": to_1d(rb_2018_time),
                                     "air_temp": to_1d(rb_2018_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2018_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2018_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2018_swd),
                                     "shortwave_up": to_1d(rb_2018_swu),
                                     "longwave_down": to_1d(rb_2018_lwd),
                                     "longwave_up": to_1d(rb_2018_lwu),
                                     "sensible_heat_flux": to_1d(rb_2018_shf),
                                     "latent_heat_flux": to_1d(rb_2018_lhf),
                                     "surface_energy_balance": to_1d(rb_2018_seb),
                                     "meltwater_runoff": to_1d(rb_2018_mru)})

rb_catchment_2019_df = pd.DataFrame({"time": to_1d(rb_2019_time),
                                     "air_temp": to_1d(rb_2019_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2019_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2019_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2019_swd),
                                     "shortwave_up": to_1d(rb_2019_swu),
                                     "longwave_down": to_1d(rb_2019_lwd),
                                     "longwave_up": to_1d(rb_2019_lwu),
                                     "sensible_heat_flux": to_1d(rb_2019_shf),
                                     "latent_heat_flux": to_1d(rb_2019_lhf),
                                     "surface_energy_balance": to_1d(rb_2019_seb),
                                     "meltwater_runoff": to_1d(rb_2019_mru)})

rb_catchment_2020_df = pd.DataFrame({"time": to_1d(rb_2020_time),
                                     "air_temp": to_1d(rb_2020_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2020_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2020_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2020_swd),
                                     "shortwave_up": to_1d(rb_2020_swu),
                                     "longwave_down": to_1d(rb_2020_lwd),
                                     "longwave_up": to_1d(rb_2020_lwu),
                                     "sensible_heat_flux": to_1d(rb_2020_shf),
                                     "latent_heat_flux": to_1d(rb_2020_lhf),
                                     "surface_energy_balance": to_1d(rb_2020_seb),
                                     "meltwater_runoff": to_1d(rb_2020_mru)})

rb_catchment_2021_df = pd.DataFrame({"time": to_1d(rb_2021_time),
                                     "air_temp": to_1d(rb_2021_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2021_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2021_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2021_swd),
                                     "shortwave_up": to_1d(rb_2021_swu),
                                     "longwave_down": to_1d(rb_2021_lwd),
                                     "longwave_up": to_1d(rb_2021_lwu),
                                     "sensible_heat_flux": to_1d(rb_2021_shf),
                                     "latent_heat_flux": to_1d(rb_2021_lhf),
                                     "surface_energy_balance": to_1d(rb_2021_seb),
                                     "meltwater_runoff": to_1d(rb_2021_mru)})

rb_catchment_2022_df = pd.DataFrame({"time": to_1d(rb_2022_time),
                                     "air_temp": to_1d(rb_2022_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2022_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2022_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2022_swd),
                                     "shortwave_up": to_1d(rb_2022_swu),
                                     "longwave_down": to_1d(rb_2022_lwd),
                                     "longwave_up": to_1d(rb_2022_lwu),
                                     "sensible_heat_flux": to_1d(rb_2022_shf),
                                     "latent_heat_flux": to_1d(rb_2022_lhf),
                                     "surface_energy_balance": to_1d(rb_2022_seb),
                                     "meltwater_runoff": to_1d(rb_2022_mru)})

rb_catchment_2023_df = pd.DataFrame({"time": to_1d(rb_2023_time),
                                     "air_temp": to_1d(rb_2023_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2023_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2023_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2023_swd),
                                     "shortwave_up": to_1d(rb_2023_swu),
                                     "longwave_down": to_1d(rb_2023_lwd),
                                     "longwave_up": to_1d(rb_2023_lwu),
                                     "sensible_heat_flux": to_1d(rb_2023_shf),
                                     "latent_heat_flux": to_1d(rb_2023_lhf),
                                     "surface_energy_balance": to_1d(rb_2023_seb),
                                     "meltwater_runoff": to_1d(rb_2023_mru)})

rb_catchment_2024_df = pd.DataFrame({"time": to_1d(rb_2024_time),
                                     "air_temp": to_1d(rb_2024_air_temp[:, 0]),
                                    "ice_temp": to_1d(rb_2024_ice_temp[:, 0]),
                                     "albedo": to_1d(rb_2024_albedo[:, 0]),
                                     "shortwave_down": to_1d(rb_2024_swd),
                                     "shortwave_up": to_1d(rb_2024_swu),
                                     "longwave_down": to_1d(rb_2024_lwd),
                                     "longwave_up": to_1d(rb_2024_lwu),
                                     "sensible_heat_flux": to_1d(rb_2024_shf),
                                     "latent_heat_flux": to_1d(rb_2024_lhf),
                                     "surface_energy_balance": to_1d(rb_2024_seb),
                                     "meltwater_runoff": to_1d(rb_2024_mru)})

rb_catchment_2000_2024_df = pd.concat([rb_catchment_2000_df,
                                       rb_catchment_2001_df,
                                       rb_catchment_2002_df,
                                       rb_catchment_2003_df,
                                       rb_catchment_2004_df,
                                       rb_catchment_2005_df,
                                       rb_catchment_2006_df,
                                       rb_catchment_2007_df,
                                       rb_catchment_2008_df,
                                       rb_catchment_2009_df,
                                       rb_catchment_2010_df,
                                       rb_catchment_2011_df,
                                       rb_catchment_2012_df,
                                       rb_catchment_2013_df,
                                       rb_catchment_2014_df,
                                       rb_catchment_2015_df,
                                       rb_catchment_2016_df,
                                       rb_catchment_2017_df,
                                       rb_catchment_2018_df,
                                       rb_catchment_2019_df,
                                       rb_catchment_2020_df,
                                       rb_catchment_2021_df,
                                       rb_catchment_2022_df,
                                       rb_catchment_2023_df,
                                       rb_catchment_2024_df],
                                      ignore_index=True)


# Save AK4 variables to dataframe
ak4_catchment_2000_df = pd.DataFrame({"time": to_1d(ak4_2000_time),
                                      "air_temp": to_1d(ak4_2000_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2000_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2000_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2000_swd),
                                      "shortwave_up": to_1d(ak4_2000_swu),
                                      "longwave_down": to_1d(ak4_2000_lwd),
                                      "longwave_up": to_1d(ak4_2000_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2000_shf),
                                      "latent_heat_flux": to_1d(ak4_2000_lhf),
                                      "surface_energy_balance": to_1d(ak4_2000_seb),
                                      "meltwater_runoff": to_1d(ak4_2000_mru)})

ak4_catchment_2001_df = pd.DataFrame({"time": to_1d(ak4_2001_time),
                                      "air_temp": to_1d(ak4_2001_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2001_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2001_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2001_swd),
                                      "shortwave_up": to_1d(ak4_2001_swu),
                                      "longwave_down": to_1d(ak4_2001_lwd),
                                      "longwave_up": to_1d(ak4_2001_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2001_shf),
                                      "latent_heat_flux": to_1d(ak4_2001_lhf),
                                      "surface_energy_balance": to_1d(ak4_2001_seb),
                                      "meltwater_runoff": to_1d(ak4_2001_mru)})

ak4_catchment_2002_df = pd.DataFrame({"time": to_1d(ak4_2002_time),
                                      "air_temp": to_1d(ak4_2002_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2002_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2002_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2002_swd),
                                      "shortwave_up": to_1d(ak4_2002_swu),
                                      "longwave_down": to_1d(ak4_2002_lwd),
                                      "longwave_up": to_1d(ak4_2002_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2002_shf),
                                      "latent_heat_flux": to_1d(ak4_2002_lhf),
                                      "surface_energy_balance": to_1d(ak4_2002_seb),
                                      "meltwater_runoff": to_1d(ak4_2002_mru)})

ak4_catchment_2003_df = pd.DataFrame({"time": to_1d(ak4_2003_time),
                                      "air_temp": to_1d(ak4_2003_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2003_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2003_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2003_swd),
                                      "shortwave_up": to_1d(ak4_2003_swu),
                                      "longwave_down": to_1d(ak4_2003_lwd),
                                      "longwave_up": to_1d(ak4_2003_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2003_shf),
                                      "latent_heat_flux": to_1d(ak4_2003_lhf),
                                      "surface_energy_balance": to_1d(ak4_2003_seb),
                                      "meltwater_runoff": to_1d(ak4_2003_mru)})

ak4_catchment_2004_df = pd.DataFrame({"time": to_1d(ak4_2004_time),
                                      "air_temp": to_1d(ak4_2004_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2004_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2004_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2004_swd),
                                      "shortwave_up": to_1d(ak4_2004_swu),
                                      "longwave_down": to_1d(ak4_2004_lwd),
                                      "longwave_up": to_1d(ak4_2004_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2004_shf),
                                      "latent_heat_flux": to_1d(ak4_2004_lhf),
                                      "surface_energy_balance": to_1d(ak4_2004_seb),
                                      "meltwater_runoff": to_1d(ak4_2004_mru)})

ak4_catchment_2005_df = pd.DataFrame({"time": to_1d(ak4_2005_time),
                                      "air_temp": to_1d(ak4_2005_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2005_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2005_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2005_swd),
                                      "shortwave_up": to_1d(ak4_2005_swu),
                                      "longwave_down": to_1d(ak4_2005_lwd),
                                      "longwave_up": to_1d(ak4_2005_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2005_shf),
                                      "latent_heat_flux": to_1d(ak4_2005_lhf),
                                      "surface_energy_balance": to_1d(ak4_2005_seb),
                                      "meltwater_runoff": to_1d(ak4_2005_mru)})

ak4_catchment_2006_df = pd.DataFrame({"time": to_1d(ak4_2006_time),
                                      "air_temp": to_1d(ak4_2006_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2006_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2006_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2006_swd),
                                      "shortwave_up": to_1d(ak4_2006_swu),
                                      "longwave_down": to_1d(ak4_2006_lwd),
                                      "longwave_up": to_1d(ak4_2006_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2006_shf),
                                      "latent_heat_flux": to_1d(ak4_2006_lhf),
                                      "surface_energy_balance": to_1d(ak4_2006_seb),
                                      "meltwater_runoff": to_1d(ak4_2006_mru)})

ak4_catchment_2007_df = pd.DataFrame({"time": to_1d(ak4_2007_time),
                                      "air_temp": to_1d(ak4_2007_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2007_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2007_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2007_swd),
                                      "shortwave_up": to_1d(ak4_2007_swu),
                                      "longwave_down": to_1d(ak4_2007_lwd),
                                      "longwave_up": to_1d(ak4_2007_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2007_shf),
                                      "latent_heat_flux": to_1d(ak4_2007_lhf),
                                      "surface_energy_balance": to_1d(ak4_2007_seb),
                                      "meltwater_runoff": to_1d(ak4_2007_mru)})

ak4_catchment_2008_df = pd.DataFrame({"time": to_1d(ak4_2008_time),
                                      "air_temp": to_1d(ak4_2008_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2008_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2008_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2008_swd),
                                      "shortwave_up": to_1d(ak4_2008_swu),
                                      "longwave_down": to_1d(ak4_2008_lwd),
                                      "longwave_up": to_1d(ak4_2008_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2008_shf),
                                      "latent_heat_flux": to_1d(ak4_2008_lhf),
                                      "surface_energy_balance": to_1d(ak4_2008_seb),
                                      "meltwater_runoff": to_1d(ak4_2008_mru)})

ak4_catchment_2009_df = pd.DataFrame({"time": to_1d(ak4_2009_time),
                                      "air_temp": to_1d(ak4_2009_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2009_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2009_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2009_swd),
                                      "shortwave_up": to_1d(ak4_2009_swu),
                                      "longwave_down": to_1d(ak4_2009_lwd),
                                      "longwave_up": to_1d(ak4_2009_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2009_shf),
                                      "latent_heat_flux": to_1d(ak4_2009_lhf),
                                      "surface_energy_balance": to_1d(ak4_2009_seb),
                                      "meltwater_runoff": to_1d(ak4_2009_mru)})

ak4_catchment_2010_df = pd.DataFrame({"time": to_1d(ak4_2010_time),
                                      "air_temp": to_1d(ak4_2010_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2010_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2010_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2010_swd),
                                      "shortwave_up": to_1d(ak4_2010_swu),
                                      "longwave_down": to_1d(ak4_2010_lwd),
                                      "longwave_up": to_1d(ak4_2010_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2010_shf),
                                      "latent_heat_flux": to_1d(ak4_2010_lhf),
                                      "surface_energy_balance": to_1d(ak4_2010_seb),
                                      "meltwater_runoff": to_1d(ak4_2010_mru)})

ak4_catchment_2011_df = pd.DataFrame({"time": to_1d(ak4_2011_time),
                                      "air_temp": to_1d(ak4_2011_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2011_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2011_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2011_swd),
                                      "shortwave_up": to_1d(ak4_2011_swu),
                                      "longwave_down": to_1d(ak4_2011_lwd),
                                      "longwave_up": to_1d(ak4_2011_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2011_shf),
                                      "latent_heat_flux": to_1d(ak4_2011_lhf),
                                      "surface_energy_balance": to_1d(ak4_2011_seb),
                                      "meltwater_runoff": to_1d(ak4_2011_mru)})

ak4_catchment_2012_df = pd.DataFrame({"time": to_1d(ak4_2012_time),
                                      "air_temp": to_1d(ak4_2012_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2012_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2012_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2012_swd),
                                      "shortwave_up": to_1d(ak4_2012_swu),
                                      "longwave_down": to_1d(ak4_2012_lwd),
                                      "longwave_up": to_1d(ak4_2012_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2012_shf),
                                      "latent_heat_flux": to_1d(ak4_2012_lhf),
                                      "surface_energy_balance": to_1d(ak4_2012_seb),
                                      "meltwater_runoff": to_1d(ak4_2012_mru)})

ak4_catchment_2013_df = pd.DataFrame({"time": to_1d(ak4_2013_time),
                                      "air_temp": to_1d(ak4_2013_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2013_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2013_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2013_swd),
                                      "shortwave_up": to_1d(ak4_2013_swu),
                                      "longwave_down": to_1d(ak4_2013_lwd),
                                      "longwave_up": to_1d(ak4_2013_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2013_shf),
                                      "latent_heat_flux": to_1d(ak4_2013_lhf),
                                      "surface_energy_balance": to_1d(ak4_2013_seb),
                                      "meltwater_runoff": to_1d(ak4_2013_mru)})

ak4_catchment_2014_df = pd.DataFrame({"time": to_1d(ak4_2014_time),
                                      "air_temp": to_1d(ak4_2014_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2014_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2014_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2014_swd),
                                      "shortwave_up": to_1d(ak4_2014_swu),
                                      "longwave_down": to_1d(ak4_2014_lwd),
                                      "longwave_up": to_1d(ak4_2014_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2014_shf),
                                      "latent_heat_flux": to_1d(ak4_2014_lhf),
                                      "surface_energy_balance": to_1d(ak4_2014_seb),
                                      "meltwater_runoff": to_1d(ak4_2014_mru)})

ak4_catchment_2015_df = pd.DataFrame({"time": to_1d(ak4_2015_time),
                                      "air_temp": to_1d(ak4_2015_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2015_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2015_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2015_swd),
                                      "shortwave_up": to_1d(ak4_2015_swu),
                                      "longwave_down": to_1d(ak4_2015_lwd),
                                      "longwave_up": to_1d(ak4_2015_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2015_shf),
                                      "latent_heat_flux": to_1d(ak4_2015_lhf),
                                      "surface_energy_balance": to_1d(ak4_2015_seb),
                                      "meltwater_runoff": to_1d(ak4_2015_mru)})

ak4_catchment_2016_df = pd.DataFrame({"time": to_1d(ak4_2016_time),
                                      "air_temp": to_1d(ak4_2016_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2016_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2016_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2016_swd),
                                      "shortwave_up": to_1d(ak4_2016_swu),
                                      "longwave_down": to_1d(ak4_2016_lwd),
                                      "longwave_up": to_1d(ak4_2016_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2016_shf),
                                      "latent_heat_flux": to_1d(ak4_2016_lhf),
                                      "surface_energy_balance": to_1d(ak4_2016_seb),
                                      "meltwater_runoff": to_1d(ak4_2016_mru)})

ak4_catchment_2017_df = pd.DataFrame({"time": to_1d(ak4_2017_time),
                                      "air_temp": to_1d(ak4_2017_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2017_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2017_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2017_swd),
                                      "shortwave_up": to_1d(ak4_2017_swu),
                                      "longwave_down": to_1d(ak4_2017_lwd),
                                      "longwave_up": to_1d(ak4_2017_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2017_shf),
                                      "latent_heat_flux": to_1d(ak4_2017_lhf),
                                      "surface_energy_balance": to_1d(ak4_2017_seb),
                                      "meltwater_runoff": to_1d(ak4_2017_mru)})

ak4_catchment_2018_df = pd.DataFrame({"time": to_1d(ak4_2018_time),
                                      "air_temp": to_1d(ak4_2018_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2018_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2018_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2018_swd),
                                      "shortwave_up": to_1d(ak4_2018_swu),
                                      "longwave_down": to_1d(ak4_2018_lwd),
                                      "longwave_up": to_1d(ak4_2018_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2018_shf),
                                      "latent_heat_flux": to_1d(ak4_2018_lhf),
                                      "surface_energy_balance": to_1d(ak4_2018_seb),
                                      "meltwater_runoff": to_1d(ak4_2018_mru)})

ak4_catchment_2019_df = pd.DataFrame({"time": to_1d(ak4_2019_time),
                                      "air_temp": to_1d(ak4_2019_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2019_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2019_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2019_swd),
                                      "shortwave_up": to_1d(ak4_2019_swu),
                                      "longwave_down": to_1d(ak4_2019_lwd),
                                      "longwave_up": to_1d(ak4_2019_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2019_shf),
                                      "latent_heat_flux": to_1d(ak4_2019_lhf),
                                      "surface_energy_balance": to_1d(ak4_2019_seb),
                                      "meltwater_runoff": to_1d(ak4_2019_mru)})

ak4_catchment_2020_df = pd.DataFrame({"time": to_1d(ak4_2020_time),
                                      "air_temp": to_1d(ak4_2020_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2020_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2020_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2020_swd),
                                      "shortwave_up": to_1d(ak4_2020_swu),
                                      "longwave_down": to_1d(ak4_2020_lwd),
                                      "longwave_up": to_1d(ak4_2020_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2020_shf),
                                      "latent_heat_flux": to_1d(ak4_2020_lhf),
                                      "surface_energy_balance": to_1d(ak4_2020_seb),
                                      "meltwater_runoff": to_1d(ak4_2020_mru)})

ak4_catchment_2021_df = pd.DataFrame({"time": to_1d(ak4_2021_time),
                                      "air_temp": to_1d(ak4_2021_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2021_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2021_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2021_swd),
                                      "shortwave_up": to_1d(ak4_2021_swu),
                                      "longwave_down": to_1d(ak4_2021_lwd),
                                      "longwave_up": to_1d(ak4_2021_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2021_shf),
                                      "latent_heat_flux": to_1d(ak4_2021_lhf),
                                      "surface_energy_balance": to_1d(ak4_2021_seb),
                                      "meltwater_runoff": to_1d(ak4_2021_mru)})

ak4_catchment_2022_df = pd.DataFrame({"time": to_1d(ak4_2022_time),
                                      "air_temp": to_1d(ak4_2022_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2022_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2022_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2022_swd),
                                      "shortwave_up": to_1d(ak4_2022_swu),
                                      "longwave_down": to_1d(ak4_2022_lwd),
                                      "longwave_up": to_1d(ak4_2022_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2022_shf),
                                      "latent_heat_flux": to_1d(ak4_2022_lhf),
                                      "surface_energy_balance": to_1d(ak4_2022_seb),
                                      "meltwater_runoff": to_1d(ak4_2022_mru)})

ak4_catchment_2023_df = pd.DataFrame({"time": to_1d(ak4_2023_time),
                                      "air_temp": to_1d(ak4_2023_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2023_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2023_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2023_swd),
                                      "shortwave_up": to_1d(ak4_2023_swu),
                                      "longwave_down": to_1d(ak4_2023_lwd),
                                      "longwave_up": to_1d(ak4_2023_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2023_shf),
                                      "latent_heat_flux": to_1d(ak4_2023_lhf),
                                      "surface_energy_balance": to_1d(ak4_2023_seb),
                                      "meltwater_runoff": to_1d(ak4_2023_mru)})

ak4_catchment_2024_df = pd.DataFrame({"time": to_1d(ak4_2024_time),
                                      "air_temp": to_1d(ak4_2024_air_temp[:, 0]),
                                     "ice_temp": to_1d(ak4_2024_ice_temp[:, 0]),
                                      "albedo": to_1d(ak4_2024_albedo[:, 0]),
                                      "shortwave_down": to_1d(ak4_2024_swd),
                                      "shortwave_up": to_1d(ak4_2024_swu),
                                      "longwave_down": to_1d(ak4_2024_lwd),
                                      "longwave_up": to_1d(ak4_2024_lwu),
                                      "sensible_heat_flux": to_1d(ak4_2024_shf),
                                      "latent_heat_flux": to_1d(ak4_2024_lhf),
                                      "surface_energy_balance": to_1d(ak4_2024_seb),
                                      "meltwater_runoff": to_1d(ak4_2024_mru)})

ak4_catchment_2008_2016_df = pd.concat([ak4_catchment_2008_df,
                                        ak4_catchment_2009_df,
                                        ak4_catchment_2010_df,
                                        ak4_catchment_2011_df,
                                        ak4_catchment_2012_df,
                                        ak4_catchment_2013_df,
                                        ak4_catchment_2014_df,
                                        ak4_catchment_2015_df,
                                        ak4_catchment_2016_df],
                                       ignore_index=True)

ak4_catchment_2000_2024_df = pd.concat([ak4_catchment_2000_df,
                                        ak4_catchment_2001_df,
                                        ak4_catchment_2002_df,
                                        ak4_catchment_2003_df,
                                        ak4_catchment_2004_df,
                                        ak4_catchment_2005_df,
                                        ak4_catchment_2006_df,
                                        ak4_catchment_2007_df,
                                        ak4_catchment_2008_df,
                                        ak4_catchment_2009_df,
                                        ak4_catchment_2010_df,
                                        ak4_catchment_2011_df,
                                        ak4_catchment_2012_df,
                                        ak4_catchment_2013_df,
                                        ak4_catchment_2014_df,
                                        ak4_catchment_2015_df,
                                        ak4_catchment_2016_df,
                                        ak4_catchment_2017_df,
                                        ak4_catchment_2018_df,
                                        ak4_catchment_2019_df,
                                        ak4_catchment_2020_df,
                                        ak4_catchment_2021_df,
                                        ak4_catchment_2022_df,
                                        ak4_catchment_2023_df,
                                        ak4_catchment_2024_df],
                                       ignore_index=True)

# Save Minturn variables to dataframe
minturn_catchment_2000_df = pd.DataFrame({"time": to_1d(minturn_2000_time),
                                           "air_temp": to_1d(minturn_2000_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2000_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2000_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2000_swd),
                                           "shortwave_up": to_1d(minturn_2000_swu),
                                           "longwave_down": to_1d(minturn_2000_lwd),
                                           "longwave_up": to_1d(minturn_2000_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2000_shf),
                                           "latent_heat_flux": to_1d(minturn_2000_lhf),
                                           "surface_energy_balance": to_1d(minturn_2000_seb),
                                           "meltwater_runoff": to_1d(minturn_2000_mru)})

minturn_catchment_2001_df = pd.DataFrame({"time": to_1d(minturn_2001_time),
                                           "air_temp": to_1d(minturn_2001_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2001_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2001_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2001_swd),
                                           "shortwave_up": to_1d(minturn_2001_swu),
                                           "longwave_down": to_1d(minturn_2001_lwd),
                                           "longwave_up": to_1d(minturn_2001_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2001_shf),
                                           "latent_heat_flux": to_1d(minturn_2001_lhf),
                                           "surface_energy_balance": to_1d(minturn_2001_seb),
                                           "meltwater_runoff": to_1d(minturn_2001_mru)})

minturn_catchment_2002_df = pd.DataFrame({"time": to_1d(minturn_2002_time),
                                           "air_temp": to_1d(minturn_2002_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2002_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2002_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2002_swd),
                                           "shortwave_up": to_1d(minturn_2002_swu),
                                           "longwave_down": to_1d(minturn_2002_lwd),
                                           "longwave_up": to_1d(minturn_2002_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2002_shf),
                                           "latent_heat_flux": to_1d(minturn_2002_lhf),
                                           "surface_energy_balance": to_1d(minturn_2002_seb),
                                           "meltwater_runoff": to_1d(minturn_2002_mru)})

minturn_catchment_2003_df = pd.DataFrame({"time": to_1d(minturn_2003_time),
                                           "air_temp": to_1d(minturn_2003_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2003_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2003_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2003_swd),
                                           "shortwave_up": to_1d(minturn_2003_swu),
                                           "longwave_down": to_1d(minturn_2003_lwd),
                                           "longwave_up": to_1d(minturn_2003_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2003_shf),
                                           "latent_heat_flux": to_1d(minturn_2003_lhf),
                                           "surface_energy_balance": to_1d(minturn_2003_seb),
                                           "meltwater_runoff": to_1d(minturn_2003_mru)})

minturn_catchment_2004_df = pd.DataFrame({"time": to_1d(minturn_2004_time),
                                           "air_temp": to_1d(minturn_2004_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2004_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2004_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2004_swd),
                                           "shortwave_up": to_1d(minturn_2004_swu),
                                           "longwave_down": to_1d(minturn_2004_lwd),
                                           "longwave_up": to_1d(minturn_2004_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2004_shf),
                                           "latent_heat_flux": to_1d(minturn_2004_lhf),
                                           "surface_energy_balance": to_1d(minturn_2004_seb),
                                           "meltwater_runoff": to_1d(minturn_2004_mru)})

minturn_catchment_2005_df = pd.DataFrame({"time": to_1d(minturn_2005_time),
                                           "air_temp": to_1d(minturn_2005_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2005_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2005_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2005_swd),
                                           "shortwave_up": to_1d(minturn_2005_swu),
                                           "longwave_down": to_1d(minturn_2005_lwd),
                                           "longwave_up": to_1d(minturn_2005_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2005_shf),
                                           "latent_heat_flux": to_1d(minturn_2005_lhf),
                                           "surface_energy_balance": to_1d(minturn_2005_seb),
                                           "meltwater_runoff": to_1d(minturn_2005_mru)})

minturn_catchment_2006_df = pd.DataFrame({"time": to_1d(minturn_2006_time),
                                           "air_temp": to_1d(minturn_2006_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2006_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2006_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2006_swd),
                                           "shortwave_up": to_1d(minturn_2006_swu),
                                           "longwave_down": to_1d(minturn_2006_lwd),
                                           "longwave_up": to_1d(minturn_2006_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2006_shf),
                                           "latent_heat_flux": to_1d(minturn_2006_lhf),
                                           "surface_energy_balance": to_1d(minturn_2006_seb),
                                           "meltwater_runoff": to_1d(minturn_2006_mru)})

minturn_catchment_2007_df = pd.DataFrame({"time": to_1d(minturn_2007_time),
                                           "air_temp": to_1d(minturn_2007_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2007_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2007_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2007_swd),
                                           "shortwave_up": to_1d(minturn_2007_swu),
                                           "longwave_down": to_1d(minturn_2007_lwd),
                                           "longwave_up": to_1d(minturn_2007_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2007_shf),
                                           "latent_heat_flux": to_1d(minturn_2007_lhf),
                                           "surface_energy_balance": to_1d(minturn_2007_seb),
                                           "meltwater_runoff": to_1d(minturn_2007_mru)})

minturn_catchment_2008_df = pd.DataFrame({"time": to_1d(minturn_2008_time),
                                           "air_temp": to_1d(minturn_2008_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2008_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2008_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2008_swd),
                                           "shortwave_up": to_1d(minturn_2008_swu),
                                           "longwave_down": to_1d(minturn_2008_lwd),
                                           "longwave_up": to_1d(minturn_2008_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2008_shf),
                                           "latent_heat_flux": to_1d(minturn_2008_lhf),
                                           "surface_energy_balance": to_1d(minturn_2008_seb),
                                           "meltwater_runoff": to_1d(minturn_2008_mru)})

minturn_catchment_2009_df = pd.DataFrame({"time": to_1d(minturn_2009_time),
                                           "air_temp": to_1d(minturn_2009_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2009_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2009_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2009_swd),
                                           "shortwave_up": to_1d(minturn_2009_swu),
                                           "longwave_down": to_1d(minturn_2009_lwd),
                                           "longwave_up": to_1d(minturn_2009_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2009_shf),
                                           "latent_heat_flux": to_1d(minturn_2009_lhf),
                                           "surface_energy_balance": to_1d(minturn_2009_seb),
                                           "meltwater_runoff": to_1d(minturn_2009_mru)})

minturn_catchment_2010_df = pd.DataFrame({"time": to_1d(minturn_2010_time),
                                           "air_temp": to_1d(minturn_2010_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2010_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2010_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2010_swd),
                                           "shortwave_up": to_1d(minturn_2010_swu),
                                           "longwave_down": to_1d(minturn_2010_lwd),
                                           "longwave_up": to_1d(minturn_2010_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2010_shf),
                                           "latent_heat_flux": to_1d(minturn_2010_lhf),
                                           "surface_energy_balance": to_1d(minturn_2010_seb),
                                           "meltwater_runoff": to_1d(minturn_2010_mru)})

minturn_catchment_2011_df = pd.DataFrame({"time": to_1d(minturn_2011_time),
                                           "air_temp": to_1d(minturn_2011_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2011_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2011_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2011_swd),
                                           "shortwave_up": to_1d(minturn_2011_swu),
                                           "longwave_down": to_1d(minturn_2011_lwd),
                                           "longwave_up": to_1d(minturn_2011_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2011_shf),
                                           "latent_heat_flux": to_1d(minturn_2011_lhf),
                                           "surface_energy_balance": to_1d(minturn_2011_seb),
                                           "meltwater_runoff": to_1d(minturn_2011_mru)})

minturn_catchment_2012_df = pd.DataFrame({"time": to_1d(minturn_2012_time),
                                           "air_temp": to_1d(minturn_2012_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2012_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2012_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2012_swd),
                                           "shortwave_up": to_1d(minturn_2012_swu),
                                           "longwave_down": to_1d(minturn_2012_lwd),
                                           "longwave_up": to_1d(minturn_2012_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2012_shf),
                                           "latent_heat_flux": to_1d(minturn_2012_lhf),
                                           "surface_energy_balance": to_1d(minturn_2012_seb),
                                           "meltwater_runoff": to_1d(minturn_2012_mru)})

minturn_catchment_2013_df = pd.DataFrame({"time": to_1d(minturn_2013_time),
                                           "air_temp": to_1d(minturn_2013_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2013_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2013_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2013_swd),
                                           "shortwave_up": to_1d(minturn_2013_swu),
                                           "longwave_down": to_1d(minturn_2013_lwd),
                                           "longwave_up": to_1d(minturn_2013_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2013_shf),
                                           "latent_heat_flux": to_1d(minturn_2013_lhf),
                                           "surface_energy_balance": to_1d(minturn_2013_seb),
                                           "meltwater_runoff": to_1d(minturn_2013_mru)})

minturn_catchment_2014_df = pd.DataFrame({"time": to_1d(minturn_2014_time),
                                           "air_temp": to_1d(minturn_2014_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2014_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2014_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2014_swd),
                                           "shortwave_up": to_1d(minturn_2014_swu),
                                           "longwave_down": to_1d(minturn_2014_lwd),
                                           "longwave_up": to_1d(minturn_2014_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2014_shf),
                                           "latent_heat_flux": to_1d(minturn_2014_lhf),
                                           "surface_energy_balance": to_1d(minturn_2014_seb),
                                           "meltwater_runoff": to_1d(minturn_2014_mru)})

minturn_catchment_2015_df = pd.DataFrame({"time": to_1d(minturn_2015_time),
                                           "air_temp": to_1d(minturn_2015_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2015_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2015_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2015_swd),
                                           "shortwave_up": to_1d(minturn_2015_swu),
                                           "longwave_down": to_1d(minturn_2015_lwd),
                                           "longwave_up": to_1d(minturn_2015_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2015_shf),
                                           "latent_heat_flux": to_1d(minturn_2015_lhf),
                                           "surface_energy_balance": to_1d(minturn_2015_seb),
                                           "meltwater_runoff": to_1d(minturn_2015_mru)})

minturn_catchment_2016_df = pd.DataFrame({"time": to_1d(minturn_2016_time),
                                           "air_temp": to_1d(minturn_2016_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2016_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2016_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2016_swd),
                                           "shortwave_up": to_1d(minturn_2016_swu),
                                           "longwave_down": to_1d(minturn_2016_lwd),
                                           "longwave_up": to_1d(minturn_2016_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2016_shf),
                                           "latent_heat_flux": to_1d(minturn_2016_lhf),
                                           "surface_energy_balance": to_1d(minturn_2016_seb),
                                           "meltwater_runoff": to_1d(minturn_2016_mru)})

minturn_catchment_2017_df = pd.DataFrame({"time": to_1d(minturn_2017_time),
                                           "air_temp": to_1d(minturn_2017_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2017_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2017_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2017_swd),
                                           "shortwave_up": to_1d(minturn_2017_swu),
                                           "longwave_down": to_1d(minturn_2017_lwd),
                                           "longwave_up": to_1d(minturn_2017_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2017_shf),
                                           "latent_heat_flux": to_1d(minturn_2017_lhf),
                                           "surface_energy_balance": to_1d(minturn_2017_seb),
                                           "meltwater_runoff": to_1d(minturn_2017_mru)})

minturn_catchment_2018_df = pd.DataFrame({"time": to_1d(minturn_2018_time),
                                           "air_temp": to_1d(minturn_2018_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2018_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2018_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2018_swd),
                                           "shortwave_up": to_1d(minturn_2018_swu),
                                           "longwave_down": to_1d(minturn_2018_lwd),
                                           "longwave_up": to_1d(minturn_2018_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2018_shf),
                                           "latent_heat_flux": to_1d(minturn_2018_lhf),
                                           "surface_energy_balance": to_1d(minturn_2018_seb),
                                           "meltwater_runoff": to_1d(minturn_2018_mru)})

minturn_catchment_2019_df = pd.DataFrame({"time": to_1d(minturn_2019_time),
                                           "air_temp": to_1d(minturn_2019_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2019_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2019_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2019_swd),
                                           "shortwave_up": to_1d(minturn_2019_swu),
                                           "longwave_down": to_1d(minturn_2019_lwd),
                                           "longwave_up": to_1d(minturn_2019_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2019_shf),
                                           "latent_heat_flux": to_1d(minturn_2019_lhf),
                                           "surface_energy_balance": to_1d(minturn_2019_seb),
                                           "meltwater_runoff": to_1d(minturn_2019_mru)})

minturn_catchment_2020_df = pd.DataFrame({"time": to_1d(minturn_2020_time),
                                           "air_temp": to_1d(minturn_2020_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2020_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2020_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2020_swd),
                                           "shortwave_up": to_1d(minturn_2020_swu),
                                           "longwave_down": to_1d(minturn_2020_lwd),
                                           "longwave_up": to_1d(minturn_2020_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2020_shf),
                                           "latent_heat_flux": to_1d(minturn_2020_lhf),
                                           "surface_energy_balance": to_1d(minturn_2020_seb),
                                           "meltwater_runoff": to_1d(minturn_2020_mru)})

minturn_catchment_2021_df = pd.DataFrame({"time": to_1d(minturn_2021_time),
                                           "air_temp": to_1d(minturn_2021_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2021_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2021_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2021_swd),
                                           "shortwave_up": to_1d(minturn_2021_swu),
                                           "longwave_down": to_1d(minturn_2021_lwd),
                                           "longwave_up": to_1d(minturn_2021_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2021_shf),
                                           "latent_heat_flux": to_1d(minturn_2021_lhf),
                                           "surface_energy_balance": to_1d(minturn_2021_seb),
                                           "meltwater_runoff": to_1d(minturn_2021_mru)})

minturn_catchment_2022_df = pd.DataFrame({"time": to_1d(minturn_2022_time),
                                           "air_temp": to_1d(minturn_2022_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2022_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2022_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2022_swd),
                                           "shortwave_up": to_1d(minturn_2022_swu),
                                           "longwave_down": to_1d(minturn_2022_lwd),
                                           "longwave_up": to_1d(minturn_2022_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2022_shf),
                                           "latent_heat_flux": to_1d(minturn_2022_lhf),
                                           "surface_energy_balance": to_1d(minturn_2022_seb),
                                           "meltwater_runoff": to_1d(minturn_2022_mru)})

minturn_catchment_2023_df = pd.DataFrame({"time": to_1d(minturn_2023_time),
                                           "air_temp": to_1d(minturn_2023_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2023_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2023_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2023_swd),
                                           "shortwave_up": to_1d(minturn_2023_swu),
                                           "longwave_down": to_1d(minturn_2023_lwd),
                                           "longwave_up": to_1d(minturn_2023_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2023_shf),
                                           "latent_heat_flux": to_1d(minturn_2023_lhf),
                                           "surface_energy_balance": to_1d(minturn_2023_seb),
                                           "meltwater_runoff": to_1d(minturn_2023_mru)})

minturn_catchment_2024_df = pd.DataFrame({"time": to_1d(minturn_2024_time),
                                           "air_temp": to_1d(minturn_2024_air_temp[:, 0]),
                                          "ice_temp": to_1d(minturn_2024_ice_temp[:, 0]),
                                           "albedo": to_1d(minturn_2024_albedo[:, 0]),
                                           "shortwave_down": to_1d(minturn_2024_swd),
                                           "shortwave_up": to_1d(minturn_2024_swu),
                                           "longwave_down": to_1d(minturn_2024_lwd),
                                           "longwave_up": to_1d(minturn_2024_lwu),
                                           "sensible_heat_flux": to_1d(minturn_2024_shf),
                                           "latent_heat_flux": to_1d(minturn_2024_lhf),
                                           "surface_energy_balance": to_1d(minturn_2024_seb),
                                           "meltwater_runoff": to_1d(minturn_2024_mru)})

minturn_catchment_2019_2020_df = pd.concat([minturn_catchment_2019_df,
                                            minturn_catchment_2020_df],
                                            ignore_index=True)

minturn_catchment_2000_2024_df = pd.concat([minturn_catchment_2000_df,
                                            minturn_catchment_2001_df,
                                            minturn_catchment_2002_df,
                                            minturn_catchment_2003_df,
                                            minturn_catchment_2004_df,
                                            minturn_catchment_2005_df,
                                            minturn_catchment_2006_df,
                                            minturn_catchment_2007_df,
                                            minturn_catchment_2008_df,
                                            minturn_catchment_2009_df,
                                            minturn_catchment_2010_df,
                                            minturn_catchment_2011_df,
                                            minturn_catchment_2012_df,
                                            minturn_catchment_2013_df,
                                            minturn_catchment_2014_df,
                                            minturn_catchment_2015_df,
                                            minturn_catchment_2016_df,
                                            minturn_catchment_2017_df,
                                            minturn_catchment_2018_df,
                                            minturn_catchment_2019_df,
                                            minturn_catchment_2020_df,
                                            minturn_catchment_2021_df,
                                            minturn_catchment_2022_df,
                                            minturn_catchment_2023_df,
                                            minturn_catchment_2024_df],
                                           ignore_index=True)

# Save North variables to dataframe
north_catchment_2000_df = pd.DataFrame({"time": to_1d(north_2000_time),
                                           "air_temp": to_1d(north_2000_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2000_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2000_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2000_swd),
                                           "shortwave_up": to_1d(north_2000_swu),
                                           "longwave_down": to_1d(north_2000_lwd),
                                           "longwave_up": to_1d(north_2000_lwu),
                                           "sensible_heat_flux": to_1d(north_2000_shf),
                                           "latent_heat_flux": to_1d(north_2000_lhf),
                                           "surface_energy_balance": to_1d(north_2000_seb),
                                           "meltwater_runoff": to_1d(north_2000_mru)})

north_catchment_2001_df = pd.DataFrame({"time": to_1d(north_2001_time),
                                           "air_temp": to_1d(north_2001_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2001_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2001_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2001_swd),
                                           "shortwave_up": to_1d(north_2001_swu),
                                           "longwave_down": to_1d(north_2001_lwd),
                                           "longwave_up": to_1d(north_2001_lwu),
                                           "sensible_heat_flux": to_1d(north_2001_shf),
                                           "latent_heat_flux": to_1d(north_2001_lhf),
                                           "surface_energy_balance": to_1d(north_2001_seb),
                                           "meltwater_runoff": to_1d(north_2001_mru)})

north_catchment_2002_df = pd.DataFrame({"time": to_1d(north_2002_time),
                                           "air_temp": to_1d(north_2002_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2002_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2002_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2002_swd),
                                           "shortwave_up": to_1d(north_2002_swu),
                                           "longwave_down": to_1d(north_2002_lwd),
                                           "longwave_up": to_1d(north_2002_lwu),
                                           "sensible_heat_flux": to_1d(north_2002_shf),
                                           "latent_heat_flux": to_1d(north_2002_lhf),
                                           "surface_energy_balance": to_1d(north_2002_seb),
                                           "meltwater_runoff": to_1d(north_2002_mru)})

north_catchment_2003_df = pd.DataFrame({"time": to_1d(north_2003_time),
                                           "air_temp": to_1d(north_2003_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2003_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2003_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2003_swd),
                                           "shortwave_up": to_1d(north_2003_swu),
                                           "longwave_down": to_1d(north_2003_lwd),
                                           "longwave_up": to_1d(north_2003_lwu),
                                           "sensible_heat_flux": to_1d(north_2003_shf),
                                           "latent_heat_flux": to_1d(north_2003_lhf),
                                           "surface_energy_balance": to_1d(north_2003_seb),
                                           "meltwater_runoff": to_1d(north_2003_mru)})

north_catchment_2004_df = pd.DataFrame({"time": to_1d(north_2004_time),
                                           "air_temp": to_1d(north_2004_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2004_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2004_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2004_swd),
                                           "shortwave_up": to_1d(north_2004_swu),
                                           "longwave_down": to_1d(north_2004_lwd),
                                           "longwave_up": to_1d(north_2004_lwu),
                                           "sensible_heat_flux": to_1d(north_2004_shf),
                                           "latent_heat_flux": to_1d(north_2004_lhf),
                                           "surface_energy_balance": to_1d(north_2004_seb),
                                           "meltwater_runoff": to_1d(north_2004_mru)})

north_catchment_2005_df = pd.DataFrame({"time": to_1d(north_2005_time),
                                           "air_temp": to_1d(north_2005_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2005_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2005_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2005_swd),
                                           "shortwave_up": to_1d(north_2005_swu),
                                           "longwave_down": to_1d(north_2005_lwd),
                                           "longwave_up": to_1d(north_2005_lwu),
                                           "sensible_heat_flux": to_1d(north_2005_shf),
                                           "latent_heat_flux": to_1d(north_2005_lhf),
                                           "surface_energy_balance": to_1d(north_2005_seb),
                                           "meltwater_runoff": to_1d(north_2005_mru)})

north_catchment_2006_df = pd.DataFrame({"time": to_1d(north_2006_time),
                                           "air_temp": to_1d(north_2006_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2006_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2006_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2006_swd),
                                           "shortwave_up": to_1d(north_2006_swu),
                                           "longwave_down": to_1d(north_2006_lwd),
                                           "longwave_up": to_1d(north_2006_lwu),
                                           "sensible_heat_flux": to_1d(north_2006_shf),
                                           "latent_heat_flux": to_1d(north_2006_lhf),
                                           "surface_energy_balance": to_1d(north_2006_seb),
                                           "meltwater_runoff": to_1d(north_2006_mru)})

north_catchment_2007_df = pd.DataFrame({"time": to_1d(north_2007_time),
                                           "air_temp": to_1d(north_2007_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2007_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2007_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2007_swd),
                                           "shortwave_up": to_1d(north_2007_swu),
                                           "longwave_down": to_1d(north_2007_lwd),
                                           "longwave_up": to_1d(north_2007_lwu),
                                           "sensible_heat_flux": to_1d(north_2007_shf),
                                           "latent_heat_flux": to_1d(north_2007_lhf),
                                           "surface_energy_balance": to_1d(north_2007_seb),
                                           "meltwater_runoff": to_1d(north_2007_mru)})

north_catchment_2008_df = pd.DataFrame({"time": to_1d(north_2008_time),
                                           "air_temp": to_1d(north_2008_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2008_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2008_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2008_swd),
                                           "shortwave_up": to_1d(north_2008_swu),
                                           "longwave_down": to_1d(north_2008_lwd),
                                           "longwave_up": to_1d(north_2008_lwu),
                                           "sensible_heat_flux": to_1d(north_2008_shf),
                                           "latent_heat_flux": to_1d(north_2008_lhf),
                                           "surface_energy_balance": to_1d(north_2008_seb),
                                           "meltwater_runoff": to_1d(north_2008_mru)})

north_catchment_2009_df = pd.DataFrame({"time": to_1d(north_2009_time),
                                           "air_temp": to_1d(north_2009_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2009_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2009_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2009_swd),
                                           "shortwave_up": to_1d(north_2009_swu),
                                           "longwave_down": to_1d(north_2009_lwd),
                                           "longwave_up": to_1d(north_2009_lwu),
                                           "sensible_heat_flux": to_1d(north_2009_shf),
                                           "latent_heat_flux": to_1d(north_2009_lhf),
                                           "surface_energy_balance": to_1d(north_2009_seb),
                                           "meltwater_runoff": to_1d(north_2009_mru)})

north_catchment_2010_df = pd.DataFrame({"time": to_1d(north_2010_time),
                                           "air_temp": to_1d(north_2010_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2010_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2010_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2010_swd),
                                           "shortwave_up": to_1d(north_2010_swu),
                                           "longwave_down": to_1d(north_2010_lwd),
                                           "longwave_up": to_1d(north_2010_lwu),
                                           "sensible_heat_flux": to_1d(north_2010_shf),
                                           "latent_heat_flux": to_1d(north_2010_lhf),
                                           "surface_energy_balance": to_1d(north_2010_seb),
                                           "meltwater_runoff": to_1d(north_2010_mru)})

north_catchment_2011_df = pd.DataFrame({"time": to_1d(north_2011_time),
                                           "air_temp": to_1d(north_2011_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2011_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2011_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2011_swd),
                                           "shortwave_up": to_1d(north_2011_swu),
                                           "longwave_down": to_1d(north_2011_lwd),
                                           "longwave_up": to_1d(north_2011_lwu),
                                           "sensible_heat_flux": to_1d(north_2011_shf),
                                           "latent_heat_flux": to_1d(north_2011_lhf),
                                           "surface_energy_balance": to_1d(north_2011_seb),
                                           "meltwater_runoff": to_1d(north_2011_mru)})

north_catchment_2012_df = pd.DataFrame({"time": to_1d(north_2012_time),
                                           "air_temp": to_1d(north_2012_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2012_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2012_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2012_swd),
                                           "shortwave_up": to_1d(north_2012_swu),
                                           "longwave_down": to_1d(north_2012_lwd),
                                           "longwave_up": to_1d(north_2012_lwu),
                                           "sensible_heat_flux": to_1d(north_2012_shf),
                                           "latent_heat_flux": to_1d(north_2012_lhf),
                                           "surface_energy_balance": to_1d(north_2012_seb),
                                           "meltwater_runoff": to_1d(north_2012_mru)})

north_catchment_2013_df = pd.DataFrame({"time": to_1d(north_2013_time),
                                           "air_temp": to_1d(north_2013_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2013_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2013_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2013_swd),
                                           "shortwave_up": to_1d(north_2013_swu),
                                           "longwave_down": to_1d(north_2013_lwd),
                                           "longwave_up": to_1d(north_2013_lwu),
                                           "sensible_heat_flux": to_1d(north_2013_shf),
                                           "latent_heat_flux": to_1d(north_2013_lhf),
                                           "surface_energy_balance": to_1d(north_2013_seb),
                                           "meltwater_runoff": to_1d(north_2013_mru)})

north_catchment_2014_df = pd.DataFrame({"time": to_1d(north_2014_time),
                                           "air_temp": to_1d(north_2014_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2014_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2014_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2014_swd),
                                           "shortwave_up": to_1d(north_2014_swu),
                                           "longwave_down": to_1d(north_2014_lwd),
                                           "longwave_up": to_1d(north_2014_lwu),
                                           "sensible_heat_flux": to_1d(north_2014_shf),
                                           "latent_heat_flux": to_1d(north_2014_lhf),
                                           "surface_energy_balance": to_1d(north_2014_seb),
                                           "meltwater_runoff": to_1d(north_2014_mru)})

north_catchment_2015_df = pd.DataFrame({"time": to_1d(north_2015_time),
                                           "air_temp": to_1d(north_2015_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2015_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2015_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2015_swd),
                                           "shortwave_up": to_1d(north_2015_swu),
                                           "longwave_down": to_1d(north_2015_lwd),
                                           "longwave_up": to_1d(north_2015_lwu),
                                           "sensible_heat_flux": to_1d(north_2015_shf),
                                           "latent_heat_flux": to_1d(north_2015_lhf),
                                           "surface_energy_balance": to_1d(north_2015_seb),
                                           "meltwater_runoff": to_1d(north_2015_mru)})

north_catchment_2016_df = pd.DataFrame({"time": to_1d(north_2016_time),
                                           "air_temp": to_1d(north_2016_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2016_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2016_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2016_swd),
                                           "shortwave_up": to_1d(north_2016_swu),
                                           "longwave_down": to_1d(north_2016_lwd),
                                           "longwave_up": to_1d(north_2016_lwu),
                                           "sensible_heat_flux": to_1d(north_2016_shf),
                                           "latent_heat_flux": to_1d(north_2016_lhf),
                                           "surface_energy_balance": to_1d(north_2016_seb),
                                           "meltwater_runoff": to_1d(north_2016_mru)})

north_catchment_2017_df = pd.DataFrame({"time": to_1d(north_2017_time),
                                           "air_temp": to_1d(north_2017_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2017_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2017_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2017_swd),
                                           "shortwave_up": to_1d(north_2017_swu),
                                           "longwave_down": to_1d(north_2017_lwd),
                                           "longwave_up": to_1d(north_2017_lwu),
                                           "sensible_heat_flux": to_1d(north_2017_shf),
                                           "latent_heat_flux": to_1d(north_2017_lhf),
                                           "surface_energy_balance": to_1d(north_2017_seb),
                                           "meltwater_runoff": to_1d(north_2017_mru)})

north_catchment_2018_df = pd.DataFrame({"time": to_1d(north_2018_time),
                                           "air_temp": to_1d(north_2018_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2018_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2018_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2018_swd),
                                           "shortwave_up": to_1d(north_2018_swu),
                                           "longwave_down": to_1d(north_2018_lwd),
                                           "longwave_up": to_1d(north_2018_lwu),
                                           "sensible_heat_flux": to_1d(north_2018_shf),
                                           "latent_heat_flux": to_1d(north_2018_lhf),
                                           "surface_energy_balance": to_1d(north_2018_seb),
                                           "meltwater_runoff": to_1d(north_2018_mru)})

north_catchment_2019_df = pd.DataFrame({"time": to_1d(north_2019_time),
                                           "air_temp": to_1d(north_2019_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2019_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2019_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2019_swd),
                                           "shortwave_up": to_1d(north_2019_swu),
                                           "longwave_down": to_1d(north_2019_lwd),
                                           "longwave_up": to_1d(north_2019_lwu),
                                           "sensible_heat_flux": to_1d(north_2019_shf),
                                           "latent_heat_flux": to_1d(north_2019_lhf),
                                           "surface_energy_balance": to_1d(north_2019_seb),
                                           "meltwater_runoff": to_1d(north_2019_mru)})

north_catchment_2020_df = pd.DataFrame({"time": to_1d(north_2020_time),
                                           "air_temp": to_1d(north_2020_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2020_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2020_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2020_swd),
                                           "shortwave_up": to_1d(north_2020_swu),
                                           "longwave_down": to_1d(north_2020_lwd),
                                           "longwave_up": to_1d(north_2020_lwu),
                                           "sensible_heat_flux": to_1d(north_2020_shf),
                                           "latent_heat_flux": to_1d(north_2020_lhf),
                                           "surface_energy_balance": to_1d(north_2020_seb),
                                           "meltwater_runoff": to_1d(north_2020_mru)})

north_catchment_2021_df = pd.DataFrame({"time": to_1d(north_2021_time),
                                           "air_temp": to_1d(north_2021_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2021_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2021_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2021_swd),
                                           "shortwave_up": to_1d(north_2021_swu),
                                           "longwave_down": to_1d(north_2021_lwd),
                                           "longwave_up": to_1d(north_2021_lwu),
                                           "sensible_heat_flux": to_1d(north_2021_shf),
                                           "latent_heat_flux": to_1d(north_2021_lhf),
                                           "surface_energy_balance": to_1d(north_2021_seb),
                                           "meltwater_runoff": to_1d(north_2021_mru)})

north_catchment_2022_df = pd.DataFrame({"time": to_1d(north_2022_time),
                                           "air_temp": to_1d(north_2022_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2022_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2022_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2022_swd),
                                           "shortwave_up": to_1d(north_2022_swu),
                                           "longwave_down": to_1d(north_2022_lwd),
                                           "longwave_up": to_1d(north_2022_lwu),
                                           "sensible_heat_flux": to_1d(north_2022_shf),
                                           "latent_heat_flux": to_1d(north_2022_lhf),
                                           "surface_energy_balance": to_1d(north_2022_seb),
                                           "meltwater_runoff": to_1d(north_2022_mru)})

north_catchment_2023_df = pd.DataFrame({"time": to_1d(north_2023_time),
                                           "air_temp": to_1d(north_2023_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2023_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2023_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2023_swd),
                                           "shortwave_up": to_1d(north_2023_swu),
                                           "longwave_down": to_1d(north_2023_lwd),
                                           "longwave_up": to_1d(north_2023_lwu),
                                           "sensible_heat_flux": to_1d(north_2023_shf),
                                           "latent_heat_flux": to_1d(north_2023_lhf),
                                           "surface_energy_balance": to_1d(north_2023_seb),
                                           "meltwater_runoff": to_1d(north_2023_mru)})

north_catchment_2024_df = pd.DataFrame({"time": to_1d(north_2024_time),
                                           "air_temp": to_1d(north_2024_air_temp[:, 0]),
                                          "ice_temp": to_1d(north_2024_ice_temp[:, 0]),
                                           "albedo": to_1d(north_2024_albedo[:, 0]),
                                           "shortwave_down": to_1d(north_2024_swd),
                                           "shortwave_up": to_1d(north_2024_swu),
                                           "longwave_down": to_1d(north_2024_lwd),
                                           "longwave_up": to_1d(north_2024_lwu),
                                           "sensible_heat_flux": to_1d(north_2024_shf),
                                           "latent_heat_flux": to_1d(north_2024_lhf),
                                           "surface_energy_balance": to_1d(north_2024_seb),
                                           "meltwater_runoff": to_1d(north_2024_mru)})

north_catchment_2019_2020_df = pd.concat([north_catchment_2019_df,
                                          north_catchment_2020_df],
                                          ignore_index=True)

north_catchment_2000_2024_df = pd.concat([north_catchment_2000_df,
                                            north_catchment_2001_df,
                                            north_catchment_2002_df,
                                            north_catchment_2003_df,
                                            north_catchment_2004_df,
                                            north_catchment_2005_df,
                                            north_catchment_2006_df,
                                            north_catchment_2007_df,
                                            north_catchment_2008_df,
                                            north_catchment_2009_df,
                                            north_catchment_2010_df,
                                            north_catchment_2011_df,
                                            north_catchment_2012_df,
                                            north_catchment_2013_df,
                                            north_catchment_2014_df,
                                            north_catchment_2015_df,
                                            north_catchment_2016_df,
                                            north_catchment_2017_df,
                                            north_catchment_2018_df,
                                            north_catchment_2019_df,
                                            north_catchment_2020_df,
                                            north_catchment_2021_df,
                                            north_catchment_2022_df,
                                            north_catchment_2023_df,
                                            north_catchment_2024_df],
                                           ignore_index=True)

# Define output directory for Rio Behar
output_dir_rb = '/Users/mlm211/Documents/DeepMelt/catchment-scale/Rio_Behar_catchment_variables'
# Output directory on personal computer:
# output_dir_rb = '/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale/Rio_Behar_catchment_variables'

# Create the directory if it doesn't exist
os.makedirs(output_dir_rb, exist_ok=True)

# Define output directory for AK4
output_dir_ak4 = '/Users/mlm211/Documents/DeepMelt/catchment-scale/AK4_catchment_variables'
# Output directory on personal computer:
# output_dir_ak4 = '/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale/AK4_catchment_variables'

# Create the directory if it doesn't exist
os.makedirs(output_dir_ak4, exist_ok=True)

# Define output directory for Minturn
output_dir_minturn = '/Users/mlm211/Documents/DeepMelt/catchment-scale/Minturn_catchment_variables'
# Output directory on personal computer:
# output_dir_minturn = '/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale/Minturn_catchment_variables'

# Create the directory if it doesn't exist
os.makedirs(output_dir_minturn, exist_ok=True)

# Define output directory for North
output_dir_north = '/Users/mlm211/Documents/DeepMelt/catchment-scale/North_catchment_variables'
# Output directory on personal computer:
# output_dir_north = '/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/catchment-scale/North_catchment_variables'

# Create the directory if it doesn't exist
os.makedirs(output_dir_north, exist_ok=True)

# File name (with path) to save Rio Behar variables for each year
rb_catchment_file_name_2000 = os.path.join(
    output_dir_rb, "rb_catchment_2000_vars.csv")
rb_catchment_file_name_2001 = os.path.join(
    output_dir_rb, "rb_catchment_2001_vars.csv")
rb_catchment_file_name_2002 = os.path.join(
    output_dir_rb, "rb_catchment_2002_vars.csv")
rb_catchment_file_name_2003 = os.path.join(
    output_dir_rb, "rb_catchment_2003_vars.csv")
rb_catchment_file_name_2004 = os.path.join(
    output_dir_rb, "rb_catchment_2004_vars.csv")
rb_catchment_file_name_2005 = os.path.join(
    output_dir_rb, "rb_catchment_2005_vars.csv")
rb_catchment_file_name_2006 = os.path.join(
    output_dir_rb, "rb_catchment_2006_vars.csv")
rb_catchment_file_name_2007 = os.path.join(
    output_dir_rb, "rb_catchment_2007_vars.csv")
rb_catchment_file_name_2008 = os.path.join(
    output_dir_rb, "rb_catchment_2008_vars.csv")
rb_catchment_file_name_2009 = os.path.join(
    output_dir_rb, "rb_catchment_2009_vars.csv")
rb_catchment_file_name_2010 = os.path.join(
    output_dir_rb, "rb_catchment_2010_vars.csv")
rb_catchment_file_name_2011 = os.path.join(
    output_dir_rb, "rb_catchment_2011_vars.csv")
rb_catchment_file_name_2012 = os.path.join(
    output_dir_rb, "rb_catchment_2012_vars.csv")
rb_catchment_file_name_2013 = os.path.join(
    output_dir_rb, "rb_catchment_2013_vars.csv")
rb_catchment_file_name_2014 = os.path.join(
    output_dir_rb, "rb_catchment_2014_vars.csv")
rb_catchment_file_name_2015 = os.path.join(
    output_dir_rb, "rb_catchment_2015_vars.csv")
rb_catchment_file_name_2016 = os.path.join(
    output_dir_rb, "rb_catchment_2016_vars.csv")
rb_catchment_file_name_2017 = os.path.join(
    output_dir_rb, "rb_catchment_2017_vars.csv")
rb_catchment_file_name_2018 = os.path.join(
    output_dir_rb, "rb_catchment_2018_vars.csv")
rb_catchment_file_name_2019 = os.path.join(
    output_dir_rb, "rb_catchment_2019_vars.csv")
rb_catchment_file_name_2020 = os.path.join(
    output_dir_rb, "rb_catchment_2020_vars.csv")
rb_catchment_file_name_2021 = os.path.join(
    output_dir_rb, "rb_catchment_2021_vars.csv")
rb_catchment_file_name_2022 = os.path.join(
    output_dir_rb, "rb_catchment_2022_vars.csv")
rb_catchment_file_name_2023 = os.path.join(
    output_dir_rb, "rb_catchment_2023_vars.csv")
rb_catchment_file_name_2024 = os.path.join(
    output_dir_rb, "rb_catchment_2024_vars.csv")
rb_catchment_file_name_2000_2024 = os.path.join(
    output_dir_rb, "rb_catchment_2000_2024_vars.csv")

# File name (with path) to save AK4 variables for each year
ak4_catchment_file_name_2000 = os.path.join(
    output_dir_ak4, "ak4_catchment_2000_vars.csv")
ak4_catchment_file_name_2001 = os.path.join(
    output_dir_ak4, "ak4_catchment_2001_vars.csv")
ak4_catchment_file_name_2002 = os.path.join(
    output_dir_ak4, "ak4_catchment_2002_vars.csv")
ak4_catchment_file_name_2003 = os.path.join(
    output_dir_ak4, "ak4_catchment_2003_vars.csv")
ak4_catchment_file_name_2004 = os.path.join(
    output_dir_ak4, "ak4_catchment_2004_vars.csv")
ak4_catchment_file_name_2005 = os.path.join(
    output_dir_ak4, "ak4_catchment_2005_vars.csv")
ak4_catchment_file_name_2006 = os.path.join(
    output_dir_ak4, "ak4_catchment_2006_vars.csv")
ak4_catchment_file_name_2007 = os.path.join(
    output_dir_ak4, "ak4_catchment_2007_vars.csv")
ak4_catchment_file_name_2008 = os.path.join(
    output_dir_ak4, "ak4_catchment_2008_vars.csv")
ak4_catchment_file_name_2009 = os.path.join(
    output_dir_ak4, "ak4_catchment_2009_vars.csv")
ak4_catchment_file_name_2010 = os.path.join(
    output_dir_ak4, "ak4_catchment_2010_vars.csv")
ak4_catchment_file_name_2011 = os.path.join(
    output_dir_ak4, "ak4_catchment_2011_vars.csv")
ak4_catchment_file_name_2012 = os.path.join(
    output_dir_ak4, "ak4_catchment_2012_vars.csv")
ak4_catchment_file_name_2013 = os.path.join(
    output_dir_ak4, "ak4_catchment_2013_vars.csv")
ak4_catchment_file_name_2014 = os.path.join(
    output_dir_ak4, "ak4_catchment_2014_vars.csv")
ak4_catchment_file_name_2015 = os.path.join(
    output_dir_ak4, "ak4_catchment_2015_vars.csv")
ak4_catchment_file_name_2016 = os.path.join(
    output_dir_ak4, "ak4_catchment_2016_vars.csv")
ak4_catchment_file_name_2017 = os.path.join(
    output_dir_ak4, "ak4_catchment_2017_vars.csv")
ak4_catchment_file_name_2018 = os.path.join(
    output_dir_ak4, "ak4_catchment_2018_vars.csv")
ak4_catchment_file_name_2019 = os.path.join(
    output_dir_ak4, "ak4_catchment_2019_vars.csv")
ak4_catchment_file_name_2020 = os.path.join(
    output_dir_ak4, "ak4_catchment_2020_vars.csv")
ak4_catchment_file_name_2021 = os.path.join(
    output_dir_ak4, "ak4_catchment_2021_vars.csv")
ak4_catchment_file_name_2022 = os.path.join(
    output_dir_ak4, "ak4_catchment_2022_vars.csv")
ak4_catchment_file_name_2023 = os.path.join(
    output_dir_ak4, "ak4_catchment_2023_vars.csv")
ak4_catchment_file_name_2024 = os.path.join(
    output_dir_ak4, "ak4_catchment_2024_vars.csv")
ak4_catchment_file_name_2008_2016 = os.path.join(
    output_dir_ak4, "ak4_catchment_2008_2016_vars.csv")
ak4_catchment_file_name_2000_2024 = os.path.join(
    output_dir_ak4, "ak4_catchment_2000_2024_vars.csv")

# File name (with path) to save Minturn variables for each year
minturn_catchment_file_name_2000 = os.path.join(
    output_dir_minturn, "minturn_catchment_2000_vars.csv")
minturn_catchment_file_name_2001 = os.path.join(
    output_dir_minturn, "minturn_catchment_2001_vars.csv")
minturn_catchment_file_name_2002 = os.path.join(
    output_dir_minturn, "minturn_catchment_2002_vars.csv")
minturn_catchment_file_name_2003 = os.path.join(
    output_dir_minturn, "minturn_catchment_2003_vars.csv")
minturn_catchment_file_name_2004 = os.path.join(
    output_dir_minturn, "minturn_catchment_2004_vars.csv")
minturn_catchment_file_name_2005 = os.path.join(
    output_dir_minturn, "minturn_catchment_2005_vars.csv")
minturn_catchment_file_name_2006 = os.path.join(
    output_dir_minturn, "minturn_catchment_2006_vars.csv")
minturn_catchment_file_name_2007 = os.path.join(
    output_dir_minturn, "minturn_catchment_2007_vars.csv")
minturn_catchment_file_name_2008 = os.path.join(
    output_dir_minturn, "minturn_catchment_2008_vars.csv")
minturn_catchment_file_name_2009 = os.path.join(
    output_dir_minturn, "minturn_catchment_2009_vars.csv")
minturn_catchment_file_name_2010 = os.path.join(
    output_dir_minturn, "minturn_catchment_2010_vars.csv")
minturn_catchment_file_name_2011 = os.path.join(
    output_dir_minturn, "minturn_catchment_2011_vars.csv")
minturn_catchment_file_name_2012 = os.path.join(
    output_dir_minturn, "minturn_catchment_2012_vars.csv")
minturn_catchment_file_name_2013 = os.path.join(
    output_dir_minturn, "minturn_catchment_2013_vars.csv")
minturn_catchment_file_name_2014 = os.path.join(
    output_dir_minturn, "minturn_catchment_2014_vars.csv")
minturn_catchment_file_name_2015 = os.path.join(
    output_dir_minturn, "minturn_catchment_2015_vars.csv")
minturn_catchment_file_name_2016 = os.path.join(
    output_dir_minturn, "minturn_catchment_2016_vars.csv")
minturn_catchment_file_name_2017 = os.path.join(
    output_dir_minturn, "minturn_catchment_2017_vars.csv")
minturn_catchment_file_name_2018 = os.path.join(
    output_dir_minturn, "minturn_catchment_2018_vars.csv")
minturn_catchment_file_name_2019 = os.path.join(
    output_dir_minturn, "minturn_catchment_2019_vars.csv")
minturn_catchment_file_name_2020 = os.path.join(
    output_dir_minturn, "minturn_catchment_2020_vars.csv")
minturn_catchment_file_name_2021 = os.path.join(
    output_dir_minturn, "minturn_catchment_2021_vars.csv")
minturn_catchment_file_name_2022 = os.path.join(
    output_dir_minturn, "minturn_catchment_2022_vars.csv")
minturn_catchment_file_name_2023 = os.path.join(
    output_dir_minturn, "minturn_catchment_2023_vars.csv")
minturn_catchment_file_name_2024 = os.path.join(
    output_dir_minturn, "minturn_catchment_2024_vars.csv")
minturn_catchment_file_name_2019_2020 = os.path.join(
    output_dir_minturn, "minturn_catchment_2019_2020_vars.csv")
minturn_catchment_file_name_2000_2024 = os.path.join(
    output_dir_minturn, "minturn_catchment_2000_2024_vars.csv")


# File name (with path) to save North variables for each year
north_catchment_file_name_2000 = os.path.join(
    output_dir_north, "north_catchment_2000_vars.csv")
north_catchment_file_name_2001 = os.path.join(
    output_dir_north, "north_catchment_2001_vars.csv")
north_catchment_file_name_2002 = os.path.join(
    output_dir_north, "north_catchment_2002_vars.csv")
north_catchment_file_name_2003 = os.path.join(
    output_dir_north, "north_catchment_2003_vars.csv")
north_catchment_file_name_2004 = os.path.join(
    output_dir_north, "north_catchment_2004_vars.csv")
north_catchment_file_name_2005 = os.path.join(
    output_dir_north, "north_catchment_2005_vars.csv")
north_catchment_file_name_2006 = os.path.join(
    output_dir_north, "north_catchment_2006_vars.csv")
north_catchment_file_name_2007 = os.path.join(
    output_dir_north, "north_catchment_2007_vars.csv")
north_catchment_file_name_2008 = os.path.join(
    output_dir_north, "north_catchment_2008_vars.csv")
north_catchment_file_name_2009 = os.path.join(
    output_dir_north, "north_catchment_2009_vars.csv")
north_catchment_file_name_2010 = os.path.join(
    output_dir_north, "north_catchment_2010_vars.csv")
north_catchment_file_name_2011 = os.path.join(
    output_dir_north, "north_catchment_2011_vars.csv")
north_catchment_file_name_2012 = os.path.join(
    output_dir_north, "north_catchment_2012_vars.csv")
north_catchment_file_name_2013 = os.path.join(
    output_dir_north, "north_catchment_2013_vars.csv")
north_catchment_file_name_2014 = os.path.join(
    output_dir_north, "north_catchment_2014_vars.csv")
north_catchment_file_name_2015 = os.path.join(
    output_dir_north, "north_catchment_2015_vars.csv")
north_catchment_file_name_2016 = os.path.join(
    output_dir_north, "north_catchment_2016_vars.csv")
north_catchment_file_name_2017 = os.path.join(
    output_dir_north, "north_catchment_2017_vars.csv")
north_catchment_file_name_2018 = os.path.join(
    output_dir_north, "north_catchment_2018_vars.csv")
north_catchment_file_name_2019 = os.path.join(
    output_dir_north, "north_catchment_2019_vars.csv")
north_catchment_file_name_2020 = os.path.join(
    output_dir_north, "north_catchment_2020_vars.csv")
north_catchment_file_name_2021 = os.path.join(
    output_dir_north, "north_catchment_2021_vars.csv")
north_catchment_file_name_2022 = os.path.join(
    output_dir_north, "north_catchment_2022_vars.csv")
north_catchment_file_name_2023 = os.path.join(
    output_dir_north, "north_catchment_2023_vars.csv")
north_catchment_file_name_2024 = os.path.join(
    output_dir_north, "north_catchment_2024_vars.csv")
north_catchment_file_name_2019_2020 = os.path.join(
    output_dir_north, "north_catchment_2019_2020_vars.csv")
north_catchment_file_name_2000_2024 = os.path.join(
    output_dir_north, "north_catchment_2000_2024_vars.csv")


# Delete old Rio Behar csv files if they already exist
if os.path.exists(rb_catchment_file_name_2000):
    os.remove(rb_catchment_file_name_2000)
if os.path.exists(rb_catchment_file_name_2001):
    os.remove(rb_catchment_file_name_2001)
if os.path.exists(rb_catchment_file_name_2002):
    os.remove(rb_catchment_file_name_2002)
if os.path.exists(rb_catchment_file_name_2003):
    os.remove(rb_catchment_file_name_2003)
if os.path.exists(rb_catchment_file_name_2004):
    os.remove(rb_catchment_file_name_2004)
if os.path.exists(rb_catchment_file_name_2005):
    os.remove(rb_catchment_file_name_2005)
if os.path.exists(rb_catchment_file_name_2006):
    os.remove(rb_catchment_file_name_2006)
if os.path.exists(rb_catchment_file_name_2007):
    os.remove(rb_catchment_file_name_2007)
if os.path.exists(rb_catchment_file_name_2008):
    os.remove(rb_catchment_file_name_2008)
if os.path.exists(rb_catchment_file_name_2009):
    os.remove(rb_catchment_file_name_2009)
if os.path.exists(rb_catchment_file_name_2010):
    os.remove(rb_catchment_file_name_2010)
if os.path.exists(rb_catchment_file_name_2011):
    os.remove(rb_catchment_file_name_2011)
if os.path.exists(rb_catchment_file_name_2012):
    os.remove(rb_catchment_file_name_2012)
if os.path.exists(rb_catchment_file_name_2013):
    os.remove(rb_catchment_file_name_2013)
if os.path.exists(rb_catchment_file_name_2014):
    os.remove(rb_catchment_file_name_2014)
if os.path.exists(rb_catchment_file_name_2015):
    os.remove(rb_catchment_file_name_2015)
if os.path.exists(rb_catchment_file_name_2016):
    os.remove(rb_catchment_file_name_2016)
if os.path.exists(rb_catchment_file_name_2017):
    os.remove(rb_catchment_file_name_2017)
if os.path.exists(rb_catchment_file_name_2018):
    os.remove(rb_catchment_file_name_2018)
if os.path.exists(rb_catchment_file_name_2019):
    os.remove(rb_catchment_file_name_2019)
if os.path.exists(rb_catchment_file_name_2020):
    os.remove(rb_catchment_file_name_2020)
if os.path.exists(rb_catchment_file_name_2021):
    os.remove(rb_catchment_file_name_2021)
if os.path.exists(rb_catchment_file_name_2022):
    os.remove(rb_catchment_file_name_2022)
if os.path.exists(rb_catchment_file_name_2023):
    os.remove(rb_catchment_file_name_2023)
if os.path.exists(rb_catchment_file_name_2024):
    os.remove(rb_catchment_file_name_2024)
if os.path.exists(rb_catchment_file_name_2000_2024):
    os.remove(rb_catchment_file_name_2000_2024)

# Delete old AK4 csv files if they already exist
if os.path.exists(ak4_catchment_file_name_2000):
    os.remove(ak4_catchment_file_name_2000)
if os.path.exists(ak4_catchment_file_name_2001):
    os.remove(ak4_catchment_file_name_2001)
if os.path.exists(ak4_catchment_file_name_2002):
    os.remove(ak4_catchment_file_name_2002)
if os.path.exists(ak4_catchment_file_name_2003):
    os.remove(ak4_catchment_file_name_2003)
if os.path.exists(ak4_catchment_file_name_2004):
    os.remove(ak4_catchment_file_name_2004)
if os.path.exists(ak4_catchment_file_name_2005):
    os.remove(ak4_catchment_file_name_2005)
if os.path.exists(ak4_catchment_file_name_2006):
    os.remove(ak4_catchment_file_name_2006)
if os.path.exists(ak4_catchment_file_name_2007):
    os.remove(ak4_catchment_file_name_2007)
if os.path.exists(ak4_catchment_file_name_2008):
    os.remove(ak4_catchment_file_name_2008)
if os.path.exists(ak4_catchment_file_name_2009):
    os.remove(ak4_catchment_file_name_2009)
if os.path.exists(ak4_catchment_file_name_2010):
    os.remove(ak4_catchment_file_name_2010)
if os.path.exists(ak4_catchment_file_name_2011):
    os.remove(ak4_catchment_file_name_2011)
if os.path.exists(ak4_catchment_file_name_2012):
    os.remove(ak4_catchment_file_name_2012)
if os.path.exists(ak4_catchment_file_name_2013):
    os.remove(ak4_catchment_file_name_2013)
if os.path.exists(ak4_catchment_file_name_2014):
    os.remove(ak4_catchment_file_name_2014)
if os.path.exists(ak4_catchment_file_name_2015):
    os.remove(ak4_catchment_file_name_2015)
if os.path.exists(ak4_catchment_file_name_2016):
    os.remove(ak4_catchment_file_name_2016)
if os.path.exists(ak4_catchment_file_name_2017):
    os.remove(ak4_catchment_file_name_2017)
if os.path.exists(ak4_catchment_file_name_2018):
    os.remove(ak4_catchment_file_name_2018)
if os.path.exists(ak4_catchment_file_name_2019):
    os.remove(ak4_catchment_file_name_2019)
if os.path.exists(ak4_catchment_file_name_2020):
    os.remove(ak4_catchment_file_name_2020)
if os.path.exists(ak4_catchment_file_name_2021):
    os.remove(ak4_catchment_file_name_2021)
if os.path.exists(ak4_catchment_file_name_2022):
    os.remove(ak4_catchment_file_name_2022)
if os.path.exists(ak4_catchment_file_name_2023):
    os.remove(ak4_catchment_file_name_2023)
if os.path.exists(ak4_catchment_file_name_2024):
    os.remove(ak4_catchment_file_name_2024)   
if os.path.exists(ak4_catchment_file_name_2008_2016):
    os.remove(ak4_catchment_file_name_2008_2016)
if os.path.exists(ak4_catchment_file_name_2000_2024):
    os.remove(ak4_catchment_file_name_2000_2024)

    # Delete old Minturn csv files if they already exist
if os.path.exists(minturn_catchment_file_name_2000):
    os.remove(minturn_catchment_file_name_2000)
if os.path.exists(minturn_catchment_file_name_2001):
    os.remove(minturn_catchment_file_name_2001)
if os.path.exists(minturn_catchment_file_name_2002):
    os.remove(minturn_catchment_file_name_2002)
if os.path.exists(minturn_catchment_file_name_2003):
    os.remove(minturn_catchment_file_name_2003)
if os.path.exists(minturn_catchment_file_name_2004):
    os.remove(minturn_catchment_file_name_2004)
if os.path.exists(minturn_catchment_file_name_2005):
    os.remove(minturn_catchment_file_name_2005)
if os.path.exists(minturn_catchment_file_name_2006):
    os.remove(minturn_catchment_file_name_2006)
if os.path.exists(minturn_catchment_file_name_2007):
    os.remove(minturn_catchment_file_name_2007)
if os.path.exists(minturn_catchment_file_name_2008):
    os.remove(minturn_catchment_file_name_2008)
if os.path.exists(minturn_catchment_file_name_2009):
    os.remove(minturn_catchment_file_name_2009)
if os.path.exists(minturn_catchment_file_name_2010):
    os.remove(minturn_catchment_file_name_2010)
if os.path.exists(minturn_catchment_file_name_2011):
    os.remove(minturn_catchment_file_name_2011)
if os.path.exists(minturn_catchment_file_name_2012):
    os.remove(minturn_catchment_file_name_2012)
if os.path.exists(minturn_catchment_file_name_2013):
    os.remove(minturn_catchment_file_name_2013)
if os.path.exists(minturn_catchment_file_name_2014):
    os.remove(minturn_catchment_file_name_2014)
if os.path.exists(minturn_catchment_file_name_2015):
    os.remove(minturn_catchment_file_name_2015)
if os.path.exists(minturn_catchment_file_name_2016):
    os.remove(minturn_catchment_file_name_2016)
if os.path.exists(minturn_catchment_file_name_2017):
    os.remove(minturn_catchment_file_name_2017)
if os.path.exists(minturn_catchment_file_name_2018):
    os.remove(minturn_catchment_file_name_2018)
if os.path.exists(minturn_catchment_file_name_2019):
    os.remove(minturn_catchment_file_name_2019)
if os.path.exists(minturn_catchment_file_name_2020):
    os.remove(minturn_catchment_file_name_2020)
if os.path.exists(minturn_catchment_file_name_2021):
    os.remove(minturn_catchment_file_name_2021)
if os.path.exists(minturn_catchment_file_name_2022):
    os.remove(minturn_catchment_file_name_2022)
if os.path.exists(minturn_catchment_file_name_2023):
    os.remove(minturn_catchment_file_name_2023)
if os.path.exists(minturn_catchment_file_name_2024):
    os.remove(minturn_catchment_file_name_2024)
if os.path.exists(minturn_catchment_file_name_2019_2020):
    os.remove(minturn_catchment_file_name_2019_2020)
if os.path.exists(minturn_catchment_file_name_2000_2024):
    os.remove(minturn_catchment_file_name_2000_2024)
    
# Delete old North csv files if they already exist
if os.path.exists(north_catchment_file_name_2000):
    os.remove(north_catchment_file_name_2000)
if os.path.exists(north_catchment_file_name_2001):
    os.remove(north_catchment_file_name_2001)
if os.path.exists(north_catchment_file_name_2002):
    os.remove(north_catchment_file_name_2002)
if os.path.exists(north_catchment_file_name_2003):
    os.remove(north_catchment_file_name_2003)
if os.path.exists(north_catchment_file_name_2004):
    os.remove(north_catchment_file_name_2004)
if os.path.exists(north_catchment_file_name_2005):
    os.remove(north_catchment_file_name_2005)
if os.path.exists(north_catchment_file_name_2006):
    os.remove(north_catchment_file_name_2006)
if os.path.exists(north_catchment_file_name_2007):
    os.remove(north_catchment_file_name_2007)
if os.path.exists(north_catchment_file_name_2008):
    os.remove(north_catchment_file_name_2008)
if os.path.exists(north_catchment_file_name_2009):
    os.remove(north_catchment_file_name_2009)
if os.path.exists(north_catchment_file_name_2010):
    os.remove(north_catchment_file_name_2010)
if os.path.exists(north_catchment_file_name_2011):
    os.remove(north_catchment_file_name_2011)
if os.path.exists(north_catchment_file_name_2012):
    os.remove(north_catchment_file_name_2012)
if os.path.exists(north_catchment_file_name_2013):
    os.remove(north_catchment_file_name_2013)
if os.path.exists(north_catchment_file_name_2014):
    os.remove(north_catchment_file_name_2014)
if os.path.exists(north_catchment_file_name_2015):
    os.remove(north_catchment_file_name_2015)
if os.path.exists(north_catchment_file_name_2016):
    os.remove(north_catchment_file_name_2016)
if os.path.exists(north_catchment_file_name_2017):
    os.remove(north_catchment_file_name_2017)
if os.path.exists(north_catchment_file_name_2018):
    os.remove(north_catchment_file_name_2018)
if os.path.exists(north_catchment_file_name_2019):
    os.remove(north_catchment_file_name_2019)
if os.path.exists(north_catchment_file_name_2020):
    os.remove(north_catchment_file_name_2020)
if os.path.exists(north_catchment_file_name_2021):
    os.remove(north_catchment_file_name_2021)
if os.path.exists(north_catchment_file_name_2022):
    os.remove(north_catchment_file_name_2022)
if os.path.exists(north_catchment_file_name_2023):
    os.remove(north_catchment_file_name_2023)
if os.path.exists(north_catchment_file_name_2024):
    os.remove(north_catchment_file_name_2024)
if os.path.exists(north_catchment_file_name_2019_2020):
    os.remove(north_catchment_file_name_2019_2020)
if os.path.exists(north_catchment_file_name_2000_2024):
    os.remove(north_catchment_file_name_2000_2024)


# Save Rio Behar data to csv
rb_catchment_2000_df.to_csv(rb_catchment_file_name_2000, index=False)
rb_catchment_2001_df.to_csv(rb_catchment_file_name_2001, index=False)
rb_catchment_2002_df.to_csv(rb_catchment_file_name_2002, index=False)
rb_catchment_2003_df.to_csv(rb_catchment_file_name_2003, index=False)
rb_catchment_2004_df.to_csv(rb_catchment_file_name_2004, index=False)
rb_catchment_2005_df.to_csv(rb_catchment_file_name_2005, index=False)
rb_catchment_2006_df.to_csv(rb_catchment_file_name_2006, index=False)
rb_catchment_2007_df.to_csv(rb_catchment_file_name_2007, index=False)
rb_catchment_2008_df.to_csv(rb_catchment_file_name_2008, index=False)
rb_catchment_2009_df.to_csv(rb_catchment_file_name_2009, index=False)
rb_catchment_2010_df.to_csv(rb_catchment_file_name_2010, index=False)
rb_catchment_2011_df.to_csv(rb_catchment_file_name_2011, index=False)
rb_catchment_2012_df.to_csv(rb_catchment_file_name_2012, index=False)
rb_catchment_2013_df.to_csv(rb_catchment_file_name_2013, index=False)
rb_catchment_2014_df.to_csv(rb_catchment_file_name_2014, index=False)
rb_catchment_2015_df.to_csv(rb_catchment_file_name_2015, index=False)
rb_catchment_2016_df.to_csv(rb_catchment_file_name_2016, index=False)
rb_catchment_2017_df.to_csv(rb_catchment_file_name_2017, index=False)
rb_catchment_2018_df.to_csv(rb_catchment_file_name_2018, index=False)
rb_catchment_2019_df.to_csv(rb_catchment_file_name_2019, index=False)
rb_catchment_2020_df.to_csv(rb_catchment_file_name_2020, index=False)
rb_catchment_2021_df.to_csv(rb_catchment_file_name_2021, index=False)
rb_catchment_2022_df.to_csv(rb_catchment_file_name_2022, index=False)
rb_catchment_2023_df.to_csv(rb_catchment_file_name_2023, index=False)
rb_catchment_2024_df.to_csv(rb_catchment_file_name_2024, index=False)
rb_catchment_2000_2024_df.to_csv(rb_catchment_file_name_2000_2024, index=False)

# Save AK4 data to csv
ak4_catchment_2000_df.to_csv(ak4_catchment_file_name_2000, index=False)
ak4_catchment_2001_df.to_csv(ak4_catchment_file_name_2001, index=False)
ak4_catchment_2002_df.to_csv(ak4_catchment_file_name_2002, index=False)
ak4_catchment_2003_df.to_csv(ak4_catchment_file_name_2003, index=False)
ak4_catchment_2004_df.to_csv(ak4_catchment_file_name_2004, index=False)
ak4_catchment_2005_df.to_csv(ak4_catchment_file_name_2005, index=False)
ak4_catchment_2006_df.to_csv(ak4_catchment_file_name_2006, index=False)
ak4_catchment_2007_df.to_csv(ak4_catchment_file_name_2007, index=False)
ak4_catchment_2008_df.to_csv(ak4_catchment_file_name_2008, index=False)
ak4_catchment_2009_df.to_csv(ak4_catchment_file_name_2009, index=False)
ak4_catchment_2010_df.to_csv(ak4_catchment_file_name_2010, index=False)
ak4_catchment_2011_df.to_csv(ak4_catchment_file_name_2011, index=False)
ak4_catchment_2012_df.to_csv(ak4_catchment_file_name_2012, index=False)
ak4_catchment_2013_df.to_csv(ak4_catchment_file_name_2013, index=False)
ak4_catchment_2014_df.to_csv(ak4_catchment_file_name_2014, index=False)
ak4_catchment_2015_df.to_csv(ak4_catchment_file_name_2015, index=False)
ak4_catchment_2016_df.to_csv(ak4_catchment_file_name_2016, index=False)
ak4_catchment_2017_df.to_csv(ak4_catchment_file_name_2017, index=False)
ak4_catchment_2018_df.to_csv(ak4_catchment_file_name_2018, index=False)
ak4_catchment_2019_df.to_csv(ak4_catchment_file_name_2019, index=False)
ak4_catchment_2020_df.to_csv(ak4_catchment_file_name_2020, index=False)
ak4_catchment_2021_df.to_csv(ak4_catchment_file_name_2021, index=False)
ak4_catchment_2022_df.to_csv(ak4_catchment_file_name_2022, index=False)
ak4_catchment_2023_df.to_csv(ak4_catchment_file_name_2023, index=False)
ak4_catchment_2024_df.to_csv(ak4_catchment_file_name_2024, index=False)
ak4_catchment_2008_2016_df.to_csv(ak4_catchment_file_name_2008_2016, index=False)
ak4_catchment_2000_2024_df.to_csv(ak4_catchment_file_name_2000_2024, index=False)


# Save Minturn data to csv
minturn_catchment_2000_df.to_csv(minturn_catchment_file_name_2000, index=False)
minturn_catchment_2001_df.to_csv(minturn_catchment_file_name_2001, index=False)
minturn_catchment_2002_df.to_csv(minturn_catchment_file_name_2002, index=False)
minturn_catchment_2003_df.to_csv(minturn_catchment_file_name_2003, index=False)
minturn_catchment_2004_df.to_csv(minturn_catchment_file_name_2004, index=False)
minturn_catchment_2005_df.to_csv(minturn_catchment_file_name_2005, index=False)
minturn_catchment_2006_df.to_csv(minturn_catchment_file_name_2006, index=False)
minturn_catchment_2007_df.to_csv(minturn_catchment_file_name_2007, index=False)
minturn_catchment_2008_df.to_csv(minturn_catchment_file_name_2008, index=False)
minturn_catchment_2009_df.to_csv(minturn_catchment_file_name_2009, index=False)
minturn_catchment_2010_df.to_csv(minturn_catchment_file_name_2010, index=False)
minturn_catchment_2011_df.to_csv(minturn_catchment_file_name_2011, index=False)
minturn_catchment_2012_df.to_csv(minturn_catchment_file_name_2012, index=False)
minturn_catchment_2013_df.to_csv(minturn_catchment_file_name_2013, index=False)
minturn_catchment_2014_df.to_csv(minturn_catchment_file_name_2014, index=False)
minturn_catchment_2015_df.to_csv(minturn_catchment_file_name_2015, index=False)
minturn_catchment_2016_df.to_csv(minturn_catchment_file_name_2016, index=False)
minturn_catchment_2017_df.to_csv(minturn_catchment_file_name_2017, index=False)
minturn_catchment_2018_df.to_csv(minturn_catchment_file_name_2018, index=False)
minturn_catchment_2019_df.to_csv(minturn_catchment_file_name_2019, index=False)
minturn_catchment_2020_df.to_csv(minturn_catchment_file_name_2020, index=False)
minturn_catchment_2021_df.to_csv(minturn_catchment_file_name_2021, index=False)
minturn_catchment_2022_df.to_csv(minturn_catchment_file_name_2022, index=False)
minturn_catchment_2023_df.to_csv(minturn_catchment_file_name_2023, index=False)
minturn_catchment_2024_df.to_csv(minturn_catchment_file_name_2024, index=False)
minturn_catchment_2019_2020_df.to_csv(minturn_catchment_file_name_2019_2020, index=False)
minturn_catchment_2000_2024_df.to_csv(minturn_catchment_file_name_2000_2024, index=False)


# Save North data to csv
north_catchment_2000_df.to_csv(north_catchment_file_name_2000, index=False)
north_catchment_2001_df.to_csv(north_catchment_file_name_2001, index=False)
north_catchment_2002_df.to_csv(north_catchment_file_name_2002, index=False)
north_catchment_2003_df.to_csv(north_catchment_file_name_2003, index=False)
north_catchment_2004_df.to_csv(north_catchment_file_name_2004, index=False)
north_catchment_2005_df.to_csv(north_catchment_file_name_2005, index=False)
north_catchment_2006_df.to_csv(north_catchment_file_name_2006, index=False)
north_catchment_2007_df.to_csv(north_catchment_file_name_2007, index=False)
north_catchment_2008_df.to_csv(north_catchment_file_name_2008, index=False)
north_catchment_2009_df.to_csv(north_catchment_file_name_2009, index=False)
north_catchment_2010_df.to_csv(north_catchment_file_name_2010, index=False)
north_catchment_2011_df.to_csv(north_catchment_file_name_2011, index=False)
north_catchment_2012_df.to_csv(north_catchment_file_name_2012, index=False)
north_catchment_2013_df.to_csv(north_catchment_file_name_2013, index=False)
north_catchment_2014_df.to_csv(north_catchment_file_name_2014, index=False)
north_catchment_2015_df.to_csv(north_catchment_file_name_2015, index=False)
north_catchment_2016_df.to_csv(north_catchment_file_name_2016, index=False)
north_catchment_2017_df.to_csv(north_catchment_file_name_2017, index=False)
north_catchment_2018_df.to_csv(north_catchment_file_name_2018, index=False)
north_catchment_2019_df.to_csv(north_catchment_file_name_2019, index=False)
north_catchment_2020_df.to_csv(north_catchment_file_name_2020, index=False)
north_catchment_2021_df.to_csv(north_catchment_file_name_2021, index=False)
north_catchment_2022_df.to_csv(north_catchment_file_name_2022, index=False)
north_catchment_2023_df.to_csv(north_catchment_file_name_2023, index=False)
north_catchment_2024_df.to_csv(north_catchment_file_name_2024, index=False)
north_catchment_2019_2020_df.to_csv(north_catchment_file_name_2019_2020, index=False)
north_catchment_2000_2024_df.to_csv(north_catchment_file_name_2000_2024, index=False)
