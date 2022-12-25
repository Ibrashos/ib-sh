class Car():
	def __init__(self,model,year):
		self.model = model
		self.year = year
		self.odometr_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.model} {self.year}"
		print(long_name.title())

	def read_odometr(self):
		print(f"This car has {self.odometr_reading} miles on it.")

	def update_odometr(self,mileage):
		if mileage >= self.odometr_reading:
			self.odometr_reading = mileage
		else:
			print("You can't roll back an odometr")

	def increment_odometr(self,miles):
		if miles >= 0:
			self.odometr_reading += miles
		else:
			print("You can't roll negative up")
	def fill_gas_tank(self):
		print("This car need gas tank!")

class Battery():
	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kwh battery.")

	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size != 100:
			self.battery_size = 100
		else:
			print("Battery Size = 100")


class ElectricCar(Car):

	def __init__(self,model,year):
		super().__init__(model,year)
		self.battery = Battery()

	def fill_gas_tank(self):
		print("This car doesn't need a gas tank!")	

my_tesla = ElectricCar('tesla', 2015)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery() #Update battery size (100)
print("\n") 
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
