givenNum = int(input("enter one number\n"))
flag = 1
if givenNum == 0 or givenNum == 1:
    print("1 and 0 neither prime nor not-prime")
else:
    for i in range(1,(givenNum//2)+1):
        if givenNum % i == 0:
            flag = 0 
        elif givenNum % i !=0:
            flag = 1
            
if flag == 1:
    print(f"{givenNum} is a prime number.")            
else:
    print(f"{givenNum} is not a prime number")