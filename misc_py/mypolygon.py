import turtle

def square(t, length):
	polyline(t,4,length,90)


def polyline(t, n, length, angle):
	"""Draws n line segments of given length and angle
	(in degrees) between them. t is a turtle.
	"""
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def polygon(t, n, length):
	ext_angle = 360/n
	polyline(t,n,length,ext_angle)

def circle(t, r):
	c = 2*3.14*r
	n = int(c/3) + 3
	step_length = c/n
	step_angle = 360/n
	polyline(t,n,step_length,step_angle)

def arc(t, r, angle):
	arc_length = 2*3.14*r*angle/360
	n = int(arc_length/3) + 3
	step_length = arc_length/n
	step_angle = angle/n
	polyline(t,n,step_length,step_angle)

bob = turtle.Turtle()
print(bob)

square(bob, 100)
arc(bob, r=100, angle=90)

turtle.mainloop()