import random
import os 

f = open('words.txt', 'r')
words = f.readlines()
f.close()
for word in words:
    word.rstrip()


def completed(correct,choice):
    if correct == choice[:-1]:
        print("YOU WON")
        return True
    return False              


def going(correct,lives,choice):
    if lives<0 or completed(correct,choice):
        return False
    return True    
    

def isthere(char,choice):
    for ch in choice:
        if ch == char:
            return True
    return False


def update_correct(char,choice,correct):
    for i in range(0,len(choice)-1):
        if choice[i] == char:
            correct = correct + char
    return correct        

def print_status(choice,correct):
    temp = ""
    for i in choice[:-1]:
        if i in correct:
            print(i,end= " ")
            temp = temp + i
        else :
            print("-",end= " ")       
    return temp

def main(words):
    choice = random.choice(words)
    correct = ""
    lives = len(choice)
    used = ""
    while going(correct,lives,choice):
        char = input("ENTER CHARACTER:")
        used = used + char +" "
        if isthere(char,choice):
            correct = update_correct(char,choice,correct) 
        else :
            lives = lives-1   
        os.system("clear")    
        print("\nStatus :")
        correct = print_status(choice,correct)
        print("\nLives :",lives)
        print("used :" + used)
    os.system("clear")
    print("\nCorrect word:",choice)    

main(words)