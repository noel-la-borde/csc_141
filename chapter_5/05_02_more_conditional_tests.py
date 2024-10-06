# More Conditional Tests 

# Equality & Inequality using strings
ice_cream = 'Caramel'
print ("I predict that Noel's favorite ice cream flavor is Caramel.")
print (ice_cream == 'Caramel')
print ("\nI predict that Noel's favorite ice cream flavor is Strawberry.")
print (ice_cream == 'Strawberry')

favorite_color= 'Blue'
print ("\nI predict that Noel's favorite color is blue.")
print(favorite_color == 'Blue')

favorite_color= 'Green'
print ("\nI predict that Noel's favorite color is Green.")
print (favorite_color == 'Blue')
if favorite_color != 'Blue':
    print("Wrong answer\n")

# Tests using the lower() method
car= 'Mazda'
print ("\n I predict Noel's favorite car maker is Mazda")
print(car.lower() == 'mazda')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age= '23'
print ("\n I predict Noel's age is 23")
print (age == "23")
age= '24'
print ("\n I predict Noel's age is 24")
print (age == '23')
if age != '23':
    print("Wrong age")
age=23
print( "\nIs Noel's age greater than 21?")
print (age>=21)
print( "\nIs Noel's age less than 19?")
print (age<=21)
# Tests using the and keyword and the or keyword 
age_01= 26
age_02= 27
print("\n Is age 1 greater or equal to 26 and age 2 less or equal than 26?")
print (age_01 >= 23 and age_02 <= 26)


print("\n Is age 1 greater or equal to 26 OR age 2 less or equal than 26?")
print (age_01 >= 26 or age_02 <= 27)

# Test whether an item is in a list
ages= ['21', '22', '23', '24', '25']
print ("\n Is age 24 in the ages list?")
print('24' in ages)
# Test whether an item is not in a list
print ("\n Is age 26 in ages lists?")
print ('26' in ages)
