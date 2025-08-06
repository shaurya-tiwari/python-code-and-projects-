import random


number = random.randint(1, 50)
while True:
    try:
        guess = int(input("guess number between the 1 to 50 "))

        if guess < number:
            print("too low !")
        elif guess > number:
            print("too high")
        else:
            print("welldone ")
            break
    except ValueError:
        print("entere a  valid NUMBER .")
