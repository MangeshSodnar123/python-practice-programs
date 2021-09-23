from random import choice

#creating class lottery
class Lottery:
    """It try to replicate real world lottery."""
    def __init__(self):
        """Initiation of the class lottery"""
        self.numbers = ['1','3','A','5','6','B','7','8','2','C','4','9','0','D','E']
        self.n1 = None
        self.n2 = None
        self.n3 = None
        self.n4 = None

    def play_lottery(self):
        """generates the lucky lottery number lottery."""
        self.n1 = choice(self.numbers)#random numbers or letters are assigned to these 4 varibles.
        self.n2 = choice(self.numbers)
        self.n3 = choice(self.numbers)
        self.n4 = choice(self.numbers)
        print(f"\nthe player having '{self.n1}{self.n2}{self.n3}{self.n4}' is winner of this lottery.\n")

    def win_lottery(self):
        """It try to win lottery by looping and guessing."""
        count = 0
        for number in self.numbers:#loop for first digit
            count += 1 #count for recording number of attempts.
            if number == self.n1:
                break
        for number in self.numbers:#loop for second digit
            count += 1
            if number == self.n2:
                break
        for number in self.numbers:#loop for third digit
            count += 1
            if number == self.n3:
                break
        for number in self.numbers:#loop for fourth digit
            count += 1
            if number == self.n4:
                break
        
        print(f"It takes you {count} attempts to win this lottery.")


#create instance lottery
first_lottery = Lottery()
first_lottery.play_lottery()
first_lottery.win_lottery()