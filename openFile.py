# with open('pie.txt') as pie:
#     content = pie.read()
#     print(content)


# pieFile = 'pie.txt'
# with open(pieFile) as pie:
#     for line in pie:#going through each line of file
#         # print(line) #this syntax adds new line after each line 
#         print(line.strip()) #this syntax removes the blank lines 


with open('pie.txt') as pie:
    lines = pie.readlines() # if you use readline() , it will only read one line at a time.
#to access the file content outside with block
pistring = ''
for line in lines:
    # pistring += line.rstrip() #this removes white spaces from right side.
    pistring += line.strip() #this removes white spaces from all sides.
print(pistring)
print(len(pistring))