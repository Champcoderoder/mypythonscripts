# Przeliczanie
from przelicznikcore1def import core1
from przelicznikcore2def import core2

print(" --- PRZElicznik --- ")
print("Więcej niż zwykły licznik")
print()

mode = int(input("Co chciałbyś przeliczyć?\n\n 1 - Jaki procent liczby stanowi wybrana przez Ciebie liczba \n 2 - Prędkość 1 km znając prędkość w km/h \n 3 - Kilogramy na funty \n 4 - Funty na kilogramy \n 5 - Koszt obiadów w TW w danym miesiącu \n Twój wybór: "))

core1(mode)

question = int(input(" 1 - Kolejne obliczenia \n 0 - Wyłączenie programu\n Twój wybór: "))

print()
if question == 1:
    core2(mode)
elif question == 0:
    print("\nZakończenie programu\n")
else:
    print("Nieznane polecenie")
    print("\nProgram zakończył działanie\n")
