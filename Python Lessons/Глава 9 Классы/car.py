class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometr_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

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
my_used_car = Car('subaru','outback','2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increment_odometr(100)
my_used_car.read_odometr()


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometr_reading = 23
# my_new_car.read_odometr()
# while True:
# 	my_new_car.update_odometr(int(input('enter mil')))
# my_new_car.read_odometr()