def addition(title,**nomber):
    print("Title:",title)
    resultat = 0
    for i in nomber.values():
        resultat += i
    return resultat

a=addition("Addition",English=10,French=20,Math=30)
print("the result is",a)