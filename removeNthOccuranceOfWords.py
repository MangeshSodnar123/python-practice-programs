myList = ["geeks", "for", "geeks"]
word = "geeks"
occ = 2
count = 0
for i in range(0, len(myList)):
    if(myList[i]==word):
        count = count + 1
        if(count == occ):
            del myList[i]

print(f"my updated list is {myList}")