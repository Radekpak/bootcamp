wymiary = input("Podaj wymiary sześcianu: ")

wynik1 = f"""Objętość sześcianu: {int(wymiary) ** 3}
Czy jest większa od 1 litra? {int(wymiary) > 1000}"""

print(wynik1)