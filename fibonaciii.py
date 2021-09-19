n1 = 0
n2 = 1
sum1 = 0

print(n1)
print(n2)

for i in range(0,10):
    sum1 = n1 + n2 
    print(sum1)
    n1 = n2
    n2 = sum1

