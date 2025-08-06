import random


while True:
    choise = input("roll the dice ? (y/n): ").lower()
    if choise == 'y':
        # generate the random number between 1 to 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choise == 'n':
        print('get lost ! bye...')
        break
    else:
        print("Invalid choice")
  