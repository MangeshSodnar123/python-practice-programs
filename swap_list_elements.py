# first approach
list1 = [1,2,3,4,5,6,7,8,9]
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)

# second approach
# n = len(list1) - 1
# list1[0], list1[n] = list1[n], list1[0]
# print(list1)

# by using function
# def swapElement(givenList):
#     givenList[0], givenList[-1] = givenList[-1], givenList[0]

#     return print(givenList)

# swapElement(list1)

# fourth approach 
# def changeElements(givenList):
#     start, *middle, finish = givenList # except the first and last valures all other values would get stored in middle(* is necessory before the middle)
#     givenList = [finish, middle, start]
#     return print(givenList)

# changeElements(list1)

# fifth approach
def exchange(givenList):
    start = givenList.pop(0)
    end = givenList.pop(-1)
    givenList.insert(0,end)
    givenList.append(start)
    return print(givenList)

exchange(list1)