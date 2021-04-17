import math
num1 = int(input("enter first number \n"))
num2 = int(input("enter second number \n"))

operation = input("choose +, -, *, / \n")
try:
    if "+" in operation:
        print(num1+num2)
    elif "-" in operation:
        print(num1-num2)
    elif "*" in operation:
        print(num1*num2)
    elif "/" in operation:
        print(num1/num2)

except Exception as error:
    print(error)