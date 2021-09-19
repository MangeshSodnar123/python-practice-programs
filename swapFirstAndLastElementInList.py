list1 = [1, 3, 4, 5 , 6]
length = len(list1)
temp1 = list1[0]
temp2 = list1[length-1]
list1[0] = temp2
list1[length-1] = temp1
print(list1)


