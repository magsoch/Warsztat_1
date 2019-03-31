import random

liczby_uzytkownika = []

while len(liczby_uzytkownika) < 6:
    try:
        liczba = int(input("Podaj liczbę: "))
    except ValueError:
        print("Takich rzeczy nie da się wylosować w Lotto!")
        continue

    if liczba in liczby_uzytkownika:
        print("Hej wylosowałeś już tą liczbę. Wybierz coś nowego!")
        continue

    if liczba > 49 or liczba < 1:
        print("Takiego Lotto jeszcze nie było!")
        continue

    liczby_uzytkownika.append(liczba)
    liczby_uzytkownika.sort()

liczby_uzytkownika = set(sorted(liczby_uzytkownika))
print(liczby_uzytkownika)
numerki_maszyny_losujacej = list(range(1, 50))
random.shuffle(numerki_maszyny_losujacej)
twoje_szczesliwe_numerki = set(numerki_maszyny_losujacej[:6])
print(twoje_szczesliwe_numerki)
c = twoje_szczesliwe_numerki & liczby_uzytkownika
if len(c) > 3:
    print("Brawo wylosowałeś co najmniej 3 liczby: {}".format(c))
else:
    print("Nie poszło ci dobrze: {}".format(c))
