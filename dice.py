from random import randint

class Dice:
	def __init__(self, sides=6):
		self.sides=sides

	def roll(self):
		return randint(1, self.sides)
	

