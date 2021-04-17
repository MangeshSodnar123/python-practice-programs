a = int(input("enter the value of a \n"))
b = int(input("enter the value of b \n"))

try:
    print(round(a/b, 2))
except:
    print("you tried to divide by zero")