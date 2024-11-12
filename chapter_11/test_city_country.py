from city_country import city_and_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me the name of your city: ")
    if city == 'q':
        break
    country = input("Please give me the name of your country: ")
    if country == 'q':
        break

    city_country= city_and_country(city, country)
    print(f" Geographic Location: {city_country}.")

# Very easy implementation, I did it folowing the same concept the book has for this exercise. 