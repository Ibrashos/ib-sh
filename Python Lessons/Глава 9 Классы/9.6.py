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

class IceCreamStand(Restaraunt):
	def __init__(self,restaraunt_name,cuisine_type):
		super().__init__(restaraunt_name,cuisine_type)
		self.flavors = ['fruity','vanilla','berry']

	def read_ice(self):
		for flavor in self.flavors:
			print(flavor.title())

my_ice_stand = IceCreamStand('vaniley','irish')
my_ice_stand.read_ice()
