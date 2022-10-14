# Description of the problem

There are data for several years from the Yandex Real Estate service. It is necessary to analyze the advertisements for the sale of apartments. Find the dependence of the price per square meter on other parameters of the apartment. Separately analyze sales in St. Petersburg and find where its center ends.

# Description of data

Column names:
- airports_nearest —distance to the nearest airport in meters (m)
- balcony - number of balconies
- ceiling_height - ceiling height (m)
- cityCenters_nearest - distance to the city center (m)
- days_exposition - how many days the ad was placed (from publication to removal)
- first_day_exposition — publication date
- floor - floor
- floors_total - total floors in the house
- is_apartment - apartments (boolean type)
- kitchen_area - kitchen area in square meters (m²)
- last_price - price at the time of removal from publication
- living_area - living area in square meters (m²)
- locality_name - name of the locality
- open_plan - free layout (boolean type)
- parks_around3000 - number of parks within a 3 km radius
- parks_nearest - distance to the nearest park (m)
- ponds_around3000 - number of ponds within a radius of 3 km
- ponds_nearest — distance to the nearest body of water (m)
- rooms - number of rooms
- studio - studio apartment (boolean type)
- total_area - area of the apartment in square meters (m²)
- total_images - the number of photos of the apartment in the ad

# Used library

1.pandas
2.matplotlib.pyplot

# What was done

- Conducted primary data analysis for gaps, duplicates and artifacts.
- Spared DF from emissions
- Graphs of distribution of various parameters of the apartment are built
- Carried out the correlation of the dependence of the price on the parameters
- Found a dozen record cities for ads and found the average cost per square meter
- Analyzed ads in St. Petersburg and found its center

# Result

Based on the results of the study, we can draw logical conclusions that the final price directly depends on the area, distribution, number of rooms (a special case of the area), distance from the city center and the city itself. In megacities, the price is objectively higher than in the depths. In the center of a big city, the price per square meter practically does not depend on anything.
