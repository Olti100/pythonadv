#functions
def greet():
    print('hello world')
greet()

def shuma (num1,num2):
    rezultati=num1+num2
    print (rezultati)

shuma(10,5)
shuma(20,10)

def pershendetja(name):
    print(f'Hello {name}')
pershendetja('Olti')
pershendetja('Ylli')

hello = "Pershendetje"
def pershendetja(name,age):
    print(f'{hello} dear ,{name} your age is {age}')
pershendetja("Olti", 16)

#default arguments
def welcome(name,mesazhi="Hello"):
    print(f'{mesazhi} dear {name}')
welcome("Olti")