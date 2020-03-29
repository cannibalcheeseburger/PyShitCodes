dic = {"a":"4","e":"3","g":"6","o":"0","s":"5","t":"7"}

inpoot = input("Enter String to convert to Basic Leet:")
inpoot = inpoot.lower()

def convert_to_leet(inpoot):
    LEET = ""
    for ch in inpoot :
        if ch in dic:
            LEET  = LEET + dic[ch]
        else:
            LEET = LEET + ch    

    print(LEET)

convert_to_leet(inpoot)    