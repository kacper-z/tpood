"""
Testing a dice throw

"""

import pytest  # pylint: disable=unused-import
import matplotlib.pyplot as plt  # pylint: disable=unused-import
from .tools import rzut_kostka
from .tools import rzut_moneta


# check if the result values are between 1 and 6, like in a standard dice
def test_rzut_kostka():
    """
    Test the function rzut_kostka().

    This function tests the rzut_kostka() function by generating 1000 random dice rolls
    and checking if the maximum value is less than or equal to 6 and the minimum value
    is greater than or equal to 1.

    Returns:
        None
    """
    wynik = []
    for _ in range(1000):
        wynik.append(rzut_kostka())
    wynik = [int(d) for d in wynik]
    max_val = max(wynik)
    min_val = min(wynik)
    assert (max_val <= 6) & (min_val >= 1)


# check if there are only 2 unique values when throwing a coin
def test_rzut_moneta():
    """
    Test function for the rzut_moneta() function.

    This function performs 1000 coin tosses using the rzut_moneta() 
    function and checks if the result contains only 2 unique values.
    """

    wynik = []
    for _ in range(1000):
        wynik.append(rzut_moneta())
    wynik = list(set(wynik))
    assert len(wynik) == 2
