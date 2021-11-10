"""This is our calculation base class / Abstract Class"""

class Calculation:
    # Constructor and it is the first function called when an object of the class is instantiated
    def __init__(self, value_a, value_b):
        # Constructor
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        # Creating the class method
        return cls(value_a, value_b)
