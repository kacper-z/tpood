"""
Testing a dice throw

"""
import pytest  # type: ignore
import matplotlib.pyplot as plt # type: ignore
from tools import rzut_kostka
from tools import rzut_moneta



# check if the result values are between 1 and 6, like in a standard dice
def test_rzut_kostka():

    wynik = []
    for i in range(1000):
        wynik.append(rzut_kostka())
    wynik = [int(d) for d in wynik]
    max_val = max(wynik)
    min_val = min(wynik)
    assert (max_val <= 6) & (min_val >= 1)





# check if there are only 2 unique values when throwing a coin
def test_rzut_moneta():

    wynik = []
    for i in range(1000):
        wynik.append(rzut_moneta())
    wynik = list(set(wynik))
    assert len(wynik) == 2