def add():
    print(num1, "+", num2, "=", num1 + num2)

def sub():
    print(num1, "-", num2, "=", num1 - num2)

def multiply():
    print(num1, "x", num2, "=", num1 * num2)

def divide():
    print(num1, "/", num2, "=", num1 / num2)

interface = int(input("Choose an Option from the Following List:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter (1, 2, 3 or 4): "))
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

else:
    print("Invaild Option!")
