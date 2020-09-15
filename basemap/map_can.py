import folium
import pandas

m = folium.Map(location=[80, -100], zoom_start=6, tiles="Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]

# Use Feature group to add child to your map and  keep code organised.also helps when you add Layer control feature
fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am marker", icon=folium.Icon(color="red")))

m.add_child(fg)
m.save("Map6.html")