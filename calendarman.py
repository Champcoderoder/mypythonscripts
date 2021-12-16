import time
import calendar

print('Co mogę dla Ciebie zrobić?\n')
mode = int(input('1 - Podaj mi aktualny czas\n2 - Pokaż mi kalendarz na wybrany rok\n3 - Sprawdź czy wybrany rok był rokiem przestępnym\n4 - Wyświetl mi wybrany miesiąc w wybranym roku\n>>>'))

if mode == 1:
    print('Aktualny czas: ', time.asctime(time.localtime(time.time())))
elif mode == 2:
    year = int(input('Wybierz rok, dla którego chcesz wyświetlić kalendarz: '))
    print('Kalendarz na rok: ', calendar.calendar(year))
elif mode == 3:
    istyl = int(input('Podaj rok, dla którego chcesz zweryfikować przestępność: '))
    if calendar.isleap(istyl) == True:
        print(f'Rok {istyl}, był lub będzie rokiem przestępnym.')
    elif calendar.isleap(istyl) == False:
        print(f'Rok {istyl}, nie był lub nie będzie rokiem przestępnym.')
    else:
        print('ERROR')
elif mode == 4:
    yearCal = int(input('Podaj wartość liczbową roku, dla którego chcesz wyświetlić kalendarz: '))
    mthCal = int(input('Podaj wartość liczbową miesiąca, dla którego chcesz wyświetlić kalendarz: '))
    print('\n', calendar.month(yearCal, mthCal))
else:
    print('ERROR MODE')