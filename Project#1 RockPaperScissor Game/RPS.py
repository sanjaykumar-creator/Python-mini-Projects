import random

print('''
1. Rock(R)
2. Paper(P)
3. Scissor(S)''')
opt=['R','P','S']
running = True
def inputdata(opt):
    p1ch=input(" Enter Your Choice:======>")
    return p1ch
def compchoice(opt):
    ch=random.choice(opt)
    if ch == "R":
        print("Your choise is  Rock")
    elif ch == "P":
        print("Your choise is  Paper")
    elif ch == "S":
        print("Your choise is  Scissor")
    return ch
def Result(p1,p2):
    if p1 == p2:
        print("*********MATCH DRAW****************")
    elif (p1 =="R" and p2 =="S") or (p1 =="S" and p2 =="P") or (p1 =="P" and p2 =="R"):
        print("*********YOU WON*******************")
    elif (p1 =="S" and p2 =="R") or (p1 =="P" and p2 =="S") or (p1 =="R" and p2 =="P"):
        print("*********COMPUTER  WINS*******************")
while running == True:
    p1=inputdata(opt)
    if p1 in opt:
        if p1=="R":
            print ("Your choise is  Rock")
        elif p1== "P":
            print("Your choise is  Paper")
        elif p1=="S":
            print("Your choise is  Scissor")
        running= False
    else:
        print("******Incorrect Entry********")
        print("******Select Any One Choice (R/P/S)********")

p2=compchoice(opt)
r=Result(p1,p2)