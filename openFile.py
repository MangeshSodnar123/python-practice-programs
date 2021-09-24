# with open('pie.txt') as pie:
#     content = pie.read()
#     print(content)


# pieFile = 'pie.txt'
# with open(pieFile) as pie:
#     for line in pie:#going through each line of file
#         # print(line) #this syntax adds new line after each line 
#         print(line.strip()) #this syntax removes the blank lines 


# with open('pie.txt') as pie:
#     lines = pie.readlines() # if you use readline() , it will only read one line at a time.
# #to access the file content outside with block
# pistring = ''
# for line in lines:
#     # pistring += line.rstrip() #this removes white spaces from right side.
#     pistring += line.strip() #this removes white spaces from all sides.
# print(pistring)
# print(len(pistring))


#currently this code is not working
# massage = "i like dogs."
# massage.replace('dogs','cats')
# print(massage)


# # writing to a file 
# with open('test_file.txt','w') as test_file:
#     test_file.write('I love programming.')




# #guest
# name_entry = input("Enter Your name: ")
# with open('guest.txt','a') as guests:
#     guests.write(name_entry + '\n')



# #guestbook
# while True:
#     print("Type 'q' to exit.")
#     guest_name = input('Please enter your name: ')
#     if 'q' in guest_name:
#         break
#     print(f"Welcome {guest_name}, It's our pleasure to have you.")
#     with open('guest_book.txt','a') as guest_book:
#         guest_book.write(guest_name + "\n")



# #programming poll


# while True:
#     print("Enter 'q' to exit.")
#     name = input("Enter your name to poll: ")
#     if 'q' in name:
#         break
#     poll = input("Why do you like programming: ")
#     if 'q' in poll:
#         break

#     with open('polls.txt','a') as polls:
#         polls.write(name.title() + " : " + poll.capitalize() + ".\n")
#         # polls.write(' : ')
#         # polls.write(poll)




# #exception handling.
# while True:
#     num1 = input("Enter num1: ")
#     if 'q' in num1:
#         break
#     num2 = input("Enter num2: ")
#     if 'q' in num2:
#         break

#     try:
#         answer = int(num1) / int(num2)
#     except ZeroDivisionError:
#         print("You can't divide by zero.")
#     else:          #get executed if try block executes.
#         print(answer)




# #handling file not found error
# file = 'test_file.txt'
# try:
#     with open(file, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print("the file you are looking for is not found.")
# else:
#     words = contents.split() #this keyword splits the sentence into words.
#     print(words)
#     print(len(words))



# #cats and dogs
# cats = 'cats.txt'
# dogs = 'dogs.txt'
# animals = [cats, dogs, 'cows.txt']

# try:
#     for file in animals:
#         with open(file) as f:
#             content = f.read()
#             words = content.split()
#         print(words)
#         print(f'length of the file is {len(words)}')
# except FileNotFoundError:
#     # print('file not found')
#     pass



#test file 
with open('test_file.txt') as test_file:
    contents = test_file.read()
words = contents.split()
# word_count = words.count('the') #can't use lower() on list, only can use on strings.
word_count = contents.lower().count('the')
print(word_count)
