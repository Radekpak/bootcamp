MiastoA = input("Podaj swoje miasto: ")
MiastoB = input("Podaj dokąd chcesz jechać: ")
cena_paliwa = input("Podaj cene paliwa: ")
spalanie = input("Podaj spalanie: ")
dystans = input("Podaj przejechany dystans: ")
cena_paliwa = int(cena_paliwa)
spalanie = int(spalanie)
dystans = int(dystans)
koszt = spalanie*cena_paliwa*dystans/100

result = f"""
Miasto A: {MiastoA}
Miasto B: {MiastoB}
Przejechany dystans: {dystans}
Cena paliwa: {cena_paliwa}
Spalanie: {spalanie}
koszt: {koszt} """
print(result)
