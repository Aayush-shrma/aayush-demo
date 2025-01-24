# PRACTICAL NO 3
import random
import string

def generatepass(length):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation

    all_cha=lower+upper+digits+symbols

    password = ''.join(random.choice(all_cha) for _ in range(length))
    return password


length=int(input("Enter the length of the random number you wnat ?:"))
password=generatepass(length)
print(f"Your random passowrd of length:{length} is: {password}")