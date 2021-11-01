myList = ['first item', 'second item', 'third item', 'fourth item']
myListLen = len(myList)

def myListElements():
    print('\nElementy składowe listy:\n')
    for element in myList:
        print(element)
        print()

def changeElements():
    if whichElement == 1:
        myList[0] = input('Nowy element:\n >>> ')
        myListElements()
    elif whichElement == 2:
        myList[1] = input('Nowy element:\n >>> ')
        myListElements()
    elif whichElement == 3:
        myList[2] = input('Nowy element:\n >>> ')
        myListElements()
    elif whichElement == 4:
        myList[3] = input('Nowy element:\n >>> ')
        myListElements()
    elif whichElement == 0:
        print('Nie zmieniono żadnych elementów listy')
    else:
        print('To nie działa!')

def addElements():
    if addElement == 'tak':
        newElement = input('\nNazwa nowego elementu: ')
        myList.append(newElement)
        myListElements()
        andAgain = input('\nCzy chcesz dodać kolejny element?\n >>> ')
        if andAgain == 'tak':
            addElements()
        elif addElement == 'nie':
            print('\nNie dodano kolejnych elementów do listy')
    elif addElement == 'nie':
        print('\nNie dodano żadnych nowych elementów do listy')
    else:
        print('\nCoś poszło niezgodnie z planem')

def cleanUpCrew():
    for i in myList:
        del myList[0:4]
        myListLen = len(myList)
    print(f"Aktualna ilość elementów edytowanej listy: {myListLen}")
    
print()
print('\t\t\t\tTWOJA LISTA\n')

print(f'Ilość elementów na liście: {myListLen}\n')
myListElements()

clean = input('Czy chesz wyczyścić listę?\n >>> ')
if clean == 'tak':
    cleanUpCrew()
    print('Wszystkie elementy z listy zostały usunięte\n')
elif clean == 'nie':
    print('Elementy na liście zostały zachowane\n')
    print('Czy chcesz zamienić któryś z elementów?')
    change = input(' >>> ')
else:
    'Error kurka'

if clean == 'nie' and change == 'tak':
        whichElement = int(input('Który element chcesz zamienić?\n >>> '))
        changeElements()
        anotherOne = input('Czy chcesz zmienić kolejny element?\n >>> ')
        if anotherOne == 'tak':
            changeElements()
        elif anotherOne == 'nie':
            print('Nie zmieniono kolejnych elementów listy\n')
        else:
            print('Coś poszło nie tak\n')       
else:
    print('Nie zmieniono elementów listy\n')

print('Czy chcesz dodać element do listy?')
addElement = input(' >>> ')
addElements()

myListElements()

print()
input('Enter zamyka program\n')