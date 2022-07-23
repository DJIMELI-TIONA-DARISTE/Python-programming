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
    def __init__(self, name ="", age=0):
        self.name = name  # Instance variable
        self.age = age
    
        if name == "":
            self.ask_name()
            
        print("Constructor Name: " +self.name)
        print("Constructor Age: " +str(age))
    
    def presentation(self,):
        if self.name != "" and self.age != 0:
            print(f"Good morning, my name is {self.name}, I am {self.age} years old. ")
            if self.you_major:
                print("you are major")
            else:
                print("you are a child")
        elif self.name != "" and self.age ==0:
            print(f"Good morning, my name is {self.name}" )
    
            
    def another_function():
        print("another function")
        
    def you_major(self):
        return self.age > 19
    
    def ask_name(self):
        self.name=input("what is your name ")
        
          
        
#-----------------INSTANCIATION-----------------------------
person1 = Person("Dariste", 30)  # create one person
person1.presentation()

print("-------------------------------------------------------")
person2 = Person()  # create another person
person2.presentation()    # Instance method

print("-------------------------------------------------------")
person3 = Person()  # create another person
person3.presentation()    # Instance method

#Person.another_function() # class method


