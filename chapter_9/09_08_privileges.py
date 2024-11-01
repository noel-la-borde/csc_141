# Privileges

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

class Privileges:

    def __init__(self, privileges= None):
        if privileges is None:
            privileges= ['Can add post', 'Can delete post', 'Can ban user'] 
        self.privileges= privileges
    
    def show_privileges(self):
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, age, major):
        super().__init__(first_name, last_name, age, major)
        self.privileges= Privileges()


admin_user= Admin('Noel', 'La Borde', '23', 'Computer Science')
admin_user.describe_user()
admin_user.privileges.show_privileges()

# While I was coding this one I got stuck and had to test my code in Chat looking for errors to fix. 
