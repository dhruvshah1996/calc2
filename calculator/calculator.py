""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def addition(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result
    def subtraction(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result
    def multiplication(self, value_a, value_b):
        """ multiply two numbers and store the result"""
        self.result = value_a * value_b
        return self.result
    def division(self, value_a, value_b):
        """ Divide two numbers and store the result"""
        self.result = value_a / value_b
        return self.result
