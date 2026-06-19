import random
while True:
    secret=random.randint(1,10)
    guess=int(input("Guess an number :"))
    if(guess>secret):
        print("Try Again :")
    elif(guess<secret):
        print("Try Again :")
    else:
        print("Correct :")
        break        