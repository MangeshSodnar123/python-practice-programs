# # Programm to print the prime numbers upto given range
# num = int(input("Enter the number upto which you want prime numbers printed\n"))
# prime = False
# if(num < 2):
#     pass
# elif(num == 3):
#     print(2, 3)
# else:
#     print(2)
#     print(3)
#     for i in range(1,num+1):
#         for j in range(2,int(i/2 +1)):
#             if(i%j == 0):
#                 prime = False
#                 break
#             else:
#                 prime = True
#         if prime:
#             print(i)


# program to check if given number is prime or not 
# num = int(input("Please enter the number: "))
# prime = False

# if(num <=1):
#     print(f"{num} is neither prime nor non-prime.")

# elif(num == (2 or 3)):
#     print(f"{num} is a prime number.")

# else:
#     prime = False
#     for i in range(2,int(num/2) + 1):
#         if(num % i == 0):
#             prime = False
#             break
#         else:
#             prime = True

#     if prime:
#         print(f"{num} is the prime number.")   
#     else:
#         print(f"{num} is not a prime number")         

from numpy.random import randn
data = {i : randn() for i in range(7)}
print(data)