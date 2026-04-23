interfrace = int(input("Calculator: Enter First Number: "))
num2 = int(input("Calculator: Enter second Number: "))

add = str(input("Do You want to Add these 2 Numbers? (Yes or No): ")).lower()
if add == "yes":
    print(interfrace ,"+", num2, "=", interfrace + num2)
else:
    subtract = str(input("Do You want to Subtract these 2 Numbers? (Yes or No): ")).lower()
if subtract == "yes":
        print(interfrace ,"-", num2, "=", interfrace - num2)
else:
    multiply = str(input("Do You want to Multiply these 2 Numbers? (Yes or No): ")).lower()
if multiply == "yes":
        print(interfrace ,"x", num2, "=", interfrace * num2)
else:
     divide = str(input("Do You want to Divide these 2 Numbers? (Yes or No): ")).lower()
if multiply == "yes":
        print(interfrace ,"/", num2, "=", interfrace / num2)
