import datetime

from module11.main import deadline_time

current_datetime = datetime.datetime.now()
print(current_datetime)
print('YEar:', current_datetime.year)
print('month:' ,current_datetime.month)
print('day:' ,current_datetime.day)
print('hour:' ,current_datetime.hour)
print('minute:', current_datetime.minute)
print('second:' ,current_datetime.second)
print('microsecond:', current_datetime.microsecond)

duration = datetime.timedelta(days=100)
new_date = current_datetime + duration
print(new_date)

previous_date = current_datetime - duration
print(previous_date)

deadline_time = datetime.datetime(2026,6,12,3,20,50,12345)
print(deadline_time)