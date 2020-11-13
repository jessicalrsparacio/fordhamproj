#Name: Jessica Lauren Sparacio
#Email: jessica.sparacio40@myhunter.cuny.edu
#Assignment: Fordham Listings Map

import folium
import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv("airbnb.csv")
boro_group = airbnb.groupby(['neighbourhood_group'])
bronx = airbnb[airbnb['neighbourhood_group'] == 'Bronx']
fordonly = airbnb[airbnb['neighbourhood'] == 'Fordham']

mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)

for index,row in fordonly.iterrows():
    lat = row["latitude"]
    lon = row["longitude"]
    name = row["name"]
    newMarker = folium.Marker([lat, lon])
    newMarker.add_to(mapNYC)

mapNYC.save(outfile='nycMap.html')
