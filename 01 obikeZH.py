
# coding: utf-8
import requests
import subprocess
import pandas as pd
import time
import random
from pprint import pprint
#import progressbar
from pygeocoder import Geocoder
import numpy as np
from geopandas import GeoDataFrame
from shapely.geometry import Point

date = time.strftime("%Y-%m-%d %H:%M:%S")

response = requests.get('https://mobile.o.bike/api/v2/bike/list', headers={'content-type': 'application/json','version': '3.2.4'}, 
	data='1152a752ff6623d245263cc1b500d38306d974dbf57110d8ace721bbaa34511e540976066d0d2d419172a34d7e1283b277d6a17091fd79d38e919ece60608c841378fef75ddf9f434067c768e88983d516a79ef7645c5d0150a3252da11ae30e20a74c8e7243c0fa1f6504536542c43c' )

response = subprocess.check_output(["curl --request POST", 
	"--url https://mobile.o.bike/api/v2/bike/list"
	, "--header 'content-type: application/json'"
	,"--header 'platform: iOS'"
	,"--header 'version: 3.2.4'"
	," --data '{ 'value': '1152a752ff6623d245263cc1b500d38306d974dbf57110d8ace721bbaa34511e540976066d0d2d419172a34d7e1283b277d6a17091fd79d38e919ece60608c841378fef75ddf9f434067c768e88983d516a79ef7645c5d0150a3252da11ae30e20a74c8e7243c0fa1f6504536542c43c'}'"])

Lil_data = response.json()
pprint(Lil_data)
'''
df = pd.DataFrame(Lil_data['data']['list'])
df = df.head(0)

a = 47.310255
b = 47.435697
c = 8.433849
d = 8.635678

# Making 2000 Random locations
lat = []
long = []
for x,y in zip(range(2000), range(2000)):
    lat.append(random.uniform(a,b))
    long.append(random.uniform(c,d))

bar = progressbar.ProgressBar()
for x, y, i in zip(long, lat, bar(range(len(long)))):
    response = requests.get('https://mobile.o.bike/api/v1/bike/list?longitude=' + str(x) +'&latitude='+ str(y))
    Lil_data = response.json()

    df_new = pd.DataFrame(Lil_data['data']['list'])
    frames = [df, df_new]
    df = pd.concat(frames)

df = df.drop_duplicates(keep='first')
df = df.reset_index()

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
df = df.drop(['longitude', 'latitude'], axis=1)
crs = {'init': 'epsg:4326'}
geo_df = GeoDataFrame(df, crs=crs, geometry=geometry)

geo_df.columns = [['index', 'countyId', 'helmet', 'id', 'imei', date]]

geo_df.to_csv(date + '2000obikesZH.csv')
'''