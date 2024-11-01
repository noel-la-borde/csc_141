# Battery Upgrade 

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Battery class with upgrade_battery method
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it is less than 65."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at 65 kWh.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_toyota = ElectricCar('Toyota', 'BZ4X', 2024)
print(my_toyota.get_descriptive_name())
my_toyota.battery.describe_battery()
my_toyota.battery.get_range()

my_toyota.battery.upgrade_battery()
my_toyota.battery.get_range()

# This exercise is very extended compared to the previous ones. 
# Most of this code is taken from the book. 