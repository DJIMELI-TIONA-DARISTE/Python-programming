from tkinter import scrolledtext


def ask_question(question,resp1,resp2,resp3,resp4,correctAnswer):
    global score   
    print("Question: " + question)
    print("(a) " + resp1)
    print("(b) " + resp2)
    print("(c) " + resp3)
    print("(d) " + resp4)
    answer=input("Answer: ")
    if answer==correctAnswer:
        score +=1
        print("Correct!")
    else:
        print("Wrong!")
    print()
score = 0
ask_question("What is the capital of France?","Paris","London","Berlin","Madrid","a")
ask_question("What is the capital of Germany?","Madrid","Berlin","London","Paris","b")
ask_question("What is the capital of Italy?","London","Madrid","Paris","Rome","d")
ask_question("What is the capital of Spain?","Madrid","London","Berlin","Paris","a")
print ("Your score is: " + str(score))