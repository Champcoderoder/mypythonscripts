# Lucky Numbers
import random

print("\n\t\t ---> Lucky Numbers <---")

randomone = random.randint(1, 45)
randomtwo = random.randint(1, 45)
# Check computer numbers
# print(f"Computer numbers: {randomone}, {randomtwo}")

print("\nTest your luck! Choose to numbers. Maybe you'll be the winner!\n")
numberone = int(input("Your first number: "))
numbertwo = int(input("Your second number: "))

if numberone == randomone and numbertwo == randomtwo:
    print("\nCongratulations! We have a winner!\n")
elif numberone == randomtwo and numbertwo == randomone:
    print("\nCongratulations! We have a winner!\n")
elif numberone == randomone and numbertwo != randomtwo:
    print("\nOugh! So close!\n")
elif numberone != randomone and numbertwo == randomtwo:
    print("\nOugh! So close!\n")
elif numberone == randomtwo and numbertwo != randomone:
    print("\nOugh! So close!\n")
elif numberone != randomtwo and numbertwo == randomone:
    print("\nOugh! So close!\n")
else:
    print("\nSo... Not today.\n")

print(f"Computer numbers: {randomone}, {randomtwo}")
print(f"Your numbers: {numberone}, {numbertwo}\n")
