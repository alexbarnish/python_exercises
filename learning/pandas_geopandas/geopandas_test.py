#--------------------------------------- Project Info ---------------------------------------#
# Tutorial: Introduction to Geospatial Data in Python
# https://www.datacamp.com/community/tutorials/geospatial-data-python


#--------------------------------------- Libraries ---------------------------------------#
import pandas as pd
import numpy as np
import scipy as sc
#import RTree as rt
import gdal as gd
import geopandas as gp
import fiona as f
from shapely.geometry import Point
#import PySAL as pys
import matplotlib.pyplot as plt
#import Missingno as msn
#import seaborn as sns


#--------------------------------------- Main ---------------------------------------#
# import country boundary data
country = gp.read_file("data/gz_2010_us_040_00_5m.json")
print country.head()
print type(country)
print type(country.geometry)
print type(country.geometry[0])

# plot map on screen
#country[country['NAME'].isin(['Alaska', 'Hawaii']) == False].plot(figsize=(30,20), color='#3B3C6E');
#plt.show()

# import Hurricane Florence data
florence = pd.read_csv('data/florence.csv')
print florence.head()
print florence.info()
print florence.describe()

# clean data
florence_clean = florence.drop(['AdvisoryNumber', 'Forecaster', 'Received'], axis=1)
print florence_clean.head()
# reformat longitude
florence_clean['Long'] = 0 - florence_clean['Long']
print florence_clean.head()
# format x, y
florence_clean['Coordinates'] = florence_clean[['Long', 'Lat']].values.tolist()
print florence_clean.head()
florence_clean['Coordinates'] = florence_clean['Coordinates'].apply(Point)
print florence_clean.head()
print type(florence_clean)
print type(florence_clean['Coordinates'])

# create geo data frame
florence_gdf = gp.GeoDataFrame(florence_clean, geometry='Coordinates')
print florence_gdf.head()
print type(florence_gdf)
print type(florence_gdf['Coordinates'])

print florence_gdf[(florence_gdf['Name'] == 'Six')]
print florence_gdf.groupby('Name').Type.count()

filter_list = ('Six', 'SIX')
print florence_gdf[florence_gdf.Name.isin(filter_list)]

# generate stats
print("Mean wind speed of the Hurricane Florence is {} mph and it can go up to {} mph maximum".format(round(florence_gdf.Wind.mean(),4), florence_gdf.Wind.max()))

# plot map on screen
#florence_gdf.plot(figsize=(30,20), color='red');
#plt.show()

fig, ax = plt.subplots(1, figsize=(20,20))
base = country[country['NAME'].isin(['Alaska', 'Hawaii']) == False].plot(ax=ax, color='#3B3C6E')
florence_gdf.plot(ax=base, column='Wind', marker='<', markersize=10, cmap='cool', label="Wind speed(mph)")
#color='darkred',
_ = ax.axis('off')
plt.legend()
ax.set_title("Hurricane Florence in US Map", fontsize=25)
#plt.show()

# plot map to file
plt.savefig("data/Hurricane_footage.png", bbox_inches="tight")