"""Testing Addition"""
import logging

import pandas as pd
import os
import logging as log
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing addition method with csv inputs"""
    df = pd.read_csv("CSVFiles/Multiplication.csv")
    print(df.head(10))
    for x, y in df.iterrows():
        mul = (y.Value_1, y.Value_2)
        multiplication = Multiplication.create(mul)
        logging.basicConfig(filename='Log files/logFile.csv')
        logging.info('This should be recorded')
        assert multiplication.get_result() == df['Result'][x]