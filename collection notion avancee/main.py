# the collections : LIST / TUPLE 
# Append / Extend / += / Insert
"""name =['John', 'Doe', 'Smith']

additional_name = ["dariste", "jean"]

#name.append(additional_name)
#print(name)

for i in additional_name:
    name.append(i)
    
print(name)

print()
# used of Extend
name.extend(additional_name)
print(name) 
name += additional_name
print(name)
name.insert(3, "toto")
print(name)

#-------------------Slices----------------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'jean']
print (name[1:3])

slice_nom = name
slice_nom[0] = "toto"
print(slice_nom)
print(name)

#------------------Sort/sorted--------------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'jean']

name.sort(reverse=True) # sort the list

sort_name = sorted(name, reverse=True) # sorted return a new list
print(name)
print(sort_name)

# sort the length of the name
sort_name = sorted(name, key=len, reverse=True)
print(sort_name)

#------------Operation on list elements:min, max, in, sum------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'jean']
ages = [20, 30, 10, 50, 22]

print (min(ages))
print (max(ages))
print (sum(ages[:3]))

if "john" in name:
    print("present")
else:
    print("absent")
    
#-----------------Exchangeg elements--------------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'Linda']
t = name[0] # t is a copy of the first element
name[0] = name[4] 
name[4] = t
print(name)

name[0], name[4] = name[4], name[0]
print(name)

#-----------------Join and Split--------------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'Linda']
# Join means to concatenate the list
name_join="-".join(name)
print(name_join)

# Split means to split the string
name_split = name_join.split("-")
print(name_split)

#----------------index,find and count--------------------
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'Linda','John']

element_search = "John"
nb_occurance = name.count(element_search) # count the number of occurance of the element
print ("number of accurance",nb_occurance)
if nb_occurance > 0:
    print(name.index(element_search))
else:
    print("not found")
"""
#        0       1       2       3           4
name =['John', 'Doe', 'Smith', 'dariste', 'Linda','John']

length_name = [len(non) for non in name if len(non) > 5  ]
name_with_j=[non for non in name if "i" in non]
#print(length_name)
#print(name_with_j)

a = [True, True, False, True, True]
print(any(a))
print(all(a))






