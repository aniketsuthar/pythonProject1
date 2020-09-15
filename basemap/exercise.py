import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])

m = folium.Map(location=[38.22, -100.00], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

fgp = folium.FeatureGroup(name="Population")


def get_color(elevation):
    if elevation < 1000:
        return "green"
    elif 3000 > elevation >= 1000:
        return "orange"
    else:
        return "red"


for lt, ln, el in zip(lat, lon, ele):
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], radius=10, popup=str(el) + " m", color="gray",
                            fill_color=get_color(el), fill=True, fill_opacity=1.0))

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'
                                                       }))
m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())

m.save("latest_m_circle_sep.html")
