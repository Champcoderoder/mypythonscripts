import random
import time

bigLet = range(65, 91)
smallLet = range(97, 123)
numbers = range(48, 58)
someSpecOne = range(35, 39)
someSpecTwo = range(58, 65)
password = ''

def passDef(k, marks):
    global password
    for i in range(k):
        password += chr(random.choice(marks))
    print('Password creation in progress: ', password)
    time.sleep(1)

print('\n==== PASS MAKER 2.0 ====\n')

passDef(4, bigLet)
passDef(4, smallLet)
passDef(4, numbers)
passDef(2, someSpecOne)
passDef(2, someSpecTwo)

conv = list(password)
random.shuffle(conv)
newPass = ''.join(conv)

print('\nYour password: ', newPass)

print('\n==== BE SAFE :: HAVE A NICE DAY ====\n')