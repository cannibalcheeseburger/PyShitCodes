import random

options = "1234567890@!#$%*qwertyuiopasdfghjklzxcxvbnbnmZXCVBNMASDFGHJKLQWERTYUIOP"
pass_len = int(input("ENTER LENGTH OF PASSWORD"))
password = ""
for i in range(0,pass_len-1):
    password = password + random.choice(options)
print(password)
