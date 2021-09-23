import user 


#priviladge class
class Priviladge:
    """Shows the priviladges tha admin gets."""
    def __init__(self):
        """Initiation of the priviladge class."""
        self.priviladges = [
                            'can add post',
                            'can delete post',
                            'can ban user']

    def show_priviladges(self):
        """Prints the priviladges that admin get."""
        print("Admin can do following things: ")
        for priviladge in self.priviladges:
            print("\t",priviladge)    

#child class admin
class Admin(user.User):
    """user that posseses special priviladges"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviladge = Priviladge() #instantiation to attribute.
    
        

    

