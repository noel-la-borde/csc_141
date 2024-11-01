# Restaurant 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print (f" Restaurant name: {self.restaurant_name}")
        print (f" Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f" The {self.restaurant_name} restaurant is open!.")

my_restaurant= Restaurant("Garlic & Oregano", 'Hispanic')        

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()




        