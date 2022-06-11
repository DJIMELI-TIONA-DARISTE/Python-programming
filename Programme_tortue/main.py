import turtle
t = turtle.Turtle()

def escalier(taille, nb_m):
    for i in range(0, nb_m):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille = taille - 10
    t.forward(taille)

def carre (taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)
        
         
carre(100)   
#escalier(60,5)

turtle.done()