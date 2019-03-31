print("Pomyśl liczbę od 0 do 1000 a ja ją zgadne w max 10 próbach")
min = 0
max = 1000

while True:
    guess = int((max - min) / 2) + min
    print(guess)
    num = int(input('Choose: 1) Less 2) More 3) Guessed'))
    if num == 1:
        max = guess
    elif num == 2:
        min = guess
        print("I'm guessing " + str(guess))
    else:
        print("The computer guessed", guess, "and it was correct!")
        break
