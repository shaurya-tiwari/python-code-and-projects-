import random


# now we map the r to the emojis accordingly in dictionary , in key value pair
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
# we se tuple becouse its only for ead not for wriite or modify
choices = ('r', 'p', 's')

while True:
    user_choice = input('rock,paper,scissor ? | r/p/s : ').lower()
    if user_choice not in choices:
        print("invalid choiice ! ")
        continue # it will n through erorr it will give a chance to go on 
    computer_choice = random.choice(choices)

    print(f'you choose {emojis[user_choice]}')
    print(f'computer choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("DRWAAAAA !")
        # \ - back slash represeent tht there is line break
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print('you win ..!')
    else:
        print("you  loosee 😂😂😁")

    again = input('continue playing ? (Y/N)').lower()
    if again == 'n':
        break
