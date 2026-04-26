import math

def add():
    print(num1, "+", num2, "=", num1 + num2)

def sub():
    print(num1, "-", num2, "=", num1 - num2)

def multiply():
    print(num1, "x", num2, "=", num1 * num2)

def divide():
    print(num1, "/", num2, "=", num1 / num2)

def power():
    print(num1, "^", num2, "=", num1 * num1)

def sqroot():
    print("Square Root of", num1, "=", math.sqrt(num1) )

# cube root function is in the code line 61 (i saved time)

interface = int(input("Choose an Option from the Following List:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root\n7. Cube Root\nEnter (1, 2, 3, 4, 5, 6 or 7): "))
if interface == 1:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    add()
elif interface == 2:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    sub()

elif interface == 3:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    multiply()
    
elif interface == 4:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    divide()

elif interface == 5:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter a value of Power: "))

    power()

elif interface == 6:
    num1 = int(input("Enter Number: "))

    sqroot()

elif interface == 7:
    num1 = int(input("Enter Number: "))

    print("Cube Root of", num1, "=", math.cbrt(num1) )

else:
    print("Invaild Option!")
