num = int(input("Enter the number : "))
prime = 0
if num == 0 or num == 1:
    print("The number is neither prime nor composite.")
else:
    for i in range(1, int(num/2)+1):
        if num % i == 0 :
            prime = 0
        else:
            prime = 1
    if prime == 1:
        print("The number is prime number. ")     
    else:
        print("The number is not prime number. ")
        
