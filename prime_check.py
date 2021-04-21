num1 = int(input("enter the number: "))

if num1 > 1:
    for i in range(2, num1):
        if num1 % i == 0:
            print(f"{num1} is not a prime number")
            break
    else:
        print(f"{num1} is the prime number")