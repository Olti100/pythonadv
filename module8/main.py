class Student:
    def __init__(self,name,percentage):
        self.name=name
        self.percentage=percentage


    def show(self):
        print("Name is:",self.name,"and percentage is:", self.percentage)



studenti = Student('Olti', 50)

studenti.show()
#variabla publike
class Myclass:
    def __init__(self):
        self.pv = 'this is a public variable'


myclass=Myclass()
print(myclass.pv)

#variabla protected
class klasaime:
    def __init__(self):
        self._protectedv = 'This is a protected variable'

    def protected_method(self):
        print('This is a protected variable')

klasa = klasaime()
print(klasa.protected_method)

#variabla private

class one_d:
    def __init__(self):
        self.__private_var = 'this is a private variable'
teacher=one_d()
print(teacher.__private_var)
