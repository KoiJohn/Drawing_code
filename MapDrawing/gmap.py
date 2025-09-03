import geopandas as gpd
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable

# 设置字体为 Arial
plt.rcParams["font.family"] = 'Arial'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False

# 读取全球矢量边界数据（shapefile）
shapefile_path = r"D:\认真学习\数据\world\world_simplify.shp"
world = gpd.read_file(shapefile_path)

# 读取栅格数据（TIFF）
tiff_path = r"D:\ActiveStudy\ClimateAsymmetry\DataProcess\Global\1.MODIS\13.Gain_Loss_Sum\Forest_Gian_Loss_Minus_project_mask2.tif"
with rasterio.open(tiff_path) as src:
    raster_data = src.read(1)
    extent = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]
    raster_data = np.where(raster_data == src.nodata, np.nan, raster_data)
    raster_data = np.where(raster_data == 0, np.nan, raster_data)

# 创建地图
fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})

# 设置地图的经纬度范围
ax.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())

# 定义自定义色带及对应边界
# 双箭头
cmap = mpl.colors.ListedColormap(['#8e1e20', '#df0029', '#ee7c6b', '#ffe5cc', '#e5ffcc', '#7fff00', '#32cd32',  '#194d11'])\
    .with_extremes(over='#093b00', under='#5c0606')

bounds = np.linspace(-0.4, 0.4, 9)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# 绘制栅格数据
ax.imshow(raster_data, cmap=cmap, norm=norm, extent=extent, transform=ccrs.PlateCarree(), origin="upper")
world.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, transform=ccrs.PlateCarree())

# 添加经纬网
gridlines = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.xlocator = plt.FixedLocator([-120, -60, 0, 60, 120])
gridlines.ylocator = plt.FixedLocator([60, 30, 0, -30])



# 添加自定义色带（色条）
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.05, axes_class=plt.Axes)
colorbar = fig.colorbar(mpl.cm.ScalarMappable(cmap=cmap, norm=norm), cax=cax, extend='both', orientation='vertical', ticks=bounds)
colorbar.ax.tick_params(direction="out", width=1, length=6, labelsize=16, pad=5)
colorbar.ax.tick_params(which="minor", bottom=False)
colorbar.outline.set_linewidth(0.5)

# 显示地图
plt.show()
#fig.savefig("Forest_Net.svg", bbox_inches='tight', dpi=600)