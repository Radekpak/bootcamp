number = input("Podaj pierwszą liczbę: ")
number1 = input("Podaj drugą liczbę: ")
number2 = input("Podaj rodzaj operacji: ")

if number2 == "+":
    print(int(number) + int(number1))
elif number2 == "-":
    print(int(number) - int(number1))
elif number2 == "/":
    print(int(number) / int(number1))
elif number2 == "*":
    print(int(number) * int(number1))


