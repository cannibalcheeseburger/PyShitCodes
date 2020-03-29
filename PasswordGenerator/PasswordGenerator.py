from random import randint
Pass_len = int(input("Enter Length of Password"))
Pass = ""
for i in range(0,Pass_len):
    Pass = Pass + chr(randint(0,128))
print(Pass)    