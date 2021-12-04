"""Testing Addition"""
import pandas as pd
from calc.calculations.multiplication import Multiplication

def test_calculation_addition():
    """testing addition method with csv inputs"""
    df = pd.read_csv("Multiplication.csv")
    print(df.head(2))
    for x, y in df.iterrows():
        mul = (y.Value_1, y.Value_2)
        multiplication = Multiplication.create(mul)
        assert multiplication.get_result() == df['Result'][x]