class Restaraunt():
	def __init__(self,rastaraunt_name,cuisine_type):
		self.rastaraunt_name = rastaraunt_name
		self.cuisine_type = cuisine_type

	def describe_restaraunt(self):
		print(f"Название ресторана: {self.rastaraunt_name.title()}")
		print(f"Тип кухни: {self.cuisine_type}")

	def restraunt_open(self):
		print(f"{self.rastaraunt_name.title()} открыт!")

my_restaraunt = Restaraunt('Веспучи','Американская')
my_restaraunt.describe_restaraunt()

dad_restaraunt = Restaraunt('santiago','irish')
dad_restaraunt.describe_restaraunt()

son_restaraunt = Restaraunt('bunker','russian')
son_restaraunt.describe_restaraunt()