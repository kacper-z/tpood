"""
Testing letter counts

"""

import pytest  # type: ignore
from tools import licz_litery
from tools import rzut_kostka


def test_licz_litery(example_data):  # pylint: disable=W0621

    example_data = ['a', 'b', 'c', 'd']

    count_data = licz_litery(example_data)

    assert len(count_data.unique()) == 4


def test_rzut_kostka():

    wynik = rzut_kostka()
    
    assert wynik <= 6