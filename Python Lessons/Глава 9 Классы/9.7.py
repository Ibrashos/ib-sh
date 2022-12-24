class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = f"{self.first_name.title()} {self.last_name.title()}"

	def describe_user(self):
		print(f"\nСводка о пользователе:\n\tfull name: {self.full_name.title()}")

	def greet_user(self):
		print(f"Hello, {self.full_name}!")

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privilages = ['добавлять сообщения','удалять пользователей','банить пользователей']

	def show_privilages(self):
		print('Разрешено:')
		for privilage in self.privilages:
			print(privilage.title())

admin = Admin('garry','manjaro')
admin.greet_user()
admin.show_privilages()


