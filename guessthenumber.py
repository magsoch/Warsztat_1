from random import randint

checked_value = False
chosen_number = randint(0, 100)

while not checked_value:
    guessnumber = input("Guess the number: ")
    try:
        guessnumber = int(guessnumber)
    except ValueError:
        print("This is not a number")
    if guessnumber > chosen_number:
        print("Too many! ")
    elif guessnumber < chosen_number:
        print("Not enough! ")
    else:
        print("You guessed")
        break

print("The number {} is correct. ".format(chosen_number))
