# Login attemps

class User:
    
    def __init__(self, first_name, last_name, age, major):
        self.firstname = first_name
        self.last_name= last_name
        self.age= age
        self.major= major
        self.login_attemps= 0


    def describe_user(self):
        print(f" Student: {self.firstname}{self.last_name}")
        print(f" Age: {self.age}")
        print(f" Major: {self.major}")

    def greet_user(self):
        print(f"\n Hi {self.firstname}, nice to have you here.\n")    

    def increment_login_attemps(self, number):
        self.login_attemps += number
    
    def reset_login_attemps(self):
        self.login_attemps = 0


my_User= User ('Noel', 'La Borde', '23', 'Computer Science')
my_User.describe_user()
my_User.greet_user()

my_User.login_attemps= 5
print(f"{my_User.firstname} has {my_User.login_attemps} login attemps.")

my_User.increment_login_attemps(10)
print(f"{my_User.firstname} has {my_User.login_attemps} login attemps.")

my_User.reset_login_attemps()
print(f"{my_User.firstname} has {my_User.login_attemps} login attemps.")

# The modified version of the user class appeared to be tricky. 
# I was able to code it following book instructions and examples. 