import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
# print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

m = folium.Map(location=[38.00, -50.33], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="New Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color="blue")))
    m.add_child(fg)
m.save("new_map.html")
