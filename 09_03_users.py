# Users 

class User:
    
    def __init__(self, first_name, last_name, age, major):
        self.firstname = first_name
        self.last_name= last_name
        self.age= age
        self.major= major

    def describe_user(self):
        print(f" Student: {self.firstname}{self.last_name}")
        print(f" Age: {self.age}")
        print(f" Major: {self.major}")

    def greet_user(self):
        print(f"\n Hi {self.firstname}, nice to have you here.")      

my_User= User ('Noel', 'La Borde', '23', 'Computer Science')
my_User.describe_user()
my_User.greet_user()

# The user class was clear and simple to code and understand. 