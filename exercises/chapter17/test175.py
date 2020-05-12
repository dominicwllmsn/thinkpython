class Point:
	"""Represents a point in 2D Cartesian space.
	
	attributes: x, y
	"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '({},{})'.format(self.x,self.y)

	def __add__(self, other):
		if isinstance(other, Point):
			return self.add_points(other)
		elif isinstance(other, tuple):
			return self.add_to_tuple(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_points(self, other):
		result = Point(self.x+other.x, self.y+other.y)
		return result

	def add_to_tuple(self, other):
		result = Point(self.x+other[0], self.y+other[1])
		return result

def print_attributes1(obj):
	"""Useful function to check obj attribute values"""
	for attr in vars(obj):
		print(attr, getattr(obj, attr))

def print_attributes2(obj):
	"""Useful function to check obj attribute values"""
	for attr, val in vars(obj).items():
		print(attr, val)

def main():
	pos1 = Point(5, 6)
	pos2 = Point(1, 6)
	pos3 = (10,10)
	print(pos1)
	print(pos1+pos2)
	print(pos3+pos1+pos2)
	print(hasattr(pos1, 'x'))
	print(vars(pos2))
	print_attributes1(pos2)
	print('---')
	print_attributes2(pos2)

if __name__ == '__main__':
	main()