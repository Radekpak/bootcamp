position_x = int(input("Podaj pozycję gracza X: "))
position_y = int(input("Podaj pozycję gracza Y: "))

if position_x > 11 and position_x < 89 and position_y > 11 and position_y < 89:
    print("Gracz znajduję się w centrum")

elif position_x >= 0 and position_x <= 10 and position_y >= 0 and position_y <= 10:
    print("Gracz znajduję się w lewym dolnym rogu")

elif position_x >= 90 and position_x <= 100 and position_y >= 0 and position_y <= 10:
    print("Gracz znajduje się w prawym dolnym rogu")

elif position_x >= 0 and position_x and position_x <= 10 and position_y >= 90 and position_y <= 100:
    print("Gracz znajduje się w lewym górnym rogu")

elif position_x >= 90 and position_x <= 100 and position_y >= 90 and position_y <= 100:
    print("Gracz znajduje się w prawym górnym rogu")

elif position_x >= 0 and position_x <= 10 and position_y >= 10 and position_y <= 90:
    print("Gracz znajduje się na lewej krawędzi")

elif position_x >= 10 and position_x <= 90 and position_y >= 90 and position_y <= 100:
    print("Gracz znajduje się na górnej krawędzi")

elif position_x >= 90 and position_x <= 100 and position_y >= 10 and position_y <= 90:
    print("Gracz znajduje się na prawej krawędzi")

elif position_x >= 10 and position_x <= 90 and position_y >= 0 and position_y <= 10:
    print("Gracz znajduje się na dolnej krawędzi")

else:
    print("Gracz jest poza mapa")







