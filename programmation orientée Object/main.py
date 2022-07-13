#difference between imperative programming 
"""
def show_informations_person (name, age):
    print(f"The name of the person is {name} his age is {age} years old")
    
def ask_name ():
    name = input("What is your name ?")
    return name
    
name = "dariste"
age = "28"
show_informations_person(name, age)

name2 = ask_name()
age2=35
show_informations_person(name2, age2)
"""
# POO
#   classe: personne
#       variable : name, age
#        Actions : (methods)
#           -presentation
#           -ask name (input)
            
#--------------- DEFINITION OF CLASS PERSON------------
import re


class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
        print("Name: " +name)
        print("Age: " +str(age))
    
    def presentation(self,):
        print(f"Good morning, my name is {self.name}, I am {self.age} years old. ")
        if self.you_major():
               print ("I am major")
        else:
            print ("I am minor")
    def another_function():
        print("another function")
        
    def you_major(self):
        return self.age > 19
          
        
#-----------------INSTANCIATION-----------------------------
person1 = Person("Dariste", 30)  # create one person
person1.presentation()

print("-------------------------------------------------------")
person2 = Person("paul", 15)  # create another person
person2.presentation()    # Instance method


#Person.another_function() # class method


