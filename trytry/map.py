import folium

# Create map object
map1 = folium.Map(location=[-6.8915, 107.6107], zoom_start=20)

# global tooltip
tooltipG = "Click for more info"

# create Markers
folium.Marker([-6.892650, 107.610433],
              popup = '<strong>Location 1</strong>',
              tooltip = tooltipG).add_to(map1),

folium.Marker([-6.892650, 107.608763],
              popup = '<strong>Location 2</strong>',
              tooltip = tooltipG).add_to(map1),

folium.Marker([-6.891056, 107.608712],
              popup = '<strong>Location 3</strong>',
              tooltip = tooltipG).add_to(map1)



# map1.simple_marker(location=[-6.8915, 107.6107], popup='<strong>Location 4</strong>')
# map1.click_for_marker(popup='Waypoint')
# map1.create_map(path='map.html')


# Generate map
map1.save('map.html')