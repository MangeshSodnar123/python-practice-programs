# ice cream stand
#defining a class and methods
class Restaurant:
    """class that replicates restaurant """
    def __init__(self,name,menue):
        """initiation of a class Restaurant."""
        self.name = name
        self.menue = menue
        self.number_served = 50
    def set_number_served(self,number):
        """Sets the number of customers served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("you can't reverse served customer value.")

    def increment_number_served(self,increment):
        """Takes the increment and adds it in number of customers served."""
        self.number_served += increment

    def describe_restaurant(self):
        """Tells name and menue type of restaurant"""
        print(f"\nName of the restaurant is '{self.name}'.")
        print(f"you can get best '{self.menue}' here.")
        print(f"it has served {self.number_served} customers.")

    def open_restaurant(self):
        """Prints that restaurant is open"""
        print(f"{self.name} is open.")

#define child class :ice cream stand
class IceCreamStand(Restaurant):
    """Class that replicates the ice cream stand"""
    def __init__(self,name,menue):
        """Initiation of class IceCreamStand"""
        super().__init__(name,menue)
        self.flavours = ['straberry','vanila','chocolate','almond','faluda']

    def display_flavours(self):
        """Prints all available flavours"""
        print("\nfollowing flavours are available: ")
        for flavour in self.flavours:
            print("\t"+flavour)



