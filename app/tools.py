"""
This module provides utility functions for various tasks.
"""
import random
import string
from collections import Counter
from typing import Counter as CounterType

from matplotlib import pyplot as plt
from wordcloud import WordCloud


def licz_litery(text: str) -> CounterType[str]:
    """    Counts the number of letters in a given text.
"""
    text = text.lower()
    text = "".join(filter(str.isalpha, text))

    return Counter(text)


def rzut_kostka():
    """Simulates a dice roll"""
    return random.randint(1, 6)


def rzut_moneta():
    """Simulates a coin roll"""
    return random.choice(["Orzeł", "Reszka"])


def losuj_litere():
    """ Randomly selects a letter from the alphabet."""
    return random.choice(string.ascii_uppercase)

def chmura_slow(text):
    """Generate a word cloud image"""

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        text
    )

    # Display the generated image:
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    return wordcloud
