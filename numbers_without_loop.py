ten = "**********"
one = "*"
def call_Me(argument):
    '''this function  prints the argument value and adds one in it''' #this is syntex of docstring
    if argument <= len(ten)*len(ten):
        print(argument)
        return call_Me(argument+len(one))
call_Me(len(one))
print(call_Me.__doc__) #this is syntex for calling the docstring