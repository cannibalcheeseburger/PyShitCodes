from random import randint
import os
def win(cpu,human):
    if (cpu == 0 and human ==2) or (cpu ==1 and human ==0) or (cpu == 2 and human == 1):
        return 0
    elif(cpu == human):
        return 2
    else :
        return 1        
    
options = ["Rock","Paper","Scissors"]
wins = ["cpu wins","human wins","tie"]    
while True:
    os.system('cls')
    cpu = randint(0,2)
    human = 3
    while human>2 or human<0:
        human = int(input("Enter valid choice(1-3):\n1.Rock\n2.Paper\n3.Scisor"))-1
    print(wins[win(cpu,human)])
    print("cpu = ",options[cpu])
    print("human = ",options[human])
    input()

