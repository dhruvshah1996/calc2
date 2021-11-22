"""Testing Multiplication"""
from calc.calculations.division import Division

def test_calculation_multiplication():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (6.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.getresult() == 3.0