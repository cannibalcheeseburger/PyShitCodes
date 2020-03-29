def slice_index(Email):
    for i in range(0,len(Email)-1):
        if Email[i]=="@":
            return i
    else :
        return -1        
Email = input("Enter Email address:")
index = slice_index(Email)
user = Email[:index]
domain = Email[index+1:]
print("User = "+user+"\nDomain = https://www."+domain)  