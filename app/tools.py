import random
import string
from wordcloud import WordCloud
from matplotlib import pyplot as plt
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

def chmura_slow(text):
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Display the generated image:
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return wordcloud
