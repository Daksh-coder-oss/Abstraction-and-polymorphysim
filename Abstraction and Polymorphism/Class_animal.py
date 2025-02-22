#Write a program to implement abstraction on animal class (base class)
# . The abstract method will be move will display what subclasses can do.
#  Subclasses can be something like - Human, Dog.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def implement(self):
        pass
class Human(Animal):
    def implement(self):
        print("I can walk and I can run")
class Snake(Animal):
    def implement(self):
        print("I can crawl")
class Dog(Animal):
    def implement(self):
        print("I can bark")
obj=Human()
obj.implement()
obj1=Snake()
obj1.implement()
obj3=Dog()
obj3.implement()


    