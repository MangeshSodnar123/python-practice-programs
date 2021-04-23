class library:
    def __init__(self, givenBooks):
        self.givenBooks = givenBooks

    def showBooks(self):
        for book in self.givenBooks:
            print("*", book)

    def withdrawBook(self, book):
        if book in self.givenBooks:
            self.givenBooks.remove(book)

    def giveBook(self, book):
        self.givenBooks.append(book)

    def quitLib(self):
        quit()

class student:
    def takeBook(self):
        wantedBook = input("enter the wanted book: ")
        return wantedBook

    def returnBook(self):
        retBook = input("enter the book to be returned: ")
        return retBook

if __name__=="__main__":
    list1 = ["physics", "maths", "biology"]
    centralLib = library(list1) #Don't write this inside the while loop, loop will repeat inself and you would get same values for list again and again.'''
    Mangesh = student()

    while True:

        print("\n===welcome to the central library===\n")
        print('''Choose the option number
        1)Show the list of available books.
        2)Withdraw the book
        3)Return the book
        4)Exit the Library\n''')

        choice = int(input("choose one option: "))

        if choice==1:
            centralLib.showBooks()

        elif choice==2:
            centralLib.withdrawBook(Mangesh.takeBook())

        elif choice==3:
            centralLib.giveBook(student.returnBook(Mangesh))

        elif choice==4:
            centralLib.quitLib()

        else:
            print("enter the valid input.\n")
