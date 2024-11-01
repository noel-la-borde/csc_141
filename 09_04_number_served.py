# Number Served 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print (f" Restaurant name: {self.restaurant_name}")
        print (f" Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f" The {self.restaurant_name} restaurant is open!.")
    
    def set_number_served(self, number):
        self.number_served= number
    
    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

    

my_restaurant= Restaurant("Garlic & Oregano", 'Hispanic')     

print(f"{my_restaurant.restaurant_name} have served {my_restaurant.number_served} tables today so far.")

my_restaurant.number_served= 20 
print(f"{my_restaurant.restaurant_name} just served {my_restaurant.number_served} customers after the fisrt count.")

my_restaurant.set_number_served(50)
print(f"After the second count, {my_restaurant.restaurant_name} served {my_restaurant.number_served} new customers")

my_restaurant.increment_number_served(30)
print(f"In their last count, {my_restaurant.restaurant_name} served {my_restaurant.number_served} customers.\n")


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# I did this exercise in one of the labs and it took me a while until I got it. 
# As soon as you understand how classes work everything starts to look simple. 
