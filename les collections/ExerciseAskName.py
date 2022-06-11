def ask_name():
    name = []
    condition = True
    while condition:
        names = input("What is your name ? ")
        if names == "":
            break
        else:
            name.append(names)
    print(name)
    name.sort()
    print()
    print(name)

ask_name()

