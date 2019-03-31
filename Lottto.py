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

liczby_uzytkownika = sorted(liczby_uzytkownika)
print(liczby_uzytkownika)
numerki_maszyny_losujacej = list(range(1, 50))
random.shuffle(numerki_maszyny_losujacej)
twoje_szczesliwe_numerki = numerki_maszyny_losujacej[:6]
print(twoje_szczesliwe_numerki)

counter = 0
for moj_numer in liczby_uzytkownika:
    if moj_numer in twoje_szczesliwe_numerki:
        counter += 1
if counter >= 3:
    print("Trafiłeś {} liczb!".format(counter))
else:
    print("Słabo losowałeś. Trafione {}".format(counter))
