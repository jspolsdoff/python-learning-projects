# was not able to initially install the folium due to python 2.x
# changed path to new python 3 using the following commmands
# $ sudo mv /usr/bin/python /usr/bin/python2
# $ sudo ln -s /usr/bin/python3 /usr/bin/python
# finally check version with python --version
# was then able to install folum via pip

#Import Library
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#Load Data
data = pd.read_csv("data/Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "Mapbox bright")

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Plot Markers and add to 'marker_cluster'
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)

#Save the map
map.save("map1.html")
