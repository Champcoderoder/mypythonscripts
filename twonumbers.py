# Lucky Numbers
import random

print(" ---> Lucky Numbers <---")

randomone = random.randint(1, 45)
randomtwo = random.randint(1, 45)
# print(f"Computer numbers: {randomone}, {randomtwo}")

print("Test your luck!")
numberone = int(input("Your first number: "))
numbertwo = int(input("Your second number: "))

if numberone == randomone and numbertwo == randomtwo:
    print("Congratulations! We have a winner!")
elif numberone == randomtwo and numbertwo == randomone:
    print("Congratulations! We have a winner!")
elif numberone == randomone and numbertwo != randomtwo:
    print("Ough! So close!")
elif numberone != randomone and numbertwo == randomtwo:
    print("Ough! So close!")
elif numberone == randomtwo and numbertwo != randomone:
    print("Ough! So close!")
elif numberone != randomtwo and numbertwo == randomone:
    print("Ough! So close!")
else:
    print("So... Not today.")

print(f"Computer numbers: {randomone}, {randomtwo}")
print(f"Your numbers: {numberone}, {numbertwo}")
