import random

secret_number = random.randint(0,100)

while True:
    
    try:
        geuss_number = int(input("Geuss your number: "))
    except:
        print("please insert a number")
        continue
    
    if geuss_number == secret_number:
        print("YOU WiN!")
        break
    elif geuss_number > secret_number:
        print("too big")
    else:
        print("too small")
            