from user import User

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
