myList = [1,3, 5, 6, 6 , 55, 7]

element = 55
flag = 0
for i in range(0, len(myList)):
    if(myList[i] == element):
        flag = 1
        break 
    else:
        flag = 0

if(flag == 1):
    print("element is found")
else:
    print("element is not found")