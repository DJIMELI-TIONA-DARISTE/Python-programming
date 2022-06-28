#-------------FIRST PART-----------------#
person = {'name': 'John', 'age': '30', 'city': 'New York'}
#print(person['name'])

person['name'] = 'Pierre'
print(person)
person ['job'] = 'programmer'
#print(person)
buy = ('apple', 'banana', 'orange')
person['buy'] = buy

for i in person:
    print(f"keys:{i}        value: {person[i]}")

#-------------SECOND PART-----------------#

person = [
    ("Melanie", 25, 1.75),
    ("John", 30, 1.85),
    ("Pierre", 35, 1.75),
    ("Mary", 40, 1.65),
          ]
dict_person = {
    "Melanie":( 25, 1.75),
    "John": (30, 1.85),
    "Pierre": (35, 1.75),
    "Mary": (40, 1.65)
}

def get_information(name, list):
    for i in list:
        if i[0] == name:
            return i
    return None

infos = get_information("Melanie", person)
print (infos)

infos = dict_person["Melanie"]
print (infos)
