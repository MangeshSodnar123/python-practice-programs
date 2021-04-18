class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks 

    def showList(self):
        print("The available books list\n")
        for book in self.books:
            print(f"*{book}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"The book named {bookName} is successfully issued to you. Have a great reading time!")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"you have successfully returned the book named {bookName}. Have a great day.")

    def quitLib(self):
        print("Quiting the Central Library.")
        quit()

class Student:
    def takeBook(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book
    def giveBook(self):
        self.book = input("Enter the book you want to return or donate: ")
        return self.book


if __name__=="__main__":
    centralLibrary = Library(["Physics", "Chemistry","Maths","Biology","English"])
    student1 = Student()
    while True:
        print('''\n====Welcome to Central Library====\n
    (1):See available books
    (2):Borrow the book
    (3):return the book
    (4):Quit the Library\n''')

        userInput = int(input("\nchoose your action :"))

        if userInput == 1:
            centralLibrary.showList()

        elif userInput == 2:
            centralLibrary.borrowBook(student1.takeBook())

        elif userInput == 3:
            centralLibrary.returnBook(student1.giveBook())

        elif userInput == 4:
            centralLibrary.quitLib()

        else:
            print("Invalid input. Please choose valid option. ")