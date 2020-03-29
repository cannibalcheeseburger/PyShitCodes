dic = {"a":"4","b":"|3","c":"(","d":"|)","e":"3","f":"|=",
        "g":"9","h":"|-|","i":"!","j":"_|","k":"|<","l":"|_",
        "m":"/\\/\\","n":"|\\|","o":"0","p":"|D","q":"q",
        "r":"|2","s":"5","t":"7","u":"(_)","v":"\\/","w":"\\/\\/","x":"><",
        "y":"`/","z":"2"}

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