# Rozwijanie gry "Jaka to liczba?"
# 1. Pytanie o imię

import random

print("Witaj w grze \"Jaka to liczba?\"")
name = input("Jak masz na imię? ")

drawnnumber = random.randint(0, 100)
attempt = 1
userselection = ""
level = ""

print("Cześć",name,"! Wybierz poziom trudności dla siebie:\n"
      "\nEasy - 10 prób - wpisz easy"
      "\nMedium - 7 prób - wpisz medium"
      "\nHard - 5 prób - wpisz hard"
      "\nInsane - 3 próby - wpisz insane"
      "\nGodMode - 1 próba - wpisz godmode\n")

level = input("Twój wybór: ")

if level == "easy":
    level = 10
elif level == "medium":
    level = 7
elif level == "hard":
    level = 5
elif level == "insane":
    level = 3
elif level == "godmode":
    level = 1
else:
    print("Nie ma takiego bicia! Za karę grasz randomowo!")

while drawnnumber != userselection:
    userselection = int(input("\nLiczba: "))
    if userselection > drawnnumber:
        print(name,",","niestety liczba", userselection,"jest za duża. Podaj mniejszą liczbę.")
    elif userselection < drawnnumber:
        print(name,",","niestety liczba", userselection,"jest za mała. Podaj większą liczbę.")
    elif userselection == drawnnumber:
        print("Tak jest! To właśnie", drawnnumber,"! Potrzebowałeś",attempt,"prób by ją odgadnąć. Brawo",name,"!")
    else:
        print("Hmmm... Coś poszło nie tak...")
    if attempt >= level:
        break
    attempt += 1

print("\t\t\t\t\tGAME OVER")

input("\nEnter kończy grę")