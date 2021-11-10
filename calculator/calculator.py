""" This is the increment function"""
#First import the addition namespace

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiply import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getresult()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        #-1 gets the last item added to the list automatically and you can expect it to have the get result method
        return Calculator.history[-1].getresult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        #create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtracts number to result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_number(value_a, value_b):
        """ multiplies number to result"""
        #This is a short hand way to creat ethe multiplication object and add it to the history in one line
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def division_number(value_a, value_b):
        """ divides number to result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
