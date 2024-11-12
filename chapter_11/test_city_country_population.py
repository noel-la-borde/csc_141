from city_country import city_and_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me the name of your city: ")
    if city == 'q':
        break
    country = input("Please give me the name of your country: ")
    if country == 'q':
        break
    population= input("What is the population? ")
    if population =='q':
        break

    city_country= city_and_country(city, country, population)
    print(f" Geographic Information: {city_country}.")

    # Pretty much like the city_country test file, just added population to the equation.