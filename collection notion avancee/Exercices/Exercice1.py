#Insensible à la casse 
def element_in_list(e, l):
    for i in range (len(l)):
        l[i]= l[i].lower()    
   
    return e.lower() in l 
name = ["jean", "Paul","dAriste","papa"]

if element_in_list("JEan",name):
    print("jean is there")
else:
    print("He is not there")
    