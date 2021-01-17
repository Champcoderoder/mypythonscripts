# Wydzielona funkcja z pętlą while programu PRZElicznik
from przelicznikifcoredef import ifcore

def core2(mode):
    while mode == 1 or 2 or 3 or 4 or 5:
        mode = int(input("\nCo chciałbyś przeliczyć?\n 1 - Jaki procent liczby stanowi wybrana przez Ciebie liczba \n 2 - Prędkość 1 km znając prędkość w km/h \n 3 - Kilogramy na funty \n 4 - Funty na kilogramy \n 5 - Koszt obiadów w TW w danym miesiącu \n 0 - Wyłącz program \n Twój wybór: "))
        if mode == 0:
            print("\nZamknięcie programu")
            print()
            break
        ifcore(mode)
