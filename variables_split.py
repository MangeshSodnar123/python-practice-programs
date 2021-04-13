# id1, id2, id3 = range(1,4) #values in the given range can be assign to multiple variables using this syntax
# print(id1)

# id1, id2, id3 = input().split(" ") #whatever seperator value is given in "" should use in giving input. if nothing is given then seperate the variable value by space
# print(id1)
# print(id2)
# print(id3)

# # Python program showing how to
# # multiple input using split

# # taking two inputs at a time
# x, y = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print()

# # taking three inputs at a time
# x, y, z = input("Enter a three value: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()

# # taking two inputs at a time
# a, b = input("Enter a two value: ").split()
# print("First number is {} and second number is {}".format(a, b))
# print()

# # taking multiple inputs at a time
# # and type casting using list() function
# x = list(map(int(input("Enter a multiple value: ").split())))
# print("List of students: ", x)


# taking three input at a time by using list
x, y, z = [int(x) for x in input("Enter three value: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)

print(isinstance(x,int))


