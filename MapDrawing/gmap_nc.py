import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib as mpl
import xarray as xr
import cartopy.io.shapereader as shpreader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# 数据路径
path = r"D:\ActiveStudy\ClimateAsymmetry\DataProcess\Result\separate\ESA\ESA_gain.nc"
data = xr.open_dataset(path)
var = data['gain']
lon = data['lon']
lat = data['lat']


def create_map(data):
    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())

    shp_path = r"D:\认真学习\数据\world\world_simplify.shp"
    ax.add_geometries(shpreader.Reader(shp_path).geometries(), ccrs.PlateCarree(),
                      edgecolor='black', facecolor='none', linewidth=1.2)

    grid = ax.gridlines(linestyle='--', color='gray', alpha=0.5, draw_labels=True, linewidth=0.5)
    grid.xlocator = plt.FixedLocator(np.arange(-180, 181, 60))
    grid.ylocator = plt.FixedLocator(np.arange(-60, 91, 30))
    ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=False))
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    bounds = np.linspace(-0.4, 0.4, 9)
    cs = ax.contourf(lon, lat, data, bounds, cmap=mpl.colors.ListedColormap(
        ['#8e1e20', '#df0029', '#ee7c6b', '#ffe5cc', '#e5ffcc', '#7fff00', '#32cd32', '#194d11']).with_extremes(
        over='#093b00', under='#5c0606'),
                     extend='both', transform=ccrs.PlateCarree(), origin="upper")

    cbar = plt.colorbar(cs, orientation='vertical', pad=0.05, aspect=50, shrink=0.7, ticks=bounds, extend='both')
    cbar.set_label('Gain (unit: 0.01)', fontsize=16)
    cbar.ax.tick_params(direction="out", width=1, length=6, labelsize=16, pad=5)

    plt.tight_layout()
    plt.show()


create_map(var)