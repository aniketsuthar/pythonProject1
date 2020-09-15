import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])

m = folium.Map(location=[38.22, -100.00], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")


def get_color(elevation):
    if elevation < 1000:
        return "green"
    elif 3000 > elevation >= 1000:
        return "orange"
    else:
        return "red"


for lt, ln, el in zip(lat, lon, ele):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) +
                                                        " m", icon=folium.Icon(color=get_color(el))))

m.add_child(fg)
m.save("latest_map.html")
