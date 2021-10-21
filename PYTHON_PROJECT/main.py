
def demande_age(nom_personne):
    age = 0
    while age == 0:
        age_str = input(nom_personne+" quel est votre age ? ")
        try:
            age = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez entrez un nombre pour l'age")
    return age

def affiche_information_personne(nom, age, taille=0):
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print(f"vous vous appelez {nom}, vous avez {age} ans")
    print("l'an prochain vous aurez " + str(age + 1) + " ans")
    if age==1 or age ==2:
        print("vous etes bébé")
    elif 12 <= age < 18:
        print("vous etes adolescent")
    elif age < 10:
        print("vous etes enfant")
    elif age == 17:
        print("vous etes presque majeur")
    elif age == 18:
        print("tout juste majeur: Félicitation")
    elif age > 60:
        print("vous etes majeur")
    elif age > 18:
        print("vous etes sénior")
    else:
        print("vous etes mineur")
    if not taille == 0:
        print("taille "+str(taille)+"m")


def demander_nom():
    reponse_nom = ""
    while reponse_nom =="":
        reponse_nom = input("entrez votre nom ")
    return reponse_nom

""""
#demander nom
nom1 = demander_nom()
nom2 = demander_nom()
print("")
#Demander age
age1=demande_age(nom1)
age2=demande_age(nom2)
print("")
#affiche information personne
affiche_information_personne(nom1,age1)
print("")
affiche_information_personne(nom2,age2)
"""
NB_PERSONNE = 1
# boucle for
for i in range(0,NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demande_age(nom)
    affiche_information_personne(nom,age,1.56)

