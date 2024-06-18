import random
import string
from collections import Counter
from typing import Counter as CounterType


def licz_litery(text: str) -> CounterType[str]:
    text = text.lower()
    text = "".join(filter(str.isalpha, text))

    return Counter(text)


def rzut_kostka():
    return random.randint(1, 6)


def rzut_moneta():
    return random.choice(["Orzeł", "Reszka"])


def losuj_litere():
    return random.choice(string.ascii_uppercase)
