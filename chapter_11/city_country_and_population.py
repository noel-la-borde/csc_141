# city, country, and population 

def city_and_country(city, country, population=''):
   # city_country= f"{city}, {country}"
    if population:
        city_country= f"{city}, {country}, {population}"
    else: 
        city_country= f"{city}, {country}"
    return city_country

# Pretty much like the original city and country function, just added the population attribute. 