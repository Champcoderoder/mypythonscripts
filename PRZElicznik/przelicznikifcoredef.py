# Funkcja z if

def ifcore(mode):
    if mode == 1:
      print()
      amode1 = float(input("Liczba: "))
      bmode1 = float(input("Procent: "))
      scoremode1 = amode1 / 100 * bmode1
      print(f"Wynik: {scoremode1}")
      print()
    elif mode == 2:
      print()
      amode2 = float(input("Prędkość w km/h: "))
      scoremode2 = 60 / amode2
      print(f"Wynik: {scoremode2}")
      print()
    elif mode == 3:
      print()
      amode3 = float(input("Twoja waga w kilogramach: "))
      scoremode3 = 2.2 * amode3
      scoremode3round = round(scoremode3, 2)
      print(f"Twoja waga w funtach: {scoremode3round}")
      print()
      # Poniżej pozostawiam błędny zapis
      # print(round(f"Twoja waga w funtach: {scoremode3}", 2))
    elif mode == 4:
      print()
      amode4 = float(input("Twoja waga w funtach: "))
      scoremode4 = amode4 / 2.2
      scoremode4round = round(scoremode4, 2)
      print(f"Twoja waga w kilogramach: {scoremode4round}")
      print()
    elif mode == 5:
      print()
      amode5 = float(input("Ilość obiadów: "))
      prize = float(input("Koszt jednego obiadu: "))
      scoremode5 = amode5 * prize
      print(f"Do zapłaty: {scoremode5}")
      print()
    else:
      print("ERROR")
      print("Program napotkał niespodziewany problem")
