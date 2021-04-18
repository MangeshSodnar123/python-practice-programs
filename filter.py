list1 = [5, 10, 15, 34, 27, 49, 25]
# list2 = []


def divisibleBy5(givenList):
    if givenList % 5 == 0:
        return True
    else:
        return False


# divisibleBy5(list1)
# print(list2)
print(list(filter(divisibleBy5, list1)))
