

nom = ""
while nom == "":
    nom = input("Entrez votre nom ")
    try:
        nom_correct = nom
    except ValueError:
        print("ERREUR ENTRER LE NOM CORRECTEMENT")
print("vous vous appelez "+nom_correct)
