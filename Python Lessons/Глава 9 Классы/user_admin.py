class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = f"{self.first_name.title()} {self.last_name.title()}"

	def describe_user(self):
		print(f"\nСводка о пользователе:\n\tfull name: {self.full_name.title()}")

	def greet_user(self):
		print(f"Hello, {self.full_name}!")

class Privilages():
	def __init__(self):
		self.privilages = ['add message','delete user','ban user']

	def show_privilages(self):
		print('Privilages:')
		for privilage in self.privilages:
			print(privilage.title())

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privilages = Privilages()

# admin = Admin('garry','kaspar')
# admin.greet_user()
# admin.privilages.show_privilages()