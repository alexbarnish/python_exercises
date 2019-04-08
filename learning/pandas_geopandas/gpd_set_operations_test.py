#--------------------------------------- Project Info ---------------------------------------#
# Tutorial: Set-Operations with Overlay
# http://geopandas.org/set_operations.html
# http://geopandas.org/mapping.html
# https://matplotlib.org/users/colormaps.html


#--------------------------------------- Libraries ---------------------------------------#
from shapely.geometry import Polygon
import geopandas
import matplotlib.pyplot as plt


#---------------------------------------Main ---------------------------------------#
# create polygons
polys1 = geopandas.GeoSeries([Polygon([(0,0), (2,0), (2,2), (0,2)]),
                              Polygon([(2,2), (4,2), (4,4), (2,4)])])

polys2 = geopandas.GeoSeries([Polygon([(1,1), (3,1), (3,3), (1,3)]),
                              Polygon([(3,3), (5,3), (5,5), (3,5)])])

# load to geo data frame
df1 = geopandas.GeoDataFrame({'geometry': polys1, 'df1':[1,2]})

df2 = geopandas.GeoDataFrame({'geometry': polys2, 'df2':[1,2]})

# plot map on screen
ax = df1.plot(color='red');
df2.plot(ax=ax, color='green', alpha=0.5);

plt.show()


#---------------------------------------overlay operations ---------------------------------------#
# union
res_union = geopandas.overlay(df1, df2, how='union')
print res_union.head()

# intersection
res_intersection = geopandas.overlay(df1, df2, how='intersection')

# symmetrical difference
res_sym_diff = geopandas.overlay(df1, df2, how='symmetric_difference')

# plot map on screen
ax = res_sym_diff.plot(alpha=0.5, cmap='cool')

df1.plot(ax=ax, facecolor='none', edgecolor='k');
df2.plot(ax=ax, facecolor='none', edgecolor='k');

plt.show()