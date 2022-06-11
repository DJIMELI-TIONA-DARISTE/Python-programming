"""def my_fonction():
    print("Hello World")
    return 1

a = 5
b= my_fonction
print("a =",a, "b =",b)"""


    
def print_table(n, operateur_str, operation_callback):
    for i in range(1,11):
        print(i,operateur_str,n,"=",operation_callback(i,n))

def multiplication_table_callback(a,b):
    return a*b

def addition_table_callback(a,b):
    return a+b
def power_table_callback(a,b):
    return pow(a,b)
        
print_table(5,"+", lambda a,b: a+b)  #equivalent at print_table(5,"+", addition_table_callback) 
print()
print_table(5,"x", lambda a,b: a*b)  #print_table(5,"x", multiplication_table_callback)
print()
print_table(5,"^", power_table_callback)  #print_table(5,"^", lambda a,b: pow(a,b))
