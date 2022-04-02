"""
    Need to be connected to the internet
"""

# Making a map using the folium module
import folium

map = folium.Map()

# Coordinates of each place desired
companies = [
    {"loc": [37.4970, 127.0266], "label": "Samsung"},
    {"loc": [37.3318, -122.0311], "label": "Apple"},
    {"loc": [22.5431, 114.0579], "label": "Huawei"},
    {"loc": [-19.832785, -44.626488], "label": "Minha Casa"},
]

# Adding markers to the map.
for company in companies:
    marker = folium.Marker(location=company["loc"], popup=company["label"])
    marker.add_to(map)

# Save the map in HTML to visualize
map.save("/home/jose/mapa.html")
