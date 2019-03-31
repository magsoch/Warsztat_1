print("Pomyśl liczbę od 0 do 1000 a ja ją zgadne w max 10 próbach")
min = 0
max = 1000
liczba_uzytkownika = True
guess = int((max - min) / 2) + min
print("Zgaduję " + str(guess))
reakcja = int(input('Wpisz: 1) Za dużo 2) Za mało 3) Wygrałeś'))
while not liczba_uzytkownika:
    if int(reakcja == 3):
        print("Wygrałem")
    if int(reakcja) == 1:
        guess = max
        print("Zgaduję " + str(guess))
    elif int(reakcja == 1):
        guess = min
        print("Zgaduję " + str(guess))
