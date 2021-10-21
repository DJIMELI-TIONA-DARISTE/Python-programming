import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 8

# 0 -> +
# 1 -> *
# 2 -> /
# 3 -> -

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 0:
        operateur_str = "+"
    elif o == 1:
        operateur_str = "*"
    elif o == 2 :
        operateur_str = "/"
    else:
        operateur_str = "-"
    r_int = ""
    while r_int == "":
        r_str = input(f"Calculer : {a} {operateur_str} {b} = ")
        try:
            r_int = int(r_str)
            calcul = a+b
            if o == 0:
                calcul = a+b
            elif o == 1:
                calcul = a * b
            elif o == 2 :
                calcul = a / b
            else:
                calcul = a - b
        except:
            print("ERREUR: Entrer un nombre")
    if r_int ==calcul:
        print("Réponse correcte")
    else:
        print("Réponse incorrecte")
    return r_int == calcul


nb_point = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}:")
    compar=poser_question()
    print()
    if compar == True:
        nb_point +=1
print(f"votre note: {nb_point}/{NB_QUESTIONS}")
moyenne = int(NB_QUESTIONS/2)
if nb_point == NB_QUESTIONS:
    print("Excellent")
elif nb_point == 0:
    print("Révisez vous maths")
elif nb_point > moyenne :
    print("Pas mal")
else:
    print("peut mieux faire")

