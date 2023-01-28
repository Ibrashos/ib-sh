from random import randint
class Die():
	def __init__(self):
		self.sides = 6

	def set_sides(self):
		if self.sides == 6:
			self.sides = 10
		elif self.sides == 10:
			self.sides = 20
		elif self.sides == 20:
			self.sides = 6

	def roll_die(self):
		num = randint(1,self.sides)
		print(num)

brick = Die()
brick.roll_die()
brick.set_sides()
brick.roll_die()
brick.set_sides()
brick.roll_die()