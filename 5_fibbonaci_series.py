def fibbonaci(num):
    n1 = 0
    n2 = 1
    if num < 0:
        print("Invalid Input")
    elif num == 1:
        print(0)
    elif num == 2:
        print(1)
    else:
        print(0)
        print(1)
        for i in range(2, num):    
            sum = n1 + n2
            print(sum)
            n1 = n2
            n2 = sum

num = int(input("Enter the number : "))
fibbonaci(num)
