import datetime
current_year = datetime.datetime.now().year

lata = int(input("podaj rok urodzenia:"))
if current_year - lata >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")
