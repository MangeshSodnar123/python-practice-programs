# name = " Mangesh "
# mid_name = "Dasharath"
# sur_name = "Sodnar"
# full_name = f"{name} {mid_name} {sur_name}"
# # print(full_name.upper())
# # print(full_name.lower())
# # print(full_name.title())
# # print(full_name.count("s"))
# # print(full_name.endswith("Sodnar"))
# # print(full_name.startswith("Mangesh"))
# print(name.rstrip())#it removes spaces from the right side of the string
# print(name.lstrip())#it removes spaces from the left side of the string
# print(name.strip())#it removes spaces from the both side of the string

# name = " Albert Einstein          "
# message = f'{name.strip()} once said, "The person who never failed, has never tried something new."'
# print(message)
# print('Types of mechanical subjects:\n\t1)Engineering mechanics\n\t2)Mathematics')#this combinations of the \n and \t ;makes the new line and adds tab before showing new text.
# 
# 
# number = 10_00_000 #this increses the readability of the number without affectiong the value of the number. 
# print(number)
# a, b, c = 2, 4, 5
# print(a, b, c)
# CONSTANT = 69 #All capital variable name is used to specify constant.
# print(CONSTANT)
# import this #this is short program writing ethics guide for cleaner code.

# friends = ['mangesh','raju','shyam','baburao','']
# friends[4] = 'ravi'
# friends.append('satya') #append() method adds new element at the end of the list.
# for i in range(0, len(friends)):
#     message = f'{friends[i].title()} is my best friend.' #string methods can be used for lists.
#     print(message)

# friends = ['mangesh','raju','shyam','baburao']
# girl_friends = ['nita','sonia','radha','divya']
# my_friends = []
# for i in range(0, len(friends)):
#     my_friends.append(friends[i].title())
#     my_friends.append(girl_friends[i].title())
#     print(f'{my_friends[i]} loves {my_friends[i+1]}')
# friends.insert(2,'revati')
# print(friends)
# del friends[3] #it permennantly deletes the item from the list and you can't use that again in future.
# print(friends)
# babu = friends.pop() #you can store poped item in the variable.
# friends.pop(0) #you can pop any element by passing the index of the item in the list.
# print (friends,'\n',babu)

#sometimes you don't know the position of the item you want to remove,
#at that time you can use the remove('<item name>') method.
# friends.remove('raju')
# print(friends)


# guestList = ['mangesh','rajesh','sejal','lata','sanika','bongo']
# guestList[3] = 'rane'
# del guestList[2]
# guestList.pop(0)
# guestList.remove('sejal')
# guestList.append('ritu')
# guestList.append('raja')
# guestList.append('bongo')
# guestList.insert(0,'ram')

# inviteMessages = ['welcome home','come in','good morning']
# for i in range(0,len(guestList)):
#     print(f'{inviteMessages[i]} {guestList[i]}')
# for i in range(0,len(guestList)-2):
#     poppedGuest = guestList.pop()
#     print(f'sorry for inconvinience {poppedGuest}')
# for i in range(0,len(guestList)):
#     print(f'you are still invited {guestList[i]}')

# del guestList[0:]
# print(guestList)

# places = ['shimla','usa','london','singapur','japan','russia']
# print(places)
# places.sort() #sort() method changes the order of the list permanantly
# places.sort(reverse=True)

# print(sorted(places)) #sorted() function temporarily changes the order of the list 
# # print(sorted(places, reverse=True))
# places.reverse()#permenantly reverses the list
# print(places)
# places.reverse()
# print(places)


#accesing list elements by using for loop
# guestList = ['mangesh','rajesh','sejal','lata','sanika','bongo']
# for guest in guestList:#for loop assigns guestList elements to the variable guest
#     print(guest)
# print(guest) #guest variable will have the last assigned value
# fruits = ['mango','chiku','orange']
# for guest in fruits:#guest variable is reusable and it won't through error.
#     print(guest)
# print(guest)


# for i in range(0,21):
#     print(i)

# list = [number for number in range(0,101)] #this syntax appends the list with the help of range function
# print(list)
# newList = list(range(2,101,2)) #can use this syntax to fill the list, here 2 is stepsize.
# print(newList)
# numbers = list(range(1, 6))
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# tableOf3 = list(range(3,33,3))
# for number in tableOf3:
#     print(number)

# for i in range(3,33,3):
#     print(i)

# cubes = [number**3 for number in range(1,11)] #one line syntax(called list comprehension) for storing the cubes inside the list.
# for cube in cubes:
#     print(cube)


# guestList = ['mangesh','rajesh','sejal','lata','sanika','bongo']
# print('\nfirst 3 names in the list are:')
# print(guestList[:3])

# print('\nmiddle 3 names in the list are:')
# print(guestList[1:4])

# print('\nlast 3 names in the list are:')
# print(guestList[-3:])


# guestList = ['mangesh','rajesh','sejal','lata','sanika','bongo']
# # nameList = guestList[:] #this syntax creates the identical but different list
# nameList = guestList #in this syntax both lists points to the list, and append in one list will chane the other list. 
# # print(nameList)
# guestList.append('swati')
# nameList.append('maddy')
# print(guestList,"\n")
# print(nameList)


#tuple
# dishes = ('pohe','vada','khichadi','chaha')
# for dish in dishes:
#     print(dish)
# prin[1] = 'coffee' #would through error as tuple does not suppoet item assignment.
# dishes = ('ratali') #we can't assign new item in old tuple, but we can reassign new items in tuples.
# print(dishes)


# dishes = ['pohe','vada','khichadi','chaha']
# dish = 'chai'
# # if dish.lower() == 'pohe':
# #     print('it is pohe')
# #     print(dish)
# # if dish.lower() != 'pohe':
# #     print(True)
# # else:
# #     print(False)

# if 'vada' in dishes:
#     print("'it's vada")
# if dish.lower() in dishes:
#     print(True)
# if dish.lower() not in dishes:
#     print(False)


# alien_colour = 'red'
# if alien_colour == 'green':
#     print('you just earned 5 points.')

# alienColour = 'red'
# if alienColour == 'green':
#     print('you fail.')

# if alien_colour == 'green':
#     print('you just earned 5 points.')
# elif alien_colour == 'yellow':
#     print('you just earned 10 points.')
# elif alien_colour == 'red':
#     print('you just earned 15 points.')
# else:
#     print('you earned 0 points.')


# age = 50
# if age < 2:
#     state = 'baby'
# elif age >= 2 and age < 4:
#     state = 'toddler'
# elif age >= 4 and age < 13:
#     state = 'kid'
# elif age >= 13 and age < 20:
#     state = 'teenger'
# elif age >=20 and age < 65:
#     state = 'adult'
# elif age >= 65:
#     state = 'elder'

# print(f'your are {state}.')

# fruits = ['mango','apple','chiku','orange','banana']

# if fruits:
#     if 'mango' in fruits:
#         print('you really like mangoes.')
#     if 'apple' in fruits:
#         print('you really like apples.')
#     if 'mosambi' in fruits:
#         print('you really like you really like mosambies.')
#     if 'chiku' in fruits:
#         print('you really like chiku.')
#     if 'mango' in fruits:
#         print('you really like mangoes.')
# else:
#     print('you sure about your favorite friut?')


# requested_fruits = ['mango','apple','chiku','orange','banana']
# available_fruits = ['apple','chiku','orange']

# for requested_fruit in requested_fruits:
#     if requested_fruit in available_fruits:
#         print(f'here take your favorite {requested_fruit}.')
#     else:
#         print(f'sorry buddy! we dont have {requested_fruit}.')


# users = ['mangesh','rohit','raj','admin','nilesh']
# if users:
#     for user in users:
#         if user == 'admin':
#             print('hey admin, would you like to watch status report?')
#         else:
#             print(f'hello {user}, Thank you for loging in again.')
# else:
#     print('We need to find some users.')


# current_users = ['John','mangesh','Mike','raja','ravi','Renu']
# new_users = ['rani','mangesh','rajat','Mike','Raju']
# #code for converting current users in lowercase
# i = 0;
# for current_user in current_users:
#     current_users[i] = current_user.lower()
#     i+=1
# # print(current_users)
# #check if username is already exists or not.
# if new_users:
#     for new_user in new_users:
#         if new_user.lower() in current_users:
#             print(f' you need to choose another username {new_user}.')
#         else:
#             print(f'welcome in the family {new_user}.')
# else:
#     print('we dont have any new users.')


# ordinals = [1,2,3,4,5,6,7,8,9,10]
# for ordinal in ordinals:
#     if ordinal == 1:
#         print('1st')
#     elif ordinal == 2:
#         print('2nd')
#     elif ordinal == 3:
#         print('3rd')
#     else:
#         print(f'{ordinal}th')


#dictionaries
#dictionaries
#dictionaries
# alien_0 = {'color':'red','points':'5','speed':'medium'}
# # print(alien_0['color'])
# # print(alien_0['points'])
# alien_0['x-coordinate'] = 0
# alien_0['y-coordinate'] =25
# # print(alien_0)

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast':
#     x_increment = 3
# alien_0['x-coordinate'] = alien_0['x-coordinate'] + x_increment
# print(alien_0)
# del alien_0['points'] #delets the key value pair parmantly.
# print(alien_0)

# mangesh = {
#     'first_name':'Mangesh',
#     'last_name':'sodnar',
#     'city':'sangamner',
#     'age':23
# }
# print(mangesh['first_name'])
# print(mangesh['last_name'])
# print(mangesh['age'])
# print(mangesh['city'])

# favoriteNum = {
#     'mangesh':3,
#     'dinesh':4,
#     'shahid':5,
#     'gokul':9,
#     'raj':4
# }
# print(favoriteNum[0]) #will through key error.
# testForRajesh = favoriteNum.get('rajesh',44)
# print(f"favorite number of mangesh is {favoriteNum['mangesh']}")
# print(f"favorite number of dinesh is {favoriteNum['dinesh']}")
# print(f"favorite number of shahid is {favoriteNum['shahid']}")
# print(f"favorite number of gokul is {favoriteNum['gokul']}")
# print(f"favorite number of rajesh is {favoriteNum.get('rajesh',43)}") #this get() method is used for avoiding error if key value is not assigned in dictionary.
# print(testForRajesh)


# grossary = {
#     'programming':'writing code',
#     'coding':'writing code for website',
#     'troubleshooting':'finding and removing errors',
#     'surfing':'searching information online',
#     'chatting':'6'
# }
# print(f"programming :\n {grossary['programming']}\n")
# print(f"coding :\n {grossary['coding']}\n")
# print(f"troubleshooting :\n {grossary['troubleshooting']}\n")
# print(f"surfing :\n {grossary['surfing']}\n")
# print(f"chatting :\n {grossary['chatting']}\n")

## above code can be written with the help of the for loop 
# for word, meaning in grossary.items(): # for key, value in dictionary.items() ###this is the syntax for looping through the dictionary. 
#     print(f"{word.capitalize()} :\n {meaning.title()}\n") #as the kyes and values are strings, we can apply the string methods.

##above code can be written with the help of the for loop 
# for word in grossary.keys():
#     print(word) 

##above code can be written with the help of the for loop as follows
# for word in grossary:#this by default assigns kyes to variable word.
#     print(word)


# favoriteLanguage = {
#     'mangesh':'python',
#     'sara':'java',
#     'john':'cpp',
#     'ravi':'C',
#     'raj':'ruby'
# }
# friends = ['sara','ravi']

# if 'erin' not in favoriteLanguage.keys():
#     print('take a pole erine.\n')

# for name in favoriteLanguage:
#     print(f"hi {name}\n")
#     if name in friends:
#         print(f"heyy {name} I see you like {favoriteLanguage[name]}\n")

#code given below allows us to loop through dictionary in a particular manner(alphabetical order)
# for name in sorted(favoriteLanguage.keys()): #alphabetical order
#     print(name)

# for name in sorted(favoriteLanguage.keys(), reverse = True): # reverse alphabetical order
#     print(name)


# favoriteLanguage = {
#     'mangesh':'python',
#     'sara':'C',
#     'john':'cpp',
#     'ravi':'C',
#     'raj':'ruby'
# }

#to access only values using loop
# for language in favoriteLanguage.values():
#     print(language)
#but this prints all values and repeatation may happen to avoid that we use set.
# for language in set(favoriteLanguage.values()):
#     print(language)

#set
#set
#set
# Friends = {'mangesh','sara','nita','ravi','raj','raj'} #can't store duplicate values.
# print(Friends)
# # print(Friends[0]) #this will through error, as set do't follow particular order,
# print(type(Friends))
# for name in Friends:
#     print(name)


#nesting : dictionaries inside list

# alien1 = {'color':'green','points':'5'}
# alien2 = {'color':'yellow','points':'10'}
# alien3 = {'color':'red','points':'15'}

# aliens = [alien1, alien2, alien3] #list of dictionaries

# for alien in aliens:
#     print(alien)

#to create the many aliens with the help of code.
# aliens = []
# for alien in range(0, 5):
#     newAlien = {'colour':'red','points':'15'}
#     aliens.append(newAlien)
# # for alien in aliens:
# #     print(alien)
# # print(f'the number of aliens created is {len(aliens)}')

# #to change the properties of some aliens
# for alien in aliens[:2]:
#     if alien['colour'] == 'red':
#         alien['colour'] = 'yellow' #here alien is a dictionary
#         alien['points'] = '10'
# for alien in aliens:
#     print(alien)
# print(f'the number of aliens created is {len(aliens)}')


# #list inside a dictionary
# #list inside a dictionary
# #list inside a dictionary
# mangesh = {
#     'age':'23',
#     'hobbies':['reading','sketching','badminton'],
#     'skills': ['python','html','c','git and github']
# }
# print(f"age of mangesh is {mangesh['age']}")
# print("he has following hobbies :")
# for hobby in mangesh['hobbies']:
#     print(f"\t{hobby.title()}")
# print("\nand he has following skills : ")
# for skill in mangesh['skills']:
#     print(f"\t{skill.title()}")


#dicrionaries inside dictionary
# students = {
#     'MangeshS':{
#         'first':'mangesh',
#         'last':'sodnar',
#         'city':'sangamner'
#     },
#     'SachineT':{
#         'first':'sachin',
#         'last':'tendulkar',
#         'city':'mumbai'
#     },
#     'RohitS':{
#         'first':'rohit',
#         'last':'sharma',
#         'city':'delhi'
#     }
# }
# #code for taking all things out from all the dictionaries.
# for student, informations in students.items():
#     print(f"\n{ student.title()} :")
#     for key, value in informations.items():
#         print(f"\t{key.title()} : {informations[key].title()}")


#dictionary inside a list
# cat = {'legs':'4','food':'milk','owner':'mangesh'}
# dog = {'legs':'4','food':'biscuits','owner':'rahul'}
# duck = {'legs':'2','food':'rice','owner':'ramu'}

# pets = [cat, dog, duck]
# i = 0
# for pet in pets:
#     print(f"\n{pets[i]} : ")
#     i+=1
#     for key, value in pet.items():
#         print(f"\t{key.title()} : {pet[key].title()}")

#list inside a dictionary
# favoritePlaces = {
#     'Mangesh':['alibag','baleshwar','singapore'],
#     'dinesh':['munbai','pune','nasik'],
#     'vasu':['mathura','hastinapur','angdesh'],
#     'shon':['kashmir','manali','kolkata']
# }
# for student, places in favoritePlaces.items():
#     print(f"\n{student.title()} :")
#     for place in places:
#         print(f"\t{place.title()}")

# #favourite numbers
# favoriteNumbers = {
#     'Mangesh':['2','3','5'],
#     'dinesh':['55','77','33'],
#     'vasu':['66','55','64'],
#     'shon':['34','64','75']
# }
# for student, numbers in favoriteNumbers.items():
#     print(f"\n{student} : ")
#     for number in numbers:
#         print(f"\t{number}")


#cities and information about it
# cities = {
#     'mumbai':{
#         'country':'india',
#         'population':'2,00,00,000',
#         'fact':'it is city full of diversity.'
#     },
#     'karachi':{
#         'country':'pakistan',
#         'population':'3,00,00,000',
#         'fact':'it is city full of terrorists.'
#     },
#     'london':{
#         'country':'united kingdom',
#         'population':'5,00,00,000',
#         'fact':'it is famous for big ben.'
#     }
# }
# #looping through first dictionary
# for city, facts in cities.items():
#     print(f"\n{city.title()} : ")
#     #looping through dictionaries inside
#     for key, value in facts.items():
#         print(f"\t{key.title()} : {facts[key].capitalize()}")


#flags
#flags
#flags
# message = '\nenter your message, i will show it back to you: '
# message += '\ntype "quit" to stop program. '
# active = True
# while active:
#     user_input = input(message)
#     print(user_input)
#     if 'quit' in user_input:
#         active = False

# prompt = "\nEnter the toppings you want on your pizza: "
# active = True
# while active:
#     topping = input(prompt)
#     if 'quit' in topping:
#         # active = False
#         break
#     else:
#         print(f"Your selected topping is {topping}.")


# copying items from one list to another by using while loop 

# unconfirmed_users = ['mangesh','jane','mandar','rajiv']
# confirmed_users = []
# #loop through unconfirmed_users
# while unconfirmed_users:
#     test_user = unconfirmed_users.pop()
#     print(f"checking registration of {test_user}.")
#     confirmed_users.append(test_user.title())
# #loop through confirmed_users
# for confirmed_user in confirmed_users:
#     print(f"welcome {confirmed_user}.")


# #removing particular value from list using while loop
# pets = ['cat','dog','cat','cow','bull']
# print(pets)
# #loop through pets to remove cats
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)


# #polling through while loop
# responses = {}
# poll_active = True
# while poll_active:
#     #taking user input for poll
#     name = input("Enter your name: ")
#     fav_politician = input("Enter your favourite politician: ")
#     responses[name] = fav_politician
#     #check for continuity of poll
#     continuity = input("to let another person poll, enter yes/no: ")
#     if 'no' in continuity:
#         poll_active = False
# #print poll result
# print("\n-----POLL RESULT-----\n")
# for name, fav_politician in responses.items():
#     print(f"{name.title()} has elected {fav_politician.title()}.")
    


# #sandwitches

# ready_sandwitches = ['peproni','cheeze','extra thick','cheeze','double','cheeze']
# finished_sandwitches = []

# #code to remove cheeze sandwitches
# print('cheeze sandwitches are out of stock.\n')
# while 'cheeze' in ready_sandwitches:
#     ready_sandwitches.remove('cheeze')

# #loop through ready_sandwitches to take order
# while ready_sandwitches:
#     ordered_sandwitch = ready_sandwitches.pop()
#     print(f"you have ordered {ordered_sandwitch}.\n")
#     finished_sandwitches.append(ordered_sandwitch)

# #loop through finished_sandwitches to print today's consumed stock.
# print("\n--finished stock--\n")
# for finished_sandwitch in finished_sandwitches:
#     print(f"{finished_sandwitch}")


# #functions

# #function defining
# def greet(user_name):
#     """The function greets the user."""
#     print(f"hello {user_name.title()}")

# #function call
# greet('mangesh')


# #favorite book

# #defining function
# def favourite_book(user,book):
#     """Prints message showings user's favorite book"""
#     print(f"{user.title()} likes {book.title()} to read.")

# #function call
# favourite_book('mangesh','alchemist')


# #t-shirt

# # defining function
# # def make_shirt(size,massage):
# #function with default arguments.
# def make_shirt(size,massage='Being Engineer!'):
#     """Prints size of the shirt and message on it."""
#     print(f"\nsize of your shirt is {size.upper()}")
#     print(f"massage on  your shirt is '{massage.upper()}'.\n")

# #function call using positional arguments
# make_shirt('slim fit','unstoppable coding machine!')

# #function call using  keyword arguments
# make_shirt(massage='unstoppable coding and reading machine!',size='slim fat')

# #function call for default arguments
# make_shirt('extra large')



# #cities and countries

# #function definition
# def describe_city(city, country='India'):
#     """prints city with country name"""
#     print(f"{city.title()} is in {country.upper()}.\n ")

# #function call using positional argumets
# describe_city('mumbai')

# #function call using keyward argument
# describe_city(city='new york',country='USA')

# #function call with only city 
# describe_city(city='surat')



# #function that returns full name

# #defining the function to give full name
# def get_full_name(first_name,last_name,middle_name=''):
#     """takes first and last names (middle name is optional) and gives full name."""
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#         return full_name.title()
#     else:
#         full_name = f'{first_name} {last_name}'
#         return full_name.title()

# #function call
# name = get_full_name('mangesh','sodnar')
# name2 = get_full_name('raj', 'kundra','babu')

# #print function outputs
# print(name)
# print(name2)



# #function that returns dictionary

# def get_dictionary_form(first_name,last_name,age=None):
#     """function that takes first , last name and age and returns dictionary"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person

# #function call
# data = get_dictionary_form('mangesh','sodnar')
# data2 = get_dictionary_form('raj','kundra',45)
# print(data)
# print(data2)



#music dictionary

# def make_album(artist,album_name,songs_count=''):
#     """takes artist ,album name and optional no of songs and returns dictionary"""
#     album = {'artist':artist.title(),'album':album_name}
#     if songs_count:
#         album['songs'] = songs_count
#     return album

# # ehile loop for taking input from prompt
# while True:
#     print("\nEnter album details.")
#     print('press q to quit any time ')
#     art_name = input('Enter artist name: ')
#     if art_name == 'q':
#         break
#     alb_name = input('Enter album name: ')
#     if alb_name == 'q':
#         break
#     songs = input('Enter songs count: ')
#     if songs == 'q':
#         break
    
#     print('Here take your album\n')
#     print(make_album(art_name,alb_name,songs))



# #pizza

# def print_pizza(available_pizza,finished_pizza):
#     """prints names of the available pizza"""
#     while available_pizza:
#         current_pizza = available_pizza.pop()
#         print(current_pizza)
#         finished_pizza.append(current_pizza)

# def print_finished_pizza(finished_pizza):
#     """prints finished pizzas"""
#     for pizza in finished_pizza:
#         print(pizza)

# available = ['peproni','thick','cheeze','peproni']
# finished = []
# print_pizza(available[:],finished) #this symbol is used to pass a copy of a list so to avoid modification of list b function.
# # print_finished_pizza(finished)
# print('here is the original list')
# print(available)



# #print massages

# def print_massages(massages,sent_massages):
#     """prints the messages from a list"""
#     while massages:
#         current_massage = massages.pop()
#         print(f"printing '{current_massage}'.")
#         sent_massages.append(current_massage)
        
# def print_sent_massages(sent_massages):
#     """prints sent messages"""
#     for massage in sent_massages:
#         print(massage)

# massages_to_send = [
#     'hello there, who are you?',
#     'welcome home.',
#     'congratulations for your success.']

# sent_massages = []

# print('\nfollowing massages need to be send: ')
# print_massages(massages_to_send[:],sent_massages)
# print('\n sent massages: ')
# print_sent_massages(sent_massages)
# print(f'here is the original list : {massages_to_send}')



# # arbitrary no of arguments

# def make_pizza(*toppings):#here toppings is a tuple
#     """takes any no of arguments and prints it"""
#     print('following are the toppings of your pizza: ')
#     for topping in toppings:
#         print(f" -{topping}")

# make_pizza('chana')
# make_pizza('chana','tomato','apple','mirchi','ratal')



# #user profile

# def make_user_profile(first,last,**user_info):
#     """make and prints the dictionary of user information."""
#     user_info['first name'] = first
#     user_info['last name'] = last
#     return user_info
#     # user_info['skills'] = 

# profile = make_user_profile('mangesh','sodnar')
# #passing multiple arguments in dictionary 
# profile1 = make_user_profile('mangesh','sodnar',address='sangamner',skill='python')
# print(profile1)



# #make car

# def make_car(manufacturer,model,**car):
#     """takes some details of car and returns dictionary"""
#     car['car manufacturer'] = manufacturer
#     car['car model'] = model
#     return car

# car1 = make_car('maruti','suzuki',color='red',seats='ventilated')
# print(car1)



# #class 

# #restaurant
# #defining a class and methods
# class Restaurant:
#     """class that replicates restaurant """
#     def __init__(self,name,menue):
#         """initiation of a class Restaurant."""
#         self.name = name
#         self.menue = menue
#         self.number_served = 50
#     def set_number_served(self,number):
#         """Sets the number of customers served."""
#         if number >= self.number_served:
#             self.number_served = number
#         else:
#             print("you can't reverse served customer value.")

#     def increment_number_served(self,increment):
#         """Takes the increment and adds it in number of customers served."""
#         self.number_served += increment

#     def describe_restaurant(self):
#         """Tells name and menue type of restaurant"""
#         print(f"\nName of the restaurant is '{self.name}'.")
#         print(f"you can get best '{self.menue}' here.")
#         print(f"it has served {self.number_served} customers.")

#     def open_restaurant(self):
#         """Prints that restaurant is open"""
#         print(f"{self.name} is open.")

# #creating an instance
# restaurant = Restaurant('baba ka dhaba','vadapav')
# restaurant.set_number_served(60)
# restaurant.increment_number_served(15)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# #creating anaother instance
# my_restaurant = Restaurant('raj palace','shevbhaji')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()



# #user

# class User:
#     """takes first and last name of user and greet them"""
#     def __init__(self,first_name,last_name):
#         """initiation of a User class."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = 45 #defining attribute without taking as input
#         self.login_attempts = 0

#     def increment_login_attempts(self):
#         """Increments ligin attempt by 1."""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """resets login attempts to 0."""
#         self.login_attempts = 0

#     def update_age(self, age):
#         """it updates the age of the user"""
#         self.age = age

#     def describe_user(self):
#         """describes the user"""
#         print(f"\nFull name of the user is {self.first_name} {self.last_name}.")
#         print(f"age of the user is {self.age}")
#         print(f"user has done {self.login_attempts} login attempts.")

#     def greet_user(self):
#         """greets the user by some massage."""
#         print(f"Welcome!! {self.first_name} {self.last_name}.")


# #instance creation
# mangesh = User('Mangesh','Sodnar')
# mangesh.age = 23 #changing attributes at creation of instance
# mangesh.increment_login_attempts()
# mangesh.reset_login_attempts()
# mangesh.describe_user()
# mangesh.greet_user()

# #another instance creation
# rajiv = User('Rajiv','Gandhi')
# rajiv.update_age(34) #updation of the age by passing it to method that changes age.
# rajiv.describe_user()



# #inheritance
# #car

# class Car:
#     """It try to replicate a car"""
#     def __init__(self,name,make,year):
#         """Initiation of attributes of class car."""
#         self.name = name
#         self.make = make
#         self.year = year
#         self.milage = 45
#         self.gas_tank_size = 70

#     def increment_milage(self,increment):
#         """Adds the increment in the milage"""
#         self.milage += increment

#     def reset_milage(self):
#         """Resets the milage."""
#         self.milage = 0

#     def gas_tank(self):
#         """Prints the capacity of the gas tank."""
#         print(f"The capacity of the gas tank is {self.gas_tank_size} litre.")
    
#     def describe_car(self):
#         """Describes the car."""
#         print(f"\n{self.year} {self.make} {self.name}")
#         print(f"milage is {self.milage}.")

# #creation of the child class
# class Electric_Car(Car):
#     """It is special group of car."""
#     def __init__(self, name, make, year):
#         """Initiation of attributes."""
#         super().__init__(name, make, year) #imports parent class attributes.
#         self.battery = 45

#     def gas_tank(self): #overriding method from parent class.
#         """Electric cars don't have gas tank"""
#         print(f"Electric cars don't have gas tank.")

#     def describe_battery(self):
#         """Describes the size of the battery."""
#         print(f"the size of battery is {self.battery} kWh.")

    
# #instance creation of Car
# honda = Car('city','Honda','2021')
# honda.increment_milage(100)
# honda.reset_milage()
# honda.describe_car()
# #instance creation of the electric car.
# my_tesla = Electric_Car('Tesla','Tesla Moters','2020')
# my_tesla.increment_milage(30)
# my_tesla.describe_car()
# my_tesla.describe_battery()
# my_tesla.gas_tank() #this is irrelevent so let's override this method inside child class.



#car

class Car:
    """It try to replicate a car"""
    def __init__(self,name,make,year):
        """Initiation of attributes of class car."""
        self.name = name
        self.make = make
        self.year = year
        self.milage = 45
        self.gas_tank_size = 70

    def increment_milage(self,increment):
        """Adds the increment in the milage"""
        self.milage += increment

    def reset_milage(self):
        """Resets the milage."""
        self.milage = 0

    def gas_tank(self):
        """Prints the capacity of the gas tank."""
        print(f"The capacity of the gas tank is {self.gas_tank_size} litre.")
    
    def describe_car(self):
        """Describes the car."""
        print(f"\n{self.year} {self.make} {self.name}")
        print(f"milage is {self.milage}.")

#creation of a class battery
class Battery:
    """It replicates a battery"""
    def __init__(self,battery_size=75):
        """Initiation of attributes of battery"""
        self.battery_size = battery_size
    
    def get_range(self):
        """It tells range of the car based on size of the battery."""
        if self.battery_size == 75:
            range = 200
        elif self.battery_size == 100:
            range = 300
        print(f"The range of the car is {range} km.")

    def upgrade_battery(self):
        """upgrades batterry to 100 kWh if it's not to that level."""
        if self.battery_size < 100:
            self.battery_size = 100

#creation of the child class
class Electric_Car(Car):
    """It is special group of car."""
    def __init__(self, name, make, year):
        """Initiation of attributes."""
        super().__init__(name, make, year) #imports parent class attributes.
        self.battery = Battery() #this attribute is instanced as battery.

    def gas_tank(self): #overriding method from parent class.
        """Electric cars don't have gas tank"""
        print(f"Electric cars don't have gas tank.")  

#instance creation of the electric car.
my_tesla = Electric_Car('Tesla','Tesla Moters','2020')
my_tesla.increment_milage(30)
my_tesla.describe_car()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.gas_tank() #this is irrelevent so let's override this method inside child class.



# #ice cream stand
# #defining a class and methods
# class Restaurant:
#     """class that replicates restaurant """
#     def __init__(self,name,menue):
#         """initiation of a class Restaurant."""
#         self.name = name
#         self.menue = menue
#         self.number_served = 50
#     def set_number_served(self,number):
#         """Sets the number of customers served."""
#         if number >= self.number_served:
#             self.number_served = number
#         else:
#             print("you can't reverse served customer value.")

#     def increment_number_served(self,increment):
#         """Takes the increment and adds it in number of customers served."""
#         self.number_served += increment

#     def describe_restaurant(self):
#         """Tells name and menue type of restaurant"""
#         print(f"\nName of the restaurant is '{self.name}'.")
#         print(f"you can get best '{self.menue}' here.")
#         print(f"it has served {self.number_served} customers.")

#     def open_restaurant(self):
#         """Prints that restaurant is open"""
#         print(f"{self.name} is open.")

# #define child class :ice cream stand
# class IceCreamStand(Restaurant):
#     """Class that replicates the ice cream stand"""
#     def __init__(self,name,menue):
#         """Initiation of class IceCreamStand"""
#         super().__init__(name,menue)
#         self.flavours = ['straberry','vanila','chocolate','almond','faluda']

#     def display_flavours(self):
#         """Prints all available flavours"""
#         print("\nfollowing flavours are available: ")
#         for flavour in self.flavours:
#             print("\t"+flavour)

# #instance creation.
# chocolicius = IceCreamStand('Chocolicius','ice scream')
# chocolicius.describe_restaurant()
# chocolicius.display_flavours()



# #admin
# class User:
#     """takes first and last name of user and greet them"""
#     def __init__(self,first_name,last_name):
#         """initiation of a User class."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = 45 #defining attribute without taking as input
#         self.login_attempts = 0

#     def increment_login_attempts(self):
#         """Increments ligin attempt by 1."""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """resets login attempts to 0."""
#         self.login_attempts = 0

#     def update_age(self, age):
#         """it updates the age of the user"""
#         self.age = age

#     def describe_user(self):
#         """describes the user"""
#         print(f"\nFull name of the user is {self.first_name} {self.last_name}.")
#         print(f"age of the user is {self.age}")
#         print(f"user has done {self.login_attempts} login attempts.")

#     def greet_user(self):
#         """greets the user by some massage."""
#         print(f"Welcome!! {self.first_name} {self.last_name}.")

# #priviladge class
# class Priviladge:
#     """Shows the priviladges tha admin gets."""
#     def __init__(self):
#         """Initiation of the priviladge class."""
#         self.priviladges = [
#                             'can add post',
#                             'can delete post',
#                             'can ban user']

#     def show_priviladges(self):
#         """Prints the priviladges that admin get."""
#         print("Admin can do following things: ")
#         for priviladge in self.priviladges:
#             print("\t",priviladge)    

# #child class admin
# class Admin(User):
#     """user that posseses special priviladges"""
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.priviladge = Priviladge() #instantiation to attribute.
    
        

    

# #instance creation
# mangesh = Admin('Mangesh','Sodnar')
# mangesh.update_age(23)
# mangesh.describe_user()
# mangesh.priviladge.show_priviladges()