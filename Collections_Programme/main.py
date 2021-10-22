#collection: Array , lists, tuples
# Tuple () : immutable -> you are not able to modified somethings
# Lists [] : mutable -> add and remove the elements

#****************** TUPLES ******************************************
personT = ("Mélanie", "Jean", "Martin", "Alice")
"""for i in range (0, len(person)):
    print(person[i])
for i in personT:
    print(i)
    print(len(i))
    print(i[0])
    print(i[-1])
#****************** LISTS ********************************************

personL = ["Mélanie", "Jean", "Martin", "Alice"]
new_personL = "David"
print(personL)
personL.append(new_personL)
print(personL)
del personL[0]
print(personL)"""

# ********************************* FONCTION ANT TUPLES ************************
def obtain_information():
    return "Melanie", 32 , 1.60

infos = obtain_information()
#print("Name: "+infos[0])
#print("Age: "+str(infos[1]))
#print("Waist: "+str(infos[2]))

Name, Age, Waist = obtain_information()
print(f"Information: Name: {Name}, Age: {Age}, Waist: {Waist}")

#********************* SLICES **********************************

personS = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")
#[start:stop:step]
for i in personS[::-2]:
    print(i)
Name = "Dariste"
print(Name[::-1])
