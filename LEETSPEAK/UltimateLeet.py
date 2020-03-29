dic = {"a":"4","b":"8","c":"(","d":"|)","e":"3","f":"|#",
        "g":"6","h":"|-|","i":"!","j":"_)","k":"|(","l":"1",
        "m":"/\\/\\","n":"|\\|","o":"0","p":"|>","q":"?",
        "r":"|2","s":"5","t":"+","u":"|_|","v":"\\/","w":"\\/\\/","x":"%",
        "y":"`/","z":"7_"}
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