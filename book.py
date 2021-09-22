def favourite_book(user,book):
    """Prints message showings user's favorite book"""
    print(f"{user.title()} likes {book.title()} to read.")

from book import favourite_book

favourite_book('mangesh','alchemist')