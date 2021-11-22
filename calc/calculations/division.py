"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def getresult(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result