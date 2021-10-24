
def print_pizza(collection):
    size_of_pizza = len(collection)
    if size_of_pizza == 0 :
        print("NO PIZZA")
    else:
        print(f"-------LIST OF PIZZA ({size_of_pizza })-------")
        for i in collection:
            print(i)
        print()
        print(f"First pizza: {collection[0]}")
        print(f"Last pizza: {collection[-1]}")


def add_pizza_user(collection):
    p = input("pizza to add: ")
    collection.append(p)


pizzas = ["4 fromages", "vegetarian", "hawai", "colzone", "pizzaroma"]
add_pizza_user(pizzas)
print_pizza(pizzas)
