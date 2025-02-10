import random 

n = (random.randint(1, 100))

win = False

tries = 0

while not win:
    number = int(input("indovina il numero: "))
    tries += 1
    if number < n:
        print("il numero è più alto") 
    elif number > n:
        print("il numero è più basso")
    else:
        win = True
        print(f"bravo hai indovinato in {tries} tentativi!")




