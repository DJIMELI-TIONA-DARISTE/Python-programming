def tri_perso (e):
    return e


def pizzas_exist(list, new_pizza):
    for i in list:
        if i == new_pizza.lower():
            return True
    return False

def print_pizzas(pizzas):
    nbr_pizzas = len(pizzas)
    if nbr_pizzas == 0:
        print("No pizza")
    else:
        number_of_pizza_print =""
        number_of_pizza_print = input("Enter the number of pizzas you want see: ")
        if number_of_pizza_print=="" or number_of_pizza_print=="0":
            pizzas.sort(key=tri_perso)
            print(f"-------LIST OF PIZZAS({nbr_pizzas})-------")
            for i in pizzas:
                print(i)
            print("-------END OF LIST-------")
            print()
            print("the first pizza is: " + pizzas[0])
            print("the last pizza is: " + pizzas[-1])
        else:
            pizzas.sort(key=tri_perso)
            int_number_of_pizza_print = int(number_of_pizza_print)
            print(f"-------LIST OF PIZZAS({int_number_of_pizza_print})-------")
            for i in range(0, int_number_of_pizza_print):
                print(pizzas[i])
            print("-------END OF LIST-------")
            print()
            print("the first pizza is: " + pizzas[0])
            print("the last pizza is: " + pizzas[-1])  
        
def user_add_pizza(pizzas):
    pizz_add = input("Add a pizza: ")
    chek_pizza = pizzas_exist(pizzas, pizz_add)
    if chek_pizza==True:
        print("This pizza already exist")
    else:
        pizzas.append(pizz_add)
    


pizzas = ['margarita', 'pepperoni', 'hawaiian', 'veggie','dariste']   
pizzas2=()

user_add_pizza(pizzas)
print_pizzas(pizzas)
