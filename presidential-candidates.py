import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

df = pd.read_csv('1976-2020-president.csv')
df = df.rename(columns={"state_po":"state_code"})

geo_df = gpd.read_file('tl_2020_us_state.shp')
geo_df = geo_df[["STUSPS", "geometry"]].rename(columns={"STUSPS":"state_code"})

#dataframe = dataframe[["year","state", "candidate", "party_simplified"]]
geometry = geo_df[["geometry"]]
party_of_state = df.groupby(["state_code"], as_index=False)["candidate"].count()

geo_df = geo_df.merge(party_of_state, on="state_code", how='left')
#print(party_of_state.head())
geo_df.plot(column = "candidate", legend = True)
plt.xlim(-200,-50)
plt.savefig('geo_df.png', dpi = 300)