class Restaraunt():
	def __init__(self,restaraunt_name,cuisine_type):
		self.restaraunt_name = restaraunt_name
		self.cuisine_type = cuisine_type
		self.number_saved = 0
	def describe_restaraunt(self):
		print(f"The restaraunt name is {self.restaraunt_name.title()}")
		print(f"Cuisine type: {self.cuisine_type.title()}")

	def open_restaraunt(self):
		print(f"\nThe {self.restaraunt_name.title()} is open!")

	def read_number(self):
		print(f"Number of visitors served: {self.number_saved}")

	def set_number_served(self,num):
		self.number_saved = num

	def increment_number_served(self,num):
		if num >= 0:  # check negative number
			self.number_saved += num
		else:
			print("Please correct number!")


restaraunt = Restaraunt('josper grill','russian')
restaraunt.describe_restaraunt()
restaraunt.set_number_served(10)
restaraunt.read_number()

restaraunt.open_restaraunt()
restaraunt.increment_number_served(19)
restaraunt.read_number()