def fibonacci(num1):
    if num1<0:
        print("invalid input ")
    elif num1 == 1:
        return 0
    elif num1 == 2:
        return 1
    else:
        return fibonacci(num1-1)+fibonacci(num1-2)

print(fibonacci(10))