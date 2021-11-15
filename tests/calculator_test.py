"""Testing the Calculator_main"""
from calculator.calculator import Calculator

def test_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_get_result():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Assert that the results are correct
    assert calc.get_result() == 0

def test_addition():
    """Testing the Add function of the calculator"""
    #Calls the calculator class from main.py
    calc = Calculator()
    #Calls the add function from main.py and inputs static number.
    calc.addition(8)
    #Assert that the results are correct
    assert calc.result == 8

def test_subtract():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the subtract function from main.py and inputs static number.
    calc.subtraction(2)
    # Assert that the results are correct
    assert calc.get_result() == -2
def test_multiply():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the multiplication function from main.py and inputs static number.
    result  = calc.multiplication(2,2)
    # Assert that the results are correct
    assert result == 4
def test_divison():
    """Calls the calculator class from main.py"""
    calc = Calculator()
    # Calls the division function from main.py and inputs static number.
    result = calc.division(6,3)
    # Assert that the results are correct
    assert result == 2
