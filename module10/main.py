#Define the Student class
class Student:
    def __init__(self,name,age):
        #initialize private attributes
        self.__name= name
        self.__age = age

        #Getter method for name
        def get_name(self):
            return self.__name

        #Setter method fro name
        def set_name(self,name):
            self.__name = name

        #Getter method for age
        def get_age(self):
            return self.__age

        #Setter method for age
        def set_age(self,age):
            self.__age = age


#Creating an insatnce of Student
student1 = Student('Alice', 17)
#Using getter and setter methods
print('Name:', student1.get_name()) #Output: Name:Alice
student1.set_name("BOB")
print("Updated Name:", student1.get_name())#Output: updated Name: bob

print("Age:", student1.get_age())#Output: Age: 17
student1.set_age(18)
print("Updated Age:", student1.get_age())#Output: Updated AGe: 18

# Import the ABC class and the abstract method decorator from the abc module

from abc import ABC, abstractmethod

#Define a new class named 'Shape' that inherits from 'ABC'
class Shape(ABC):
    #Use the @abstractmethod decoratpr to declare 'area' as an abstract method
    @abstractmethod
    def area(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, length):
        self.length = length


    def area(self):
        return self.length * self.length




circle1=circle(7)
square1 = Square(10)

print(circle1.area())
print(square_1.area())
