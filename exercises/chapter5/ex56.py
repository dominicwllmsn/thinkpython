import turtle 

def koch(t, x):
	if x < 3:
		t.fd(x)
	else:
		koch(t, x/3)
		t.lt(60)
		koch(t, x/3)
		t.rt(120)
		koch(t, x/3)
		t.lt(60)
		koch(t, x/3)

def snowflake(t, x):
	koch(t,x)
	t.rt(120)
	koch(t,x)
	t.rt(120)#
	koch(t,x)
	t.rt(120)

bob = turtle.Turtle()
print(bob)

snowflake(bob, 50)

turtle.mainloop()