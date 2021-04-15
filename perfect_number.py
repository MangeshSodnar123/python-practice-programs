'''A number is a perfect number if is equal
 to sum of its proper divisors, that is, 
sum of its positive divisors excluding the 
number itself. Write a function to check if 
a given number is perfect or not.'''

def perfectNum(givenNum):
    addition = 0
    for i in range(1, givenNum-1):
        if givenNum%i == 0:
            addition += i
        else:
            pass
    if addition == givenNum:
        return print(f"{givenNum} is the perfect number")
    else:
        return print(f"{givenNum} is not a perfect number")

perfectNum(6)