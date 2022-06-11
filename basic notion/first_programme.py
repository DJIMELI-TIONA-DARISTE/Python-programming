# DEMANDE D'AGE POUR NOTRE PREMIER PROGRAMME

def infos_person (nom_person, age_person, taille=0):
    print()
    if taille != 0:
        print("vous avez "+str(age)+"m")
    print("L'etudiant s'appel: "+nom_person+ " age "+str(age_person)+" ans")
    print(f"L'an prochain vous aurez {str(age_person+1)} ans")
    if age_person > 60:
        print("vous etes segnior")
    elif age_person > 18:
        print("vous etes majeur")
    elif age_person == 18:
        print("vous etes majeur : Felicitation")
    elif age_person == 17:
        print("Tout etes presque majeur")
    elif 12 <= age_person  < 17 :
        print("vous etes adolescent")
    elif age_person == 1 or age_person == 2:
        print("vous etes bebe")
    elif age_person >= 10:
        print("Vous etes mineur")
   
    else:
        print("Vous etes enfant")
    
    
def demade_age (nom_person):
    age_int = 0
    while age_int==0:
        age_str =input(nom_person+" quel est ton age: ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("entre l'age correctement:")
    return age_int


def demande_nom ():
    nom_f =""
    nom_f= input("entrer votre nom: ")
    while nom_f =="":
        nom_f= input("Entrer un nom ")
    return nom_f
    
"""           
nom1 = demande_nom()
nom2 = demande_nom()
age1 = demade_age(nom1) 
age2 = demade_age(nom2)
infos_person(nom1,age1)
infos_person(nom2,age2)
"""
NB_PERSON = 2
for i in range(0, NB_PERSON):
    nom = "personne " + str(i+1)
    age = demade_age(nom) 
    infos_person(nom, age)
 
