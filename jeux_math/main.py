import random
from xmlrpc.client import boolean

NOMBRE_MAX = 10
NOMNBRE_MIN = 1
NOMBRE_QUESTION = 4
NOMBER_OF_POINTS=0

def ask_question():
    a=random.randint(NOMNBRE_MIN, NOMBRE_MAX)
    b=random.randint(NOMNBRE_MIN, NOMBRE_MAX)
    answer_int = 0
    while answer_int ==0: 
        answer = input(f"calculed {a} + {b} = ")
        try:
            answer_int = int(answer)
        except ValueError:
            print("please enter a number")
        else:
            if answer_int == a+b:
                print("your answer is Correct")
                return True 
            else:
                print("your answer is Wrong")
                return False
                
                
for i in range(NOMBRE_QUESTION):
    print(f"question number {i+1} of {NOMBRE_QUESTION}")
    point=ask_question()
    if point == True:
        NOMBER_OF_POINTS = NOMBER_OF_POINTS + 1
        
print(f"your score is {NOMBER_OF_POINTS} / {NOMBRE_QUESTION}. Thank you for playing")

if NOMBER_OF_POINTS == NOMBRE_QUESTION:
    print("you are a genius")
elif NOMBER_OF_POINTS == 0:
    print("you are a loser")
elif NOMBER_OF_POINTS > int(NOMBRE_QUESTION/2):
    print("you are a good person")
else:
    print("Learn more")
    
 