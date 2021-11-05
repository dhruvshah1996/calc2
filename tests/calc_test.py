from calculator.calc import Calculator

def calctest_result():
    calc = Calculator()
    assert calc.result == 0

def caltest_add():
    calc = Calculator()
    calc.addition(4)
    assert calc.result == 4