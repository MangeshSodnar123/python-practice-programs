num1 = int(input("enter the number \n"))
table = [i*num1 for i in range(1,11)]
print(table)
with open(f"{num1}table.txt","w") as f:
    f.write(str(table))
    f.close()