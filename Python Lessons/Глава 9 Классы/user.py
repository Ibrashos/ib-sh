class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = f"{self.first_name.title()} {self.last_name.title()}"

	def describe_user(self):
		print(f"\nСводка о пользователе:\n\tfull name: {self.full_name.title()}")

	def greet_user(self):
		print(f"Hello, {self.full_name}!")