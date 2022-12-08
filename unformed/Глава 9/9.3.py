class User():
	def __init__(self,first_name,last_name,age,country):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country

	def describe_user(self):
		print(f"Сводка о пользователе:\n\tfull name: {self.first_name.title()} {self.last_name.title()}\n\tage: {self.age}\n\tcountry: {self.country.title()}\n")



first_user = User('alex','mikey',22,'usa')
first_user.describe_user()

second_user = User('mike','willie',32,'montenegro')
second_user.describe_user()

third_user = User('ivan','ivanov',45,'russia')
third_user.describe_user()