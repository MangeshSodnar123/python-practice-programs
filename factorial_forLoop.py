num = int(input("Enter the number : "))
factorial = 1
if num == 1 or num == 0:
    print("The factorial is 1. ")
else:
    for i in range( 1, num+1):
        factorial = factorial * i

print("The factorial of the ",num,"is ",factorial)