class User:
    """takes first and last name of user and greet them"""
    def __init__(self,first_name,last_name):
        """initiation of a User class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = 45 #defining attribute without taking as input
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increments ligin attempt by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets login attempts to 0."""
        self.login_attempts = 0

    def update_age(self, age):
        """it updates the age of the user"""
        self.age = age

    def describe_user(self):
        """describes the user"""
        print(f"\nFull name of the user is {self.first_name} {self.last_name}.")
        print(f"age of the user is {self.age}")
        print(f"user has done {self.login_attempts} login attempts.")

    def greet_user(self):
        """greets the user by some massage."""
        print(f"Welcome!! {self.first_name} {self.last_name}.")