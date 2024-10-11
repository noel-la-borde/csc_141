# Extensions


city_1= {'City': 'New York', 
         'Country': 'United States of America', 
         'Population': '333.3 million', 
         'Fact': 'that the USA is the third largest country in the world in terms of landmass',
         'Most popular food or plate': 'Pizza',
         'Weather': 'Mostly cold except for summer time' }

city_2= {'City': 'Bogota', 
         'Country': 'Colombia', 
         'Population': '51.7 million', 
         'fact': 'Colombia is the country with the greatest biodiversity on the planet',
         'Most popular food or plate': 'Paisa Platter',
         'Weather': 'Annual average maximum temperature is 78f/30c, creeping down to 54f/12c at night.'
         }

city_3= {'City': 'Santo Domingo', 
         'Country': 'Dominican Republic', 
         'Population': '11.23 million', 
         'fact': 'that the Dominiocan Republic is the site of the oldest colonial settlement in the Americas.',
         'Most popular food or plate': 'The Dominican Flag',
         'Weather': 'Warm and humid conditions associated with the Tropics'
         }

for (key, value) in city_1.items():
     print(f" The {key} is {value}")
print("\n")
for (key, value) in city_2.items():
     print(f" The {key} is {value}")
print("\n")
for (key, value) in city_3.items():
     print(f" The {key} is {value}")
print("\n")

# I decided to modify the previous asignment I just created by adding two more keys to my dictionaries. 
# Each key gets displayed along with the information stored. 