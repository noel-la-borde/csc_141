# Ice Cream Stand 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print (f" Restaurant name: {self.restaurant_name}")
        print (f" Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f" The {self.restaurant_name} restaurant is open!.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors= []
    
    def describe_flavors(self):
        print("\n We have the following Ice Cream flavors:")

        for flavor in self.flavors:
            print (flavor)

ice_cream_stand= IceCreamStand ('Heaven taste', 'Ice Cream')
ice_cream_stand.flavors= ['Cheesecake', 'Chocolate', 'Vanilla', 'Strawberry', 'Caramel']

ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_flavors()

# The Ice_creamStand class is the first inheritance exercise of the chapter, 
# It took me a while to understand how it works but now if you run it it works fine. 


