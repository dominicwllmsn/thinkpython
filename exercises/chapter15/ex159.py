import math

class Point:
	"""Represents a Cartesian coordinate.
	
	attributes: x, y
	"""


class Circle:
	"""Represents a circle.

	attributes: centre (Point), radius (number)
	"""


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def dist_between_points(p1, p2):
	dx = p2.x - p1.x
	dy = p2.y - p1.y
	return math.sqrt(dx*dx + dy*dy)


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


def point_in_circle(circ, p):
	return dist_between_points(circ.centre, p) <= circ.radius


def rect_in_circle(circ, rect, n):
	"""n is minimum no. of corners required inside circle"""
	c = Point()
	i = 0
	for x in [rect.corner.x, rect.corner.x+rect.width]:
		c.x = x
		for y in [rect.corner.y, rect.corner.y+rect.height]:
			c.y = y
			if point_in_circle(circ, c):
				i += 1
	return i >= n


def rect_circle_overlap(circ, rect):
	"""True if atleast one corner inside circle"""
	return rect_in_circle(circ, rect, 1)


def rect_circle_overlap_adv(circ, rect):
	"""Return True if any part of rectangle in circle"""
	# for loop recreating each point of rect
	# check if this point is inside circle
	# if so, return true
	# maybe start with the points near corner that is closest to centre
	c = Point()
	for x in range(rect.corner.x, rect.corner.x+rect.width+1):
		c.x = x
		for y in range(rect.corner.y, rect.corner.y+rect.height+1):
			c.y = y
			if point_in_circle(circ, c):
				return True
	return False
	

def draw_axes(t):
	pass


def draw_rect(t, rect):
	#Draw x, y axes
	pass


def draw_circle(t, circ):
	#Draw x, y axes
	#Using centre and radius, draw an accurate circle 
	pass


def main():
	circ = Circle()
	circ.centre = Point()
	circ.centre.x = 100
	circ.centre.y = 100
	circ.radius = 75

	rect = Rectangle()
	rect.corner = Point()
	rect.corner.x = 0
	rect.corner.y = 0
	rect.width = 50
	rect.height = 50

	print(rect_in_circle(circ, rect, 4))
	print(rect_circle_overlap_adv(circ, rect))


if __name__ == '__main__':
	main()