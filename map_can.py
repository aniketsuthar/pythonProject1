import folium

m = folium.Map(location=[80, -100], zoom_start=10, tiles="Stamen Terrain")
m.save("Map2.html")
