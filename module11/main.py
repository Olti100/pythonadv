file_path = "main.txt"
file = open(file_path, 'r')

content = file.read()
print(content)

'''
with open("main.txt", "w") as file:
    file.write('Sot eshte dite e mire dite e zotit')

'''


line = ['Hello World \n', 'Digital School \n']
with open('main.txt','w') as file:
    file.writelines(line)

import os
import datetime

file_path = 'main.txt'
if os.path.exists('main.txt'):
    print('file exists')
else:
    print('Doesnt exist')

with open('main.txt','a') as file:
    file.write('The best group ever')
    file.close()

with open('main.txt','r') as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = 'Alice'
age = 30

with open('main.txt','w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age {age}\n")

current_datetime = datetime.datetime.now()
print(current_datetime)
print('YEar:', current_datetime.year)
print('month:' ,current_datetime.month)
print('day:' ,current_datetime.day)
print('hour:' ,current_datetime.hour)
print('minute:', current_datetime.minute)
print('second:' ,current_datetime.second)
print('microsecond:', current_datetime.microsecond)

deadline_time = datetime.time(12,00,00,0000)
print(deadline_time)

print('Ora:',deadline_time.hour)
print('Minuta:',deadline_time.minute)
print('Sekonda:',deadline_time.second)
print('Milisekonda:',deadline_time.microsecond)

duration = datetime.timedelta(days= 5, hours= 3)
print(duration)

new_date = current_datetime + duration
print(new_date)

previous_date = current_datetime - duration
print(previous_date)