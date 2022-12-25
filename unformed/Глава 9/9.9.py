class Car():
	def __init__(self,model,year):
		self.model = model
		self.year = year
		self.odometr_num = 0

	def describe_car(self):
		print(f"Car Description: {self.model.title()} {self.year}")

	def odometr(self):
		print(f"Miles: {self.odometr_num}")

	def update_odometr(self,miles):
		if miles >= 0:
			self.odometr_num += miles
		else:
			print('pls enter correct number!')

	def ent_odometr(self,miles):
		if miles >= self.odometr_num:
			self.odometr_num = miles
		else:
			print("You can't roll back")

my_car = Car('nissan',2005)


my_car.describe_car()
my_car.odometr()
my_car.update_odometr(20)
my_car.odometr()
my_car.ent_odometr(21)
my_car.odometr()