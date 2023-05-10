import math
from fractions import Fraction as f
from time import sleep as zzz

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def leftdiv(a, b):
    return a % b

def floordiv(a, b):
    return a // b

def fulldiv(a, b):
    fulldiv = str(a % b) + str(a // b)
    return str(fulldiv)

def exp(a, b):
    return a ** b

def squ(a):
    return math.sqrt(a)
    return math.sqrt(b)

def frac(a, b):
    return f(a, b)

def perc(a, b):
    per = 100 * float(a)/float(b)
    return str(per)


def surmod():
    optionsphere = int(input("""
    1. Sphere surface
    2. Sphere perimeter
    3. Circle surface
    4. Circle perimeter
    5. Convert circle to sphere
    6. Convert sphere to circle
    7. Exit sphere mode
    """))

    def circlesur(a):
        return a * math.pi ** 2

    def circleperi(a):
        return a * math.pi

    def sphersur(a):
        return 4 * math.pi * a ** 2

    def spherperi(a):
        return math.pi * a * 2

    def sphertocir(a):
        return a / 2

    def cirtospher(a):
        return a * 2

    while True:
        if optionsphere == 7:
            break
        elif optionsphere == 1:
            print(circlesur(a))
        elif optionsphere == 2:
            print(circleperi(a))
        elif optionsphere == 3:
            print(sphersur(a))
        elif optionsphere == 4:
            print(spherperi(a))
        elif optionsphere == 5:
            print(cirtospher(a))
        elif optionsphere == 6:
            print(sphertocir(a))
        optionsphere = int(input("""
        1. Sphere surface
        2. Sphere perimeter
        3. Circle surface
        4. Circle perimeter
        5. Convert circle to sphere
        6. Convert sphere to circle
        7. Exit sphere mode
        """))

def greet():
    print("Welcome to 'MY CALCULATOR' !")

greet()

zzz(1)
a = int(input("\nEnter the first number : "))
zzz(1)
b = int(input("\nEnter the second number : "))
option = int(input("""
1. Add
2. Substract
3. Multiply
4. Divide
5. Divison with lefts
6. Floor Division
7. Expose
8. Square Root
9. Fraction
10. Percentage
11. Sphere mode
12. Exit
"""))

while(option != 12): 
    if(option == 1):
        print(add(a, b))
    elif(option == 2):
        print(sub(a, b))
    elif(option == 3):
        print(mul(a, b))
    elif(option == 4):
        print(div(a, b))
    elif(option == 5):
        print(leftdiv(a, b))
    elif(option == 6):
        print(floordiv(a, b))
    elif(option == 7):
        print(exp(a, b))
    elif(option == 8):
        print(squ(a, b))
    elif(option == 9):
        print(frac(a, b))
    elif(option == 10):
        print(perc(a, b))
    elif(option == 11):
        surmod()
    elif(option == 12):
        break