class LR:
	def __init__(self, height, width):
		print("Linear regression object created")
		self.height = height
		self.width = width

	def draw_linear_line(self, slope, intercept):

		y_coordinates = [y for y in range(intercept, self.height, slope)]

		space = 6
		for i in range(self.height, 0, -1):
			print(i, end = ' ' * (space - len(str(i)) + 1))
			for j in range(len(y_coordinates)):
				if i == y_coordinates[j]:
					print('o', end = ' ')
				else:
					print('', end = ' ' * (space + 1))
			print("")

		print(' ', end = '')
		for i in range((space + 1) * self.width):
			print("-", end = '')
		print(">", end = '')
		print("")

		print(' ', end = ' ' * space)
		for i in range(self.width):
			if len(str(i)) == 1:
				print(i, end = ' ' * (space))
			else:
				print(i, end = ' ' * (space - len(str(i)) + 1))

		print()


	# regression finds the relationship between variables (people, animal, colleges, students, ...)
	# linear regression algorithm: create the best fit line that minimizes the discrepancies between predicted and actual output values
	def linearResgression(self, coordinates, newX):
		pass

LR1 = LR(40, 20)
LR1.draw_linear_line(4, 3)