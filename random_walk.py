from random import choice

class RandomWalk:
	def __init__(self, num_points=5000):
		self.num_points = num_points

		self.x = [0]
		self.y = [0]

	def fill_walk(self):
		for i in range(self.num_points):
			step_x = choice([-1, 1]) * choice([0, 1, 2, 3, 4])
			step_y = choice([-1, 1]) * choice([0, 1, 2, 3, 4])

			if not step_x and not step_y:
				continue

			self.x.append(step_x + self.x[-1])
			self.y.append(step_y + self.y[-1])