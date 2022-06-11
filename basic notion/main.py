def print_information(name="", age=0):
    if name == "":
        print("Name: Unknown")
        return
    if age ==0:
        print("My name is "+name)
        print("your have",len(name),"characters in your name")
    else:
        print("My name is " + name + " and I am " + str(age) + " years old.")
        print("your have",len(name),"characters in your name")

print_information()