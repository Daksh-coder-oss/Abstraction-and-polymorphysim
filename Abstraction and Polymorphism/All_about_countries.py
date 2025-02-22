#Write a program to create two classes for two different countries
#  that consist of three methods
#  to display the following information of respective country - capital, language and type of country.
#  Then, use Polymorphism to create a common interface for both classes

class India():
    def capital(self):
        print("My capital is New Delhi")
    def language(self):
        print("My main language is Hindi")
    def type_of_country(self):
        print("I am a developing contry")
class UK():
    def capital(self):
        print("My capital is London")
    def language(self):
        print("My main language is English")
    def type_of_country(self):
        print("I am a developed country")
obj=India()
obj1=UK()
for i in (obj,obj1):
    i.capital()
    i.language()
    i.type_of_country()
    