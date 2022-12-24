class User():
	def __init__(self,first_name,last_name,country,age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country
		self.login_attempts = 0
	def describe_user(self):
		print(f"\nСводка о пользователе:\n\tполное имя: {self.first_name.title()} {self.last_name.title()}\n\tвозвраст: {self.age}\n\tcтрана: {self.country.title()}")

	def increment_login_attempts(self,num):
		if num >= 0:
			self.login_attempts += num

	def reset_login_attempts(self):
		self.login_attempts = 0

	def read_login_attempts(self):
		print(f"Attempts: {self.login_attempts}")

alien = User('garry','kuper','mars','544')
alien.describe_user()

alien.increment_login_attempts(10)
alien.read_login_attempts()
alien.reset_login_attempts()
alien.read_login_attempts()