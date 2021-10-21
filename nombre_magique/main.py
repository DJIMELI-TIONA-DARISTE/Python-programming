import random

def demander_nombre(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0:
        nb_str = input(f"quel est le nombre magique (entre {nb_min} et{nb_max}) ? ")
        try:
            nb_int = int(nb_str)
        except:
            print("Erreur, entrez un nombre ")
        else:
            if nb_int < nb_min or nb_int > nb_max :
                print(f"ERREUR: Le nombre doit etre ente {nb_min} et {nb_max}. Réessayez")
                nb_int = 0
    return nb_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIE = 4

nombre = 0
vie = NB_VIE
while not nombre == NOMBRE_MAGIQUE and vie > 0:
    print(f"il vous reste {vie} vies")
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nombre > NOMBRE_MAGIQUE :
        print("le nombre magique est plus petit ")
        vie -=1
    elif nombre < NOMBRE_MAGIQUE:
        print("le nombre magique est plus grand ")
        vie -=1
    else:
       print("Bravo, vous avez gagné")
if vie ==0:
    print("vous avez perdu")
    print(f"le nombre magique est : {NOMBRE_MAGIQUE}")