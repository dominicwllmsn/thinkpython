import time

epoch_time = time.time()

one_day = 60*60*24
current_time = epoch_time%one_day # today's time in seconds
hours = current_time//3600
mins = current_time%3600//60
secs = (current_time%3600/60)%1*60

time_now = '{}:{}:{}'.format(int(hours),int(mins),int(secs))
print('Current time is:', time_now)
print('Number of days since epoch:', int(epoch_time//one_day))