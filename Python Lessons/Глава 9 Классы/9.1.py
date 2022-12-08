class Restaraunt():
	def __init__(self,restaraunt_name,cuisine_type):
		self.restaraunt_name = restaraunt_name
		self.cuisine_type = cuisine_type

	def describe_restaraunt(self):
		print(f"The restaraunt name is {self.restaraunt_name.title()}")
		print(f"Cuisine type: {self.cuisine_type}")

	def open_restaraunt(self):
		print(f"\nThe {self.restaraunt_name.title()} is open!")

my_rastaraunt = Restaraunt('veranda','italian')
my_rastaraunt.describe_restaraunt()
my_rastaraunt.open_restaraunt()
