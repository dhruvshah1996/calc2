"""Testing Addition"""

import pandas as pd

from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing addition method with csv inputs"""
    df = pd.read_csv("addition_csv.csv")
    print(df.head(5))
    for x, y in df.iterrows():
        sum = (y.value_1, y.value_2)
        addition = Addition.create(sum)
        assert addition.get_result() == df['results'][x]