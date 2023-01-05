from car import Car

#Battery part
class Battery():
	def __init__(self,size):
		self.size = size

	def describe_battery(self):
		print(f"Battery size: {self.size}kwh")


#Electro Car
class ElectricCar():
	def __init__(self,model,year):
		super().__init__(model,year)
		self.battery = Battery()

my_car = ElectricCar('','')