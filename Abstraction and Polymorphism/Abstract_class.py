#Write a program to create a base class that consists of two functions
#  - one to display a value, 
# and another function is an abstract method.
#  Next, create a subclass that consists of a method similar to the abstract method. 
# Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC,abstractmethod
class Test:
    def display():
        print("This is displaying a value")
    @abstractmethod
    def display2():
        print("This is also displaying a value")
class Test2(Test):
    def display2():
        print("This is outside the abstraction method")
obj=Test2
obj.display2()
