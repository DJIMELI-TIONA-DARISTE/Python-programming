def demande_age():
    age = 0
    while age == 0:
        age_str = input("quel est votre age ? ")
        try:
            age = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez entrez un nombre pour l'age")
    return age
def demander_nom():
    reponse_nom = ""
    while reponse_nom =="":
        reponse_nom = input("entrez votre nom ")
    return reponse_nom
#demander nom
nom = demander_nom()
#Afficher resultat
age = demande_age()
print("vous vous appelez "+ nom + ", vous avez " + str(age) + " ans")
print("l'an prochain vous aurez " + str(age+1) + " ans")
