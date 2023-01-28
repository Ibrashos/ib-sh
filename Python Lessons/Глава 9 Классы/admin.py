from user import User
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