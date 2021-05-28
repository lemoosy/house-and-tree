# How to build a house with a tree ?


lines = 8
possibilities = {	
					0 : [1, 2, 3, 4],
					1 : [0, 2, 3, 4],
					2 : [0, 1, 3],
					3 : [0, 1, 2],
					4 : [0, 1]
				}


def errors(old_values):
	if len(old_values) <= 2:
		return False
	elif len(old_values) <= 4:
		return error_1(old_values)
	else:
		return error_1(old_values) or error_2(old_values)


# [a, b, a] >> True
def error_1(old_values):
	for cursor in range(len(old_values) - 2):
		if old_values[cursor] == old_values[cursor + 2]:
			return True
	return False


# [a, b, ..., a, b] >> True
# [a, b, ..., b, a] >> True
def error_2(old_values):
	for cursor_1 in range(len(old_values) - 3):
		for cursor_2 in range(len(old_values) - cursor_1 - 4):
			test_1 = old_values[cursor_1 : cursor_1 + 2]
			test_2 = old_values[cursor_1 + cursor_2 + 3 : cursor_1 + cursor_2 + 5]
			if test_1 == test_2 or test_1 == test_2[::-1]:
				return True
	return False


class Tree:

	def __init__(self, value, old_values = list()):
		self.value = value
		self.old_values = old_values
		self.nodes = list()

	def generate_nodes(self):
		global total
		for value in possibilities[self.value]:
			if not errors(self.old_values + [self.value]):
				node = Tree(value, self.old_values + [self.value]).generate_nodes()
				self.nodes.append(node)
				if len(self.old_values) == lines:
					print('Solution : ' + str(self.old_values + [self.value]))
					total += 1
					return

	def print(self, level = 0):
		print('  ' * level + str(self.value))
		if len(self.nodes) == 0:
			return
		for node in self.nodes:
			node.print(level + 1)


total = 0

for i in range(len(possibilities)):
	tree = Tree(i)
	tree.generate_nodes()

input('\nSolutions : ' + str(total))
