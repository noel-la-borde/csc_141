# Three Restaurants


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print (f" Restaurant name: {self.restaurant_name}")
        print (f" Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f" The {self.restaurant_name} restaurant is open!.\n")

    
    def multiple_instances(self):
        print(f"{self.restaurant_name} has people fascinated with its {self.cuisine_type} cuisine.")


my_restaurant= Restaurant('Garlic & Oregano', 'Hispanic')    
my_restaurant01= Restaurant ('Hells Kitchen','American')
my_restaurant02= Restaurant ('Catedralle', 'Italian')
my_restaurant03= Restaurant ('Plaza Azteca','Mexican')    

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant01.multiple_instances()
my_restaurant02.multiple_instances()
my_restaurant03.multiple_instances()

# This exercise, being the second one appeared to be a little bit complex.
# Following the book example I was able to make it. 
