# Admin

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

class Admin(User):

    def __init__(self, first_name, last_name, age, major):
        super().__init__(first_name, last_name, age, major)
        self.privileges= ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(privilege)

admin_user= Admin('Noel', 'La Borde', '23', 'Computer Science')
admin_user.describe_user()
admin_user.show_privileges()

# This exercise made me go back to file 09_03 to create an inheritance class. 
# It wasn't as hard as the previous exercise from my perspective. 
