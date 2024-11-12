# Employee 

class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name= first_name
        self.last_name= last_name
        self.annual_salary= annual_salary
    
    def give_raise(self, amount= 5000):
        self.annual_salary += amount

# I was able to code this class on my own as well, but I felf a little unsecure about the give_raise method. 
# I had to take some reference from the github files. 
        
