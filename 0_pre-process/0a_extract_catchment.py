# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 09:56:25 2026

@author: mayam

Extract Rio Behar, AK4, and Minturn catchments from MAR version 3.14
to prepare for further analysis.
"""

import os
import xarray as xr
import geopandas as gpd
import rioxarray as rio
import numpy as np
from shapely.geometry import box
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.collections import PatchCollection


# Set working directory
os.chdir('/Users/mlm211/Documents/DeepMelt/MAR_files')
# Working directory on personal computer:
# os.chdir('/Users/mayam/OneDrive/Documents/Duke University/DeepMelt/MAR_2000_2021')


# Open MAR files for each year
mar_2000 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2000.nc')
mar_2001 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2001.nc')
mar_2002 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2002.nc')
mar_2003 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2003.nc')
mar_2004 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2004.nc')
mar_2005 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2005.nc')
mar_2006 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2006.nc')
mar_2007 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2007.nc')
mar_2008 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2008.nc')
mar_2009 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2009.nc')
mar_2010 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2010.nc')
mar_2011 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2011.nc')
mar_2012 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2012.nc')
mar_2013 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2013.nc')
mar_2014 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2014.nc')
mar_2015 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2015.nc')
mar_2016 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2016.nc')
mar_2017 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2017.nc')
mar_2018 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2018.nc')
mar_2019 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2019.nc')
mar_2020 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2020.nc')
mar_2021 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2021.nc')
mar_2022 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2022.nc')
mar_2023 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2023.nc')
mar_2024 = xr.open_dataset('MARv3.14.3-10km-daily-ERA5-2024.nc')

def spatial_mar(ds):
    ds = ds.drop_vars(
        [v for v in ds.data_vars if v.lower() in ["lon", "lat"]],
        errors="ignore"
    )

    ds = ds.drop_vars(
        [v for v in ds.data_vars if v.endswith("_bnds")],
        errors="ignore"
    )

    ds = ds.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)

    return ds


mar_2000 = spatial_mar(mar_2000)
mar_2001 = spatial_mar(mar_2001)
mar_2002 = spatial_mar(mar_2002)
mar_2003 = spatial_mar(mar_2003)
mar_2004 = spatial_mar(mar_2004)
mar_2005 = spatial_mar(mar_2005)
mar_2006 = spatial_mar(mar_2006)
mar_2007 = spatial_mar(mar_2007)
mar_2008 = spatial_mar(mar_2008)
mar_2009 = spatial_mar(mar_2009)
mar_2010 = spatial_mar(mar_2010)
mar_2011 = spatial_mar(mar_2011)
mar_2012 = spatial_mar(mar_2012)
mar_2013 = spatial_mar(mar_2013)
mar_2014 = spatial_mar(mar_2014)
mar_2015 = spatial_mar(mar_2015)
mar_2016 = spatial_mar(mar_2016)
mar_2017 = spatial_mar(mar_2017)
mar_2018 = spatial_mar(mar_2018)
mar_2019 = spatial_mar(mar_2019)
mar_2020 = spatial_mar(mar_2020)
mar_2021 = spatial_mar(mar_2021)
mar_2022 = spatial_mar(mar_2022)
mar_2023 = spatial_mar(mar_2023)
mar_2024 = spatial_mar(mar_2024)

# Open Rio Behar catchment delineation
rio_behar_catchment = gpd.read_file(
    '/Users/mlm211/Documents/DeepMelt/catchment_delineations/rio_behar_basin_delineation.shp')

# Open AK4 catchment delineation
ak4_catchment = gpd.read_file(
    '/Users/mlm211/Documents/DeepMelt/catchment_delineations/AK4_basin_delineation.shp')

# Open Minturn catchment delineation
minturn_catchment = gpd.read_file(
    '/Users/mlm211/Documents/DeepMelt/catchment_delineations/minturn_basin.shp')

# Convert MAR coordinates from km to meters for each year
mar_2000 = mar_2000.assign_coords(
    {"x": mar_2000["x"] * 1000, "y": mar_2000["y"] * 1000, })
mar_2001 = mar_2001.assign_coords(
    {"x": mar_2001["x"] * 1000, "y": mar_2001["y"] * 1000, })
mar_2002 = mar_2002.assign_coords(
    {"x": mar_2002["x"] * 1000, "y": mar_2002["y"] * 1000, })
mar_2003 = mar_2003.assign_coords(
    {"x": mar_2003["x"] * 1000, "y": mar_2003["y"] * 1000, })
mar_2004 = mar_2004.assign_coords(
    {"x": mar_2004["x"] * 1000, "y": mar_2004["y"] * 1000, })
mar_2005 = mar_2005.assign_coords(
    {"x": mar_2005["x"] * 1000, "y": mar_2005["y"] * 1000, })
mar_2006 = mar_2006.assign_coords(
    {"x": mar_2006["x"] * 1000, "y": mar_2006["y"] * 1000, })
mar_2007 = mar_2007.assign_coords(
    {"x": mar_2007["x"] * 1000, "y": mar_2007["y"] * 1000, })
mar_2008 = mar_2008.assign_coords(
    {"x": mar_2008["x"] * 1000, "y": mar_2008["y"] * 1000, })
mar_2009 = mar_2009.assign_coords(
    {"x": mar_2009["x"] * 1000, "y": mar_2009["y"] * 1000, })
mar_2010 = mar_2010.assign_coords(
    {"x": mar_2010["x"] * 1000, "y": mar_2010["y"] * 1000, })
mar_2011 = mar_2011.assign_coords(
    {"x": mar_2011["x"] * 1000, "y": mar_2011["y"] * 1000, })
mar_2012 = mar_2012.assign_coords(
    {"x": mar_2012["x"] * 1000, "y": mar_2012["y"] * 1000, })
mar_2013 = mar_2013.assign_coords(
    {"x": mar_2013["x"] * 1000, "y": mar_2013["y"] * 1000, })
mar_2014 = mar_2014.assign_coords(
    {"x": mar_2014["x"] * 1000, "y": mar_2014["y"] * 1000, })
mar_2015 = mar_2015.assign_coords(
    {"x": mar_2015["x"] * 1000, "y": mar_2015["y"] * 1000, })
mar_2016 = mar_2016.assign_coords(
    {"x": mar_2016["x"] * 1000, "y": mar_2016["y"] * 1000, })
mar_2017 = mar_2017.assign_coords(
    {"x": mar_2017["x"] * 1000, "y": mar_2017["y"] * 1000, })
mar_2018 = mar_2018.assign_coords(
    {"x": mar_2018["x"] * 1000, "y": mar_2018["y"] * 1000, })
mar_2019 = mar_2019.assign_coords(
    {"x": mar_2019["x"] * 1000, "y": mar_2019["y"] * 1000, })
mar_2020 = mar_2020.assign_coords(
    {"x": mar_2020["x"] * 1000, "y": mar_2020["y"] * 1000, })
mar_2021 = mar_2021.assign_coords(
    {"x": mar_2021["x"] * 1000, "y": mar_2021["y"] * 1000, })
mar_2022 = mar_2022.assign_coords(
    {"x": mar_2022["x"] * 1000, "y": mar_2022["y"] * 1000, })
mar_2023 = mar_2023.assign_coords(
    {"x": mar_2023["x"] * 1000, "y": mar_2023["y"] * 1000, })
mar_2024 = mar_2024.assign_coords(
    {"x": mar_2024["x"] * 1000, "y": mar_2024["y"] * 1000, })

# Assign the correct CRS to MAR from its metadata

mar_2000 = mar_2000.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2000 = mar_2000.rio.write_crs("EPSG:3413")

mar_2001 = mar_2001.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2001 = mar_2001.rio.write_crs("EPSG:3413")

mar_2002 = mar_2002.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2002 = mar_2002.rio.write_crs("EPSG:3413")

mar_2003 = mar_2003.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2003 = mar_2003.rio.write_crs("EPSG:3413")

mar_2004 = mar_2004.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2004 = mar_2004.rio.write_crs("EPSG:3413")

mar_2005 = mar_2005.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2005 = mar_2005.rio.write_crs("EPSG:3413")

mar_2006 = mar_2006.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2006 = mar_2006.rio.write_crs("EPSG:3413")

mar_2007 = mar_2007.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2007 = mar_2007.rio.write_crs("EPSG:3413")

mar_2008 = mar_2008.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2008 = mar_2008.rio.write_crs("EPSG:3413")

mar_2009 = mar_2009.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2009 = mar_2009.rio.write_crs("EPSG:3413")

mar_2010 = mar_2010.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2010 = mar_2010.rio.write_crs("EPSG:3413")

mar_2011 = mar_2011.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2011 = mar_2011.rio.write_crs("EPSG:3413")

mar_2012 = mar_2012.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2012 = mar_2012.rio.write_crs("EPSG:3413")

mar_2013 = mar_2013.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2013 = mar_2013.rio.write_crs("EPSG:3413")

mar_2014 = mar_2014.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2014 = mar_2014.rio.write_crs("EPSG:3413")

mar_2015 = mar_2015.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2015 = mar_2015.rio.write_crs("EPSG:3413")

mar_2016 = mar_2016.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2016 = mar_2016.rio.write_crs("EPSG:3413")

mar_2017 = mar_2017.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2017 = mar_2017.rio.write_crs("EPSG:3413")

mar_2018 = mar_2018.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2018 = mar_2018.rio.write_crs("EPSG:3413")

mar_2019 = mar_2019.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2019 = mar_2019.rio.write_crs("EPSG:3413")

mar_2020 = mar_2020.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2020 = mar_2020.rio.write_crs("EPSG:3413")

mar_2021 = mar_2021.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2021 = mar_2021.rio.write_crs("EPSG:3413")

mar_2022 = mar_2022.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2022 = mar_2022.rio.write_crs("EPSG:3413")

mar_2023 = mar_2023.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2023 = mar_2023.rio.write_crs("EPSG:3413")

mar_2024 = mar_2024.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
mar_2024 = mar_2024.rio.write_crs("EPSG:3413")

# Reproject catchments to MAR CRS
rb_catchment = rio_behar_catchment.to_crs(mar_2000.rio.crs)
ak4_catchment = ak4_catchment.to_crs(mar_2000.rio.crs)
minturn_catchment = minturn_catchment.to_crs(mar_2000.rio.crs)


# Print catchment areas
catchments = {
    "Rio Behar": rb_catchment,
    "AK4": ak4_catchment,
    "Minturn": minturn_catchment}

for name, gdf in catchments.items():
    area_m2 = gdf.geometry.area.sum()
    area_km2 = area_m2 / 1e6
    print(f"{name} catchment area: {area_km2:.2f} km^2")

# Determine the fractional coverage of MAR grid cells intersecting a catchment

def make_fraction(ds, catchment_gdf, msk_var="MSK"):
    """
    Fractional coverage of each MAR grid cell by a catchment,
    weighted by MAR ice-sheet mask percentage.

    Output fraction =
        catchment overlap fraction * MSK fraction

    So a cell that is 50% inside the catchment and MSK = 80
    gets fraction = 0.5 * 0.8 = 0.4.
    """

    x = ds["x"].values
    y = ds["y"].values
    dx = np.abs(x[1] - x[0])
    dy = np.abs(y[1] - y[0])

    catchment_geom = catchment_gdf.geometry.iloc[0]
    msk = ds[msk_var]

    frac = np.zeros((len(y), len(x)))

    for j, yy in enumerate(y):
        for i, xx in enumerate(x):

            cell = box(
                xx - dx / 2, yy - dy / 2,
                xx + dx / 2, yy + dy / 2
            )

            inter_area = cell.intersection(catchment_geom).area

            if inter_area > 0:
                overlap_fraction = inter_area / cell.area

                msk_fraction = float(msk.sel(x=xx, y=yy).values) / 100.0

                frac[j, i] = overlap_fraction * msk_fraction
            else:
                frac[j, i] = 0.0

    fraction = xr.DataArray(
        frac,
        coords={"y": y, "x": x},
        dims=("y", "x"),
        name="fraction"
    )

    fraction = fraction.rio.write_crs(ds.rio.crs)

    return fraction

# Get MAR grid cell fractional coverage for Rio Behar, AK4, and Minturn
rb_fraction = make_fraction(mar_2000, rb_catchment)
ak4_fraction = make_fraction(mar_2008, ak4_catchment)
minturn_fraction = make_fraction(mar_2019, minturn_catchment)

# 4 panel figure of catchments mapped onto MAR grid
def plot_catchment_remap(
    ds,
    catchment_gdf,
    fraction_da,
    title=None,
    pad_cells=1,
    cmap_name="Blues",
    ax=None,
):
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 12))

    x = ds["x"].values
    y = ds["y"].values
    dx = float(np.abs(x[1] - x[0]))
    dy = float(np.abs(y[1] - y[0]))

    catchment_geom = catchment_gdf.geometry.iloc[0]
    minx, miny, maxx, maxy = catchment_geom.bounds

    ix = np.where((x >= minx - pad_cells * dx) & (x <= maxx + pad_cells * dx))[0]
    iy = np.where((y >= miny - pad_cells * dy) & (y <= maxy + pad_cells * dy))[0]

    if len(ix) == 0 or len(iy) == 0:
        raise ValueError("Catchment bounds do not overlap dataset coordinates.")

    cmap = plt.get_cmap(cmap_name)
    norm = plt.Normalize(vmin=0, vmax=1)

    patches = []
    patch_colors = []

    for j in iy:
        for i in ix:
            xx = x[i]
            yy = y[j]

            frac_val = float(fraction_da.sel(x=xx, y=yy).values)

            cell_x = [xx - dx/2, xx + dx/2, xx + dx/2, xx - dx/2, xx - dx/2]
            cell_y = [yy - dy/2, yy - dy/2, yy + dy/2, yy + dy/2, yy - dy/2]
            ax.plot(cell_x, cell_y, color="black", lw=0.8, alpha=0.8, zorder=0)

            if frac_val > 0:
                cell = box(xx - dx/2, yy - dy/2, xx + dx/2, yy + dy/2)
                inter = cell.intersection(catchment_geom)

                if not inter.is_empty:

                    if inter.geom_type == "Polygon":
                        geoms = [inter]
                    elif inter.geom_type == "MultiPolygon":
                        geoms = list(inter.geoms)
                    elif inter.geom_type == "GeometryCollection":
                        geoms = [g for g in inter.geoms if g.geom_type == "Polygon"]
                    else:
                        geoms = []

                    color = cmap(norm(frac_val))

                    for geom in geoms:
                        if geom.area > 0:
                            coords = np.asarray(geom.exterior.coords)
                            patches.append(MplPolygon(coords, closed=True))
                            patch_colors.append(color)

                            for ring in geom.interiors:
                                hole_xy = np.asarray(ring.coords)
                                ax.fill(hole_xy[:, 0], hole_xy[:, 1], color="white", zorder=2)

    if patches:
        pc = PatchCollection(
            patches,
            facecolor=patch_colors,
            edgecolor="none",
            alpha=0.9,
            zorder=1,
        )
        ax.add_collection(pc)

    catchment_gdf.boundary.plot(ax=ax, color="0.2", linewidth=1.5, zorder=3)

    ax.set_xlim(x[ix[0]] - dx/2, x[ix[-1]] + dx/2)
    ax.set_ylim(y[iy[0]] - dy/2, y[iy[-1]] + dy/2)

    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(1.2)

    if title:
        ax.set_title(title, fontsize=24)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    return sm

fig, axes = plt.subplots(
    2, 2,
    figsize=(14, 14),
    constrained_layout=True
)
axes = axes.ravel()

sm = plot_catchment_remap(mar_2000, rb_catchment, rb_fraction,
                          title="Rio Behar", pad_cells=0.5, ax=axes[0])

plot_catchment_remap(mar_2000, ak4_catchment, ak4_fraction,
                     title="AK4", pad_cells=0.5, ax=axes[1])

plot_catchment_remap(mar_2000, minturn_catchment, minturn_fraction,
                     title="Minturn", pad_cells=0.5, ax=axes[2])

cbar = fig.colorbar(sm, ax=axes, orientation="vertical", shrink=0.8)
cbar.set_label("Grid cell fractional overlap", fontsize=20)   # bigger title
cbar.ax.tick_params(labelsize=20)                   # bigger ticks

plt.show()

# 4-panel figure of catchments MAR ice sheet mask
def plot_catchment_msk(
    ds,
    catchment_gdf,
    fraction_da,
    title=None,
    pad_cells=1,
    ax=None,
    norm=None,
    cmap=None,
):

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 12))

    if cmap is None:
        cmap = plt.get_cmap("gray")

    if norm is None:
        norm = plt.Normalize(vmin=0, vmax=100)

    x = ds["x"].values
    y = ds["y"].values
    dx = float(np.abs(x[1] - x[0]))
    dy = float(np.abs(y[1] - y[0]))

    catchment_geom = catchment_gdf.geometry.iloc[0]
    minx, miny, maxx, maxy = catchment_geom.bounds

    ix = np.where((x >= minx - pad_cells * dx) & (x <= maxx + pad_cells * dx))[0]
    iy = np.where((y >= miny - pad_cells * dy) & (y <= maxy + pad_cells * dy))[0]

    if len(ix) == 0 or len(iy) == 0:
        raise ValueError("Catchment bounds do not overlap dataset coordinates.")

    msk = ds["MSK"]

    patches = []
    patch_colors = []

    for j in iy:
        for i in ix:
            xx = x[i]
            yy = y[j]

            frac_val = float(fraction_da.sel(x=xx, y=yy).values)

            # Draw all grid-cell outlines in the local window
            cell_x = [xx - dx/2, xx + dx/2, xx + dx/2, xx - dx/2, xx - dx/2]
            cell_y = [yy - dy/2, yy - dy/2, yy + dy/2, yy + dy/2, yy - dy/2]
            ax.plot(cell_x, cell_y, color="black", lw=0.8, alpha=0.8, zorder=0)

            # Only fill cells that overlap the catchment
            if frac_val > 0:
                msk_val = float(msk.sel(x=xx, y=yy).values)

                cell = box(xx - dx/2, yy - dy/2, xx + dx/2, yy + dy/2)
                inter = cell.intersection(catchment_geom)

                if not inter.is_empty:
                    if inter.geom_type == "Polygon":
                        geoms = [inter]
                    elif inter.geom_type == "MultiPolygon":
                        geoms = list(inter.geoms)
                    elif inter.geom_type == "GeometryCollection":
                        geoms = [g for g in inter.geoms if g.geom_type == "Polygon"]
                    else:
                        geoms = []

                    color = cmap(norm(msk_val))

                    for geom in geoms:
                        if geom.area > 0:
                            coords = np.asarray(geom.exterior.coords)
                            patches.append(MplPolygon(coords, closed=True))
                            patch_colors.append(color)

                            for ring in geom.interiors:
                                hole_xy = np.asarray(ring.coords)
                                ax.fill(
                                    hole_xy[:, 0],
                                    hole_xy[:, 1],
                                    color="white",
                                    zorder=2
                                )

    if patches:
        pc = PatchCollection(
            patches,
            facecolor=patch_colors,
            edgecolor="none",
            alpha=0.9,
            zorder=1,
        )
        ax.add_collection(pc)

    # Catchment outline
    catchment_gdf.boundary.plot(ax=ax, color="0.2", linewidth=1.5, zorder=3)

    ax.set_xlim(x[ix[0]] - dx/2, x[ix[-1]] + dx/2)
    ax.set_ylim(y[iy[0]] - dy/2, y[iy[-1]] + dy/2)

    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(1.2)

    if title:
        ax.set_title(title, fontsize=24)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    return sm


# Shared colormap and normalization for ALL panels
cmap = plt.get_cmap("gray")
norm = plt.Normalize(vmin=0, vmax=100)

# Make 4-panel MSK figure
fig, axes = plt.subplots(
    2, 2,
    figsize=(14, 14),
    constrained_layout=True
)
axes = axes.ravel()

sm = plot_catchment_msk(
    mar_2000,
    rb_catchment,
    rb_fraction,
    title="Rio Behar",
    pad_cells=0.5,
    ax=axes[0],
    norm=norm,
    cmap=cmap,
)

plot_catchment_msk(
    mar_2000,
    ak4_catchment,
    ak4_fraction,
    title="AK4",
    pad_cells=0.5,
    ax=axes[1],
    norm=norm,
    cmap=cmap,
)

plot_catchment_msk(
    mar_2000,
    minturn_catchment,
    minturn_fraction,
    title="Minturn",
    pad_cells=0.5,
    ax=axes[2],
    norm=norm,
    cmap=cmap,
)

cbar = fig.colorbar(sm, ax=axes, orientation="vertical", shrink=0.8)
cbar.set_label("MAR Ice Sheet Mask (%)", fontsize=20)
cbar.ax.tick_params(labelsize=20)
cbar.set_ticks([0, 25, 50, 75, 100])

plt.show()

# Function to calculate the percentage of a catchment that is glaciated
# using the MAR ice-sheet mask and the fractional overlap grid.
def glaciated_percent(catchment_gdf, fraction_da, ds):

    # Compute MAR grid-cell dimensions (m)
    dx = abs(ds.x.values[1] - ds.x.values[0])
    dy = abs(ds.y.values[1] - ds.y.values[0])

    # Area of a single MAR grid cell (m²)
    cell_area = dx * dy

    # Total glaciated area within the catchment (m²)
    #
    # fraction_da contains:
    #     overlap_fraction × (MSK / 100)
    #
    # Multiplying by cell_area converts each grid-cell fraction
    # into an effective glaciated area contribution.
    glaciated_area = float((fraction_da * cell_area).sum())

    # Total catchment area (m²)
    catchment_area = catchment_gdf.geometry.area.sum()

    # Return percentage of catchment that is glaciated
    return 100 * glaciated_area / catchment_area


# Calculate and print glaciated percentage for each catchment
for name, gdf, frac in [
    ("Rio Behar", rb_catchment, rb_fraction),
    ("AK4", ak4_catchment, ak4_fraction),
    ("Minturn", minturn_catchment, minturn_fraction)
]:

    # Compute glaciated percentage
    pct = glaciated_percent(gdf, frac, mar_2000)

    # Print result
    print(f"{name}: {pct:.1f}% glaciated")

def clip_mar(mar, geometry, crs, *, drop=True, all_touched=True, allow_empty=True):
    """
    Safely clip a MAR xarray Dataset or DataArray to a geometry.

    Parameters
    ----------
    mar : xr.Dataset or xr.DataArray
        MAR data with x/y spatial dimensions.
    geometry : GeoSeries or list of shapely geometries
        Geometry to clip to.
    crs : CRS
        CRS of the geometry.
    drop : bool, default True
        Drop pixels outside geometry.
    all_touched : bool, default True
        Include pixels touched by geometry (important for small basins).
    allow_empty : bool, default True
        If True, return NaNs instead of raising NoDataInBounds.

    Returns
    -------
    xr.Dataset or xr.DataArray
    """

    # Handle DataArray directly
    if isinstance(mar, xr.DataArray):
        try:
            return mar.rio.clip(geometry,
                                crs=crs,
                                drop=drop,
                                all_touched=all_touched)
        except rio.exceptions.NoDataInBounds:
            if allow_empty:
                return mar * np.nan
            raise

    # Dataset case
    out_vars = {}

    for v in mar.data_vars:
        da = mar[v]

        # Skip known non-raster variables
        if v.lower() in {"lon", "lat"}:
            continue
        if v.endswith("_bnds"):
            continue
        if "bnds" in da.dims:
            continue
        if not {"x", "y"}.issubset(da.dims):
            continue

        try:
            out_vars[v] = da.rio.clip(geometry,
                                      crs=crs,
                                      drop=drop,
                                      all_touched=all_touched)
        except rio.exceptions.NoDataInBounds:
            if allow_empty:
                out_vars[v] = da * np.nan
            else:
                raise

    if not out_vars:
        raise ValueError("No spatial MAR variables could be clipped.")

    clipped = xr.Dataset(out_vars)

    # Preserve CRS & spatial metadata
    clipped = clipped.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=False)
    clipped = clipped.rio.write_crs(mar.rio.crs, inplace=False)

    return clipped


# Clip MAR to the extent of the Rio Behar catchment
rb_catchment_2000 = clip_mar(
    mar_2000, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2001 = clip_mar(
    mar_2001, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2002 = clip_mar(
    mar_2002, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2003 = clip_mar(
    mar_2003, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2004 = clip_mar(
    mar_2004, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2005 = clip_mar(
    mar_2005, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2006 = clip_mar(
    mar_2006, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2007 = clip_mar(
    mar_2007, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2008 = clip_mar(
    mar_2008, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2009 = clip_mar(
    mar_2009, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2010 = clip_mar(
    mar_2010, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2011 = clip_mar(
    mar_2011, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2012 = clip_mar(
    mar_2012, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2013 = clip_mar(
    mar_2013, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2014 = clip_mar(
    mar_2014, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2015 = clip_mar(
    mar_2015, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2016 = clip_mar(
    mar_2016, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2017 = clip_mar(
    mar_2017, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2018 = clip_mar(
    mar_2018, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2019 = clip_mar(
    mar_2019, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2020 = clip_mar(
    mar_2020, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2021 = clip_mar(
    mar_2021, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2022 = clip_mar(
    mar_2022, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2023 = clip_mar(
    mar_2023, rb_catchment.geometry, crs=rb_catchment.crs)
rb_catchment_2024 = clip_mar(
    mar_2024, rb_catchment.geometry, crs=rb_catchment.crs)

# Clip MAR to the extent of the AK4 catchment
ak4_catchment_2000 = clip_mar(
    mar_2000, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2001 = clip_mar(
    mar_2001, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2002 = clip_mar(
    mar_2002, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2003 = clip_mar(
    mar_2003, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2004 = clip_mar(
    mar_2004, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2005 = clip_mar(
    mar_2005, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2006 = clip_mar(
    mar_2006, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2007 = clip_mar(
    mar_2007, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2008 = clip_mar(
    mar_2008, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2009 = clip_mar(
    mar_2009, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2010 = clip_mar(
    mar_2010, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2011 = clip_mar(
    mar_2011, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2012 = clip_mar(
    mar_2012, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2013 = clip_mar(
    mar_2013, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2014 = clip_mar(
    mar_2014, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2015 = clip_mar(
    mar_2015, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2016 = clip_mar(
    mar_2016, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2017 = clip_mar(
    mar_2017, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2018 = clip_mar(
    mar_2018, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2019 = clip_mar(
    mar_2019, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2020 = clip_mar(
    mar_2020, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2021 = clip_mar(
    mar_2021, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2022 = clip_mar(
    mar_2022, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2023 = clip_mar(
    mar_2023, ak4_catchment.geometry, crs=ak4_catchment.crs)
ak4_catchment_2024 = clip_mar(
    mar_2024, ak4_catchment.geometry, crs=ak4_catchment.crs)

# Clip MAR to the extent of the Minturn catchment
minturn_catchment_2000 = clip_mar(
    mar_2000, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2001 = clip_mar(
    mar_2001, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2002 = clip_mar(
    mar_2002, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2003 = clip_mar(
    mar_2003, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2004 = clip_mar(
    mar_2004, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2005 = clip_mar(
    mar_2005, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2006 = clip_mar(
    mar_2006, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2007 = clip_mar(
    mar_2007, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2008 = clip_mar(
    mar_2008, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2009 = clip_mar(
    mar_2009, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2010 = clip_mar(
    mar_2010, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2011 = clip_mar(
    mar_2011, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2012 = clip_mar(
    mar_2012, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2013 = clip_mar(
    mar_2013, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2014 = clip_mar(
    mar_2014, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2015 = clip_mar(
    mar_2015, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2016 = clip_mar(
    mar_2016, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2017 = clip_mar(
    mar_2017, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2018 = clip_mar(
    mar_2018, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2019 = clip_mar(
    mar_2019, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2020 = clip_mar(
    mar_2020, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2021 = clip_mar(
    mar_2021, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2022 = clip_mar(
    mar_2022, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2023 = clip_mar(
    mar_2023, minturn_catchment.geometry, crs=minturn_catchment.crs)
minturn_catchment_2024 = clip_mar(
    mar_2024, minturn_catchment.geometry, crs=minturn_catchment.crs)

# Define output directory for Rio Behar
output_dir_rb = "/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/Rio_Behar_catchment_2000_2021"

# Create Rio Behar directory if it doesn't exist
os.makedirs(output_dir_rb, exist_ok=True)

# File name (with path) to save Rio Behar catchments
rb_file_name_2000 = os.path.join(output_dir_rb, "rio_behar_catchment_2000.nc")
rb_file_name_2001 = os.path.join(output_dir_rb, "rio_behar_catchment_2001.nc")
rb_file_name_2002 = os.path.join(output_dir_rb, "rio_behar_catchment_2002.nc")
rb_file_name_2003 = os.path.join(output_dir_rb, "rio_behar_catchment_2003.nc")
rb_file_name_2004 = os.path.join(output_dir_rb, "rio_behar_catchment_2004.nc")
rb_file_name_2005 = os.path.join(output_dir_rb, "rio_behar_catchment_2005.nc")
rb_file_name_2006 = os.path.join(output_dir_rb, "rio_behar_catchment_2006.nc")
rb_file_name_2007 = os.path.join(output_dir_rb, "rio_behar_catchment_2007.nc")
rb_file_name_2008 = os.path.join(output_dir_rb, "rio_behar_catchment_2008.nc")
rb_file_name_2009 = os.path.join(output_dir_rb, "rio_behar_catchment_2009.nc")
rb_file_name_2010 = os.path.join(output_dir_rb, "rio_behar_catchment_2010.nc")
rb_file_name_2011 = os.path.join(output_dir_rb, "rio_behar_catchment_2011.nc")
rb_file_name_2012 = os.path.join(output_dir_rb, "rio_behar_catchment_2012.nc")
rb_file_name_2013 = os.path.join(output_dir_rb, "rio_behar_catchment_2013.nc")
rb_file_name_2014 = os.path.join(output_dir_rb, "rio_behar_catchment_2014.nc")
rb_file_name_2015 = os.path.join(output_dir_rb, "rio_behar_catchment_2015.nc")
rb_file_name_2016 = os.path.join(output_dir_rb, "rio_behar_catchment_2016.nc")
rb_file_name_2017 = os.path.join(output_dir_rb, "rio_behar_catchment_2017.nc")
rb_file_name_2018 = os.path.join(output_dir_rb, "rio_behar_catchment_2018.nc")
rb_file_name_2019 = os.path.join(output_dir_rb, "rio_behar_catchment_2019.nc")
rb_file_name_2020 = os.path.join(output_dir_rb, "rio_behar_catchment_2020.nc")
rb_file_name_2021 = os.path.join(output_dir_rb, "rio_behar_catchment_2021.nc")
rb_file_name_2022 = os.path.join(output_dir_rb, "rio_behar_catchment_2022.nc")
rb_file_name_2023 = os.path.join(output_dir_rb, "rio_behar_catchment_2023.nc")
rb_file_name_2024 = os.path.join(output_dir_rb, "rio_behar_catchment_2024.nc")

# File name (with path) to save Rio Behar fraction
rb_frac_file_name = os.path.join(output_dir_rb, "rb_fraction.nc")

# Delete old Rio Behar catchment files if they exist
if os.path.exists(rb_file_name_2000):
    os.remove(rb_file_name_2000)
if os.path.exists(rb_file_name_2001):
    os.remove(rb_file_name_2001)
if os.path.exists(rb_file_name_2002):
    os.remove(rb_file_name_2002)
if os.path.exists(rb_file_name_2003):
    os.remove(rb_file_name_2003)
if os.path.exists(rb_file_name_2004):
    os.remove(rb_file_name_2004)
if os.path.exists(rb_file_name_2005):
    os.remove(rb_file_name_2005)
if os.path.exists(rb_file_name_2006):
    os.remove(rb_file_name_2006)
if os.path.exists(rb_file_name_2007):
    os.remove(rb_file_name_2007)
if os.path.exists(rb_file_name_2008):
    os.remove(rb_file_name_2008)
if os.path.exists(rb_file_name_2009):
    os.remove(rb_file_name_2009)
if os.path.exists(rb_file_name_2010):
    os.remove(rb_file_name_2010)
if os.path.exists(rb_file_name_2011):
    os.remove(rb_file_name_2011)
if os.path.exists(rb_file_name_2012):
    os.remove(rb_file_name_2012)
if os.path.exists(rb_file_name_2013):
    os.remove(rb_file_name_2013)
if os.path.exists(rb_file_name_2014):
    os.remove(rb_file_name_2014)
if os.path.exists(rb_file_name_2015):
    os.remove(rb_file_name_2015)
if os.path.exists(rb_file_name_2016):
    os.remove(rb_file_name_2016)
if os.path.exists(rb_file_name_2017):
    os.remove(rb_file_name_2017)
if os.path.exists(rb_file_name_2018):
    os.remove(rb_file_name_2018)
if os.path.exists(rb_file_name_2019):
    os.remove(rb_file_name_2019)
if os.path.exists(rb_file_name_2020):
    os.remove(rb_file_name_2020)
if os.path.exists(rb_file_name_2021):
    os.remove(rb_file_name_2021)
if os.path.exists(rb_file_name_2022):
    os.remove(rb_file_name_2022)
if os.path.exists(rb_file_name_2023):
    os.remove(rb_file_name_2023)
if os.path.exists(rb_file_name_2024):
    os.remove(rb_file_name_2024)

# Delete old Rio Behar fraction file if it exists
if os.path.exists(rb_frac_file_name):
    os.remove(rb_frac_file_name)

# Save Rio Behar catchment files to NetCDF
rb_catchment_2000.to_netcdf(rb_file_name_2000)
rb_catchment_2001.to_netcdf(rb_file_name_2001)
rb_catchment_2002.to_netcdf(rb_file_name_2002)
rb_catchment_2003.to_netcdf(rb_file_name_2003)
rb_catchment_2004.to_netcdf(rb_file_name_2004)
rb_catchment_2005.to_netcdf(rb_file_name_2005)
rb_catchment_2006.to_netcdf(rb_file_name_2006)
rb_catchment_2007.to_netcdf(rb_file_name_2007)
rb_catchment_2008.to_netcdf(rb_file_name_2008)
rb_catchment_2009.to_netcdf(rb_file_name_2009)
rb_catchment_2010.to_netcdf(rb_file_name_2010)
rb_catchment_2011.to_netcdf(rb_file_name_2011)
rb_catchment_2012.to_netcdf(rb_file_name_2012)
rb_catchment_2013.to_netcdf(rb_file_name_2013)
rb_catchment_2014.to_netcdf(rb_file_name_2014)
rb_catchment_2015.to_netcdf(rb_file_name_2015)
rb_catchment_2016.to_netcdf(rb_file_name_2016)
rb_catchment_2017.to_netcdf(rb_file_name_2017)
rb_catchment_2018.to_netcdf(rb_file_name_2018)
rb_catchment_2019.to_netcdf(rb_file_name_2019)
rb_catchment_2020.to_netcdf(rb_file_name_2020)
rb_catchment_2021.to_netcdf(rb_file_name_2021)
rb_catchment_2022.to_netcdf(rb_file_name_2022)
rb_catchment_2023.to_netcdf(rb_file_name_2023)
rb_catchment_2024.to_netcdf(rb_file_name_2024)

# Save Rio Behar fraction file to NetCDF
rb_fraction.to_netcdf(rb_frac_file_name)

# Define output directory for AK4
output_dir_ak4 = "/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/AK4_catchment_2008_2016"

# Create AK4 directory if it doesn't exist
os.makedirs(output_dir_ak4, exist_ok=True)

# File name (with path) to save AK4 catchments
ak4_file_name_2000 = os.path.join(output_dir_ak4, "ak4_catchment_2000.nc")
ak4_file_name_2001 = os.path.join(output_dir_ak4, "ak4_catchment_2001.nc")
ak4_file_name_2002 = os.path.join(output_dir_ak4, "ak4_catchment_2002.nc")
ak4_file_name_2003 = os.path.join(output_dir_ak4, "ak4_catchment_2003.nc")
ak4_file_name_2004 = os.path.join(output_dir_ak4, "ak4_catchment_2004.nc")
ak4_file_name_2005 = os.path.join(output_dir_ak4, "ak4_catchment_2005.nc")
ak4_file_name_2006 = os.path.join(output_dir_ak4, "ak4_catchment_2006.nc")
ak4_file_name_2007 = os.path.join(output_dir_ak4, "ak4_catchment_2007.nc")
ak4_file_name_2008 = os.path.join(output_dir_ak4, "ak4_catchment_2008.nc")
ak4_file_name_2009 = os.path.join(output_dir_ak4, "ak4_catchment_2009.nc")
ak4_file_name_2010 = os.path.join(output_dir_ak4, "ak4_catchment_2010.nc")
ak4_file_name_2011 = os.path.join(output_dir_ak4, "ak4_catchment_2011.nc")
ak4_file_name_2012 = os.path.join(output_dir_ak4, "ak4_catchment_2012.nc")
ak4_file_name_2013 = os.path.join(output_dir_ak4, "ak4_catchment_2013.nc")
ak4_file_name_2014 = os.path.join(output_dir_ak4, "ak4_catchment_2014.nc")
ak4_file_name_2015 = os.path.join(output_dir_ak4, "ak4_catchment_2015.nc")
ak4_file_name_2016 = os.path.join(output_dir_ak4, "ak4_catchment_2016.nc")
ak4_file_name_2017 = os.path.join(output_dir_ak4, "ak4_catchment_2017.nc")
ak4_file_name_2018 = os.path.join(output_dir_ak4, "ak4_catchment_2018.nc")
ak4_file_name_2019 = os.path.join(output_dir_ak4, "ak4_catchment_2019.nc")
ak4_file_name_2020 = os.path.join(output_dir_ak4, "ak4_catchment_2020.nc")
ak4_file_name_2021 = os.path.join(output_dir_ak4, "ak4_catchment_2021.nc")
ak4_file_name_2022 = os.path.join(output_dir_ak4, "ak4_catchment_2022.nc")
ak4_file_name_2023 = os.path.join(output_dir_ak4, "ak4_catchment_2023.nc")
ak4_file_name_2024 = os.path.join(output_dir_ak4, "ak4_catchment_2024.nc")

# File name (with path) to save AK4 fraction
ak4_frac_file_name = os.path.join(output_dir_ak4, "ak4_fraction.nc")

# Delete old AK4 catchment files if they exist
if os.path.exists(ak4_file_name_2000):
    os.remove(ak4_file_name_2000)
if os.path.exists(ak4_file_name_2001):
    os.remove(ak4_file_name_2001)
if os.path.exists(ak4_file_name_2002):
    os.remove(ak4_file_name_2002)
if os.path.exists(ak4_file_name_2003):
    os.remove(ak4_file_name_2003)
if os.path.exists(ak4_file_name_2004):
    os.remove(ak4_file_name_2004)
if os.path.exists(ak4_file_name_2005):
    os.remove(ak4_file_name_2005)
if os.path.exists(ak4_file_name_2006):
    os.remove(ak4_file_name_2006)
if os.path.exists(ak4_file_name_2007):
    os.remove(ak4_file_name_2007)
if os.path.exists(ak4_file_name_2008):
    os.remove(ak4_file_name_2008)
if os.path.exists(ak4_file_name_2009):
    os.remove(ak4_file_name_2009)
if os.path.exists(ak4_file_name_2010):
    os.remove(ak4_file_name_2010)
if os.path.exists(ak4_file_name_2011):
    os.remove(ak4_file_name_2011)
if os.path.exists(ak4_file_name_2012):
    os.remove(ak4_file_name_2012)
if os.path.exists(ak4_file_name_2013):
    os.remove(ak4_file_name_2013)
if os.path.exists(ak4_file_name_2014):
    os.remove(ak4_file_name_2014)
if os.path.exists(ak4_file_name_2015):
    os.remove(ak4_file_name_2015)
if os.path.exists(ak4_file_name_2016):
    os.remove(ak4_file_name_2016)
if os.path.exists(ak4_file_name_2017):
    os.remove(ak4_file_name_2017)
if os.path.exists(ak4_file_name_2018):
    os.remove(ak4_file_name_2018)
if os.path.exists(ak4_file_name_2019):
    os.remove(ak4_file_name_2019)
if os.path.exists(ak4_file_name_2020):
    os.remove(ak4_file_name_2020)  
if os.path.exists(ak4_file_name_2021):
    os.remove(ak4_file_name_2021)
if os.path.exists(ak4_file_name_2022):
    os.remove(ak4_file_name_2022)
if os.path.exists(ak4_file_name_2023):
    os.remove(ak4_file_name_2023)
if os.path.exists(ak4_file_name_2024):
    os.remove(ak4_file_name_2024)

# Delete old AK4 fraction file if it exists
if os.path.exists(ak4_frac_file_name):
    os.remove(ak4_frac_file_name)

# Save AK4 catchment files to NetCDF
ak4_catchment_2000.to_netcdf(ak4_file_name_2000)
ak4_catchment_2001.to_netcdf(ak4_file_name_2001)
ak4_catchment_2002.to_netcdf(ak4_file_name_2002)
ak4_catchment_2003.to_netcdf(ak4_file_name_2003)
ak4_catchment_2004.to_netcdf(ak4_file_name_2004)
ak4_catchment_2005.to_netcdf(ak4_file_name_2005)
ak4_catchment_2006.to_netcdf(ak4_file_name_2006)
ak4_catchment_2007.to_netcdf(ak4_file_name_2007)
ak4_catchment_2008.to_netcdf(ak4_file_name_2008)
ak4_catchment_2009.to_netcdf(ak4_file_name_2009)
ak4_catchment_2010.to_netcdf(ak4_file_name_2010)
ak4_catchment_2011.to_netcdf(ak4_file_name_2011)
ak4_catchment_2012.to_netcdf(ak4_file_name_2012)
ak4_catchment_2013.to_netcdf(ak4_file_name_2013)
ak4_catchment_2014.to_netcdf(ak4_file_name_2014)
ak4_catchment_2015.to_netcdf(ak4_file_name_2015)
ak4_catchment_2016.to_netcdf(ak4_file_name_2016)
ak4_catchment_2017.to_netcdf(ak4_file_name_2017)
ak4_catchment_2018.to_netcdf(ak4_file_name_2018)
ak4_catchment_2019.to_netcdf(ak4_file_name_2019)
ak4_catchment_2020.to_netcdf(ak4_file_name_2020)
ak4_catchment_2021.to_netcdf(ak4_file_name_2021)
ak4_catchment_2022.to_netcdf(ak4_file_name_2022)
ak4_catchment_2023.to_netcdf(ak4_file_name_2023)
ak4_catchment_2024.to_netcdf(ak4_file_name_2024)

# Save AK4 fraction file to NetCDF
ak4_fraction.to_netcdf(ak4_frac_file_name)

# Define output directory for Minturn
output_dir_minturn = "/Users/mlm211/Documents/DeepMelt/catchment-scale/MAR_catchments/minturn_catchment_2019_2020"

# Create Minturn directory if it doesn't exist
os.makedirs(output_dir_minturn, exist_ok=True)

# File name (with path) to save Minturn catchments
minturn_file_name_2000 = os.path.join(
    output_dir_minturn, "minturn_catchment_2000.nc")
minturn_file_name_2001 = os.path.join(
    output_dir_minturn, "minturn_catchment_2001.nc")
minturn_file_name_2002 = os.path.join(
    output_dir_minturn, "minturn_catchment_2002.nc")
minturn_file_name_2003 = os.path.join(
    output_dir_minturn, "minturn_catchment_2003.nc")
minturn_file_name_2004 = os.path.join(
    output_dir_minturn, "minturn_catchment_2004.nc")
minturn_file_name_2005 = os.path.join(
    output_dir_minturn, "minturn_catchment_2005.nc")
minturn_file_name_2006 = os.path.join(
    output_dir_minturn, "minturn_catchment_2006.nc")
minturn_file_name_2007 = os.path.join(
    output_dir_minturn, "minturn_catchment_2007.nc")
minturn_file_name_2008 = os.path.join(
    output_dir_minturn, "minturn_catchment_2008.nc")
minturn_file_name_2009 = os.path.join(
    output_dir_minturn, "minturn_catchment_2009.nc")
minturn_file_name_2010 = os.path.join(
    output_dir_minturn, "minturn_catchment_2010.nc")
minturn_file_name_2011 = os.path.join(
    output_dir_minturn, "minturn_catchment_2011.nc")
minturn_file_name_2012 = os.path.join(
    output_dir_minturn, "minturn_catchment_2012.nc")
minturn_file_name_2013 = os.path.join(
    output_dir_minturn, "minturn_catchment_2013.nc")
minturn_file_name_2014 = os.path.join(
    output_dir_minturn, "minturn_catchment_2014.nc")
minturn_file_name_2015 = os.path.join(
    output_dir_minturn, "minturn_catchment_2015.nc")
minturn_file_name_2016 = os.path.join(
    output_dir_minturn, "minturn_catchment_2016.nc")
minturn_file_name_2017 = os.path.join(
    output_dir_minturn, "minturn_catchment_2017.nc")
minturn_file_name_2018 = os.path.join(
    output_dir_minturn, "minturn_catchment_2018.nc")
minturn_file_name_2019 = os.path.join(
    output_dir_minturn, "minturn_catchment_2019.nc")
minturn_file_name_2020 = os.path.join(
    output_dir_minturn, "minturn_catchment_2020.nc")
minturn_file_name_2021 = os.path.join(
    output_dir_minturn, "minturn_catchment_2021.nc")
minturn_file_name_2022 = os.path.join(
    output_dir_minturn, "minturn_catchment_2022.nc")
minturn_file_name_2023 = os.path.join(
    output_dir_minturn, "minturn_catchment_2023.nc")
minturn_file_name_2024 = os.path.join(
    output_dir_minturn, "minturn_catchment_2024.nc")

# File name (with path) to save Minturn fraction
minturn_frac_file_name = os.path.join(
    output_dir_minturn, "minturn_fraction.nc")

# Delete old Minturn catchment files if they exist
if os.path.exists(minturn_file_name_2000):
    os.remove(minturn_file_name_2000)
if os.path.exists(minturn_file_name_2001):
    os.remove(minturn_file_name_2001)
if os.path.exists(minturn_file_name_2002):
    os.remove(minturn_file_name_2002)
if os.path.exists(minturn_file_name_2003):
    os.remove(minturn_file_name_2003)
if os.path.exists(minturn_file_name_2004):
    os.remove(minturn_file_name_2004)
if os.path.exists(minturn_file_name_2005):
    os.remove(minturn_file_name_2005)
if os.path.exists(minturn_file_name_2006):
    os.remove(minturn_file_name_2006)
if os.path.exists(minturn_file_name_2007):
    os.remove(minturn_file_name_2007)
if os.path.exists(minturn_file_name_2008):
    os.remove(minturn_file_name_2008)
if os.path.exists(minturn_file_name_2009):
    os.remove(minturn_file_name_2009)
if os.path.exists(minturn_file_name_2010):
    os.remove(minturn_file_name_2010)
if os.path.exists(minturn_file_name_2011):
    os.remove(minturn_file_name_2011)
if os.path.exists(minturn_file_name_2012):
    os.remove(minturn_file_name_2012)
if os.path.exists(minturn_file_name_2013):
    os.remove(minturn_file_name_2013)
if os.path.exists(minturn_file_name_2014):
    os.remove(minturn_file_name_2014)
if os.path.exists(minturn_file_name_2015):
    os.remove(minturn_file_name_2015)
if os.path.exists(minturn_file_name_2016):
    os.remove(minturn_file_name_2016)
if os.path.exists(minturn_file_name_2017):
    os.remove(minturn_file_name_2017)
if os.path.exists(minturn_file_name_2018):
    os.remove(minturn_file_name_2018)
if os.path.exists(minturn_file_name_2019):
    os.remove(minturn_file_name_2019)
if os.path.exists(minturn_file_name_2020):
    os.remove(minturn_file_name_2020)
if os.path.exists(minturn_file_name_2021):
    os.remove(minturn_file_name_2021)
if os.path.exists(minturn_file_name_2022):
    os.remove(minturn_file_name_2022)
if os.path.exists(minturn_file_name_2023):
    os.remove(minturn_file_name_2023)
if os.path.exists(minturn_file_name_2024):
    os.remove(minturn_file_name_2024)

# Delete old Minturn fraction file if it exists
if os.path.exists(minturn_frac_file_name):
    os.remove(minturn_frac_file_name)

# Save Minturn catchment files to NetCDF
minturn_catchment_2000.to_netcdf(minturn_file_name_2000)
minturn_catchment_2001.to_netcdf(minturn_file_name_2001)
minturn_catchment_2002.to_netcdf(minturn_file_name_2002)
minturn_catchment_2003.to_netcdf(minturn_file_name_2003)
minturn_catchment_2004.to_netcdf(minturn_file_name_2004)
minturn_catchment_2005.to_netcdf(minturn_file_name_2005)
minturn_catchment_2006.to_netcdf(minturn_file_name_2006)
minturn_catchment_2007.to_netcdf(minturn_file_name_2007)
minturn_catchment_2008.to_netcdf(minturn_file_name_2008)
minturn_catchment_2009.to_netcdf(minturn_file_name_2009)
minturn_catchment_2010.to_netcdf(minturn_file_name_2010)
minturn_catchment_2011.to_netcdf(minturn_file_name_2011)
minturn_catchment_2012.to_netcdf(minturn_file_name_2012)
minturn_catchment_2013.to_netcdf(minturn_file_name_2013)
minturn_catchment_2014.to_netcdf(minturn_file_name_2014)
minturn_catchment_2015.to_netcdf(minturn_file_name_2015)
minturn_catchment_2016.to_netcdf(minturn_file_name_2016)
minturn_catchment_2017.to_netcdf(minturn_file_name_2017)
minturn_catchment_2018.to_netcdf(minturn_file_name_2018)
minturn_catchment_2019.to_netcdf(minturn_file_name_2019)
minturn_catchment_2020.to_netcdf(minturn_file_name_2020)
minturn_catchment_2021.to_netcdf(minturn_file_name_2021)
minturn_catchment_2022.to_netcdf(minturn_file_name_2022)
minturn_catchment_2023.to_netcdf(minturn_file_name_2023)
minturn_catchment_2024.to_netcdf(minturn_file_name_2024)

# Save Minturn fraction file to NetCDF
minturn_fraction.to_netcdf(minturn_frac_file_name)