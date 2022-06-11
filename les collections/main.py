#Collections : (Tableaux : array ), Liste, Tuples...
# Tuples (): immutable, uniquement les valeurs sont lues une fois
#Liste [] : mutable, les valeurs sont lues plusieurs fois et peuvent etre modifiées


#------------------SECTION TUPLES------------------
"""person = ("John", "Doe", "dariste", "jean","paul")
#print(len(person))
#print(person[3])

#for i in range(0, len(person)):
    #print(person[i])
    
for i in person:
    print(i)
    print(len(i))
    print(i[-1])
    
#------------------SECTION LISTES------------------    

person = ["John", "Doe", "dariste", "jean","paul"]
#print(person)
person.append("Luise") 
#print(person)
del person[2]
#print(person)

def print_liste(liste):
    for i in liste:
        print(i)

print_liste(person)"""

#------------------FONCTION AND TUPLES------------------
"""def get_information():
    return "John", 18, 1.80

def get_information2(name, age, taille):
    print(f"informations : Name: {name}, Age: {age}, taille: {taille}")

infos = get_information()

print("nom: " +infos[0])
print("age: " +str(infos[1]))
print("taille: " +str(infos[2]))
name, age, taille = get_information()
#print(f"informations : Name: {name}, Age: {age}, taille: {taille}")
get_information2(*infos)
print()
print(infos)
print()
print(*infos) #unpack tuple equivalent à print(infos[0], infos[1], infos[2])
"""

#-----------------------SLICES-----------------------
person = ("John", "Doe", "dariste", "jean","paul")

for i in person[0:3]:
    print(i)
    