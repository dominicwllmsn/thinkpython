import datetime

def current_day():
	today = datetime.date.today()
	print(today)
	day = today.weekday()
	weekdays = {0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
	print(weekdays[day].title())

def age(bday):
	"""Takes birthday in format YYYY-MM-DD"""
	year = int(bday[:4])
	month = int(bday[5:7])
	day = int(bday[8:])
	then = datetime.datetime(year, month, day)
	now = datetime.datetime.now()
	diff = (now-then).total_seconds()
	age, quot = divmod(diff, 31536000)
	secs_to_bday = 31536000-quot
	bday_delta = datetime.timedelta(seconds=secs_to_bday)

	print(int(age))
	print(bday_delta)



if __name__ == '__main__':
	current_day()
	age('1998-05-25')