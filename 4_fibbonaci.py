def fibbonaci(num):
    if num < 0:
        print("Invalid Input")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        fiboNum = fibbonaci(num-1) + fibbonaci(num-2)
        return fiboNum
        

num = int(input("Enter the number :"))
i = 0
fiboNum = 0
print(fibbonaci(num))