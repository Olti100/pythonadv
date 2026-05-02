""" import emoji as e
import my_math as m
from m import square

def ssquare(x):
    print(x*x)

result = m.square(3)
print(result)

ssquare(3)
print(e.emojize("Python is so nice :snake:"))
"""

#functions
def gpa(g1,g2,g3,g4,g5,g6):
    shuma = g1+g2+g3+g4+g5+g6
    rezultati_final = shuma / 6
    print(rezultati_final)
    if rezultati_final >= 3.5:
        print('You can go to Harvard')
    else:
     print('You can go to Sami Frasheri')

gpa(2,2,2,3,4,5)

def test(x):
    if x > 0:
        print('Its a positive number')
    elif x == 0:
        print('Itss 0')
    else:
        print('Its a negative number')

    if x % 2==0:
        print('Its an even number')
    else:
        print('Its an odd number')

test(6)

import random
import string
colors = ['yellow','red','black','green','blue','purple','pink']
shapes = ['triangle','circle','square','diamond','Hexagon']

print('Welcome to Password Generator')

while True:
    ngjyra = random.choice(colors)
    forma = random.choice(shapes)
    number = random.randint(1,10)
    char = random.choice(string.punctuation)

    password = ngjyra + forma + str(number) + char
    print('Your new passwprd is: %s' %password)

    response=input('U like your new password, do you want a new one? Type y or n')
    if response== 'n':
        break