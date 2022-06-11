def ask_choice_user(min,max):
    respond_str=input(f"Enter a number between {min} and {max}:")
    try:
        reponse_int=int(respond_str)
        if not (min <= reponse_int <= max):
            print("Error:choice de number between {} and {}".format(min,max))
            return ask_choice_user(min,max)
        return reponse_int
    except ValueError:
        print("You must enter a number")
        return ask_choice_user(min,max)

def a():
    print("begin of function a")
    for i in range(1,50):
        if i > 10:
            return
        print(i)
    print("end of function a")
#choix = ask_choice_user(1,4)
#print("choice is:", choix)
a()     