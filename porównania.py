number1 = input("Podaj liczbę: ")

wynik1 = int(number1) > 10

wynik2 = int(number1) <= 15

wynik3 = int(number1) % 2 == 0

result = F"""
Podana liczba: {number1}

Czy liczba jest większa od 10? {wynik1}
Czy liczba jest mniejsza bądź równa 15? {wynik2}
Czy liczba jest podzielna przez 2? {wynik3}

"""
print(result)