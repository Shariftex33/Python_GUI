# Import the Folium library
import folium

# Create a base map centered at a specific location (e.g., New York City)
map_center = [40.7128, -74.0060]
my_map = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map (e.g., Times Square)
marker_location = [40.758896, -73.985130]
folium.Marker(
    location=marker_location,
    popup='Times Square',
    icon=folium.Icon(icon='cloud')
).add_to(my_map)

# Add a circle to the map (e.g., Central Park)
circle_location = [40.785091, -73.968285]
folium.Circle(
    location=circle_location,
    radius=1000,  # in meters
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(my_map)

# Save the map to an HTML file
my_map.save('interactive_map.html')

# Open the map in a web browser
import webbrowser
webbrowser.open('interactive_map.html')
