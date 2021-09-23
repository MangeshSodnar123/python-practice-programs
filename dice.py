from random import randint

#creating class die
class Die:
    """class tha replicates die with n sides"""
    def __init__(self, sides):
        """Initiation of class die"""
        self.sides = sides

    def roll_die(self):
        """generates a random number replicating through of a die."""
        face_up = randint(1,self.sides)
        print(f"You got {face_up}.")

#creating instance of class die
my_die = Die(6)
# my_die.roll_die()

your_die = Die(10)
# your_die.roll_die()

her_die = Die(20)
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()
her_die.roll_die()