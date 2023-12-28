import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


filename = 'population_data.json'

# Load JSON data
with open(filename) as f:
    pop_data = json.load(f)

# Print the structure of the JSON data
for country_data in pop_data:
    print(country_data['Country Name'], country_data['Year'], country_data['Value'])


cc_populations = {}
for country_data in pop_data:
    country_name = country_data['Country Name']
    population = int(float(country_data['Value']))
    year = int(country_data['Year'])
    
    if year == 2018:
        cc_populations[country_name] = population

# Customization
wm_style = LS('#336699', base_style=LCS)

# Create a world map with population data for the year 2018
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2018, by Country'
wm.add('2018', cc_populations)

# Save the map to an SVG file
wm.render_to_file('world_population.svg')
