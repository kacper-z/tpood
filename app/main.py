"""
Main module for running the application.
"""
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from app.tools import chmura_slow, licz_litery, losuj_litere, rzut_kostka, rzut_moneta

# Ustawienia aplikacji
st.set_page_config(
    page_title="Prosta Aplikacja", page_icon=":game_die:", layout="centered"
)

# Tytuł aplikacji
st.title("Generator")

# Tworzenie zakładek
tab1, tab2, tab3, tab4 = st.tabs(
    ["Sprawdź ilość liter", "Rzut kostką", "Rzut monetą", "Losowanie litery"]
)

if "dice" not in st.session_state:
    st.session_state.dice = []

if "toss" not in st.session_state:
    st.session_state.toss = []

with tab1:
    st.header("Sprawdź ilość liter")
    uploaded_file = st.file_uploader("Załaduj plik", type="txt")

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        letter_counts = licz_litery(text)
        total_letters = sum(letter_counts.values())

        df = pd.DataFrame(letter_counts.items(), columns=["Litery", "Liczba wystąpień"])
        df["%"] = (df["Liczba wystąpień"] / total_letters) * 100
        df = df.sort_values(by="Liczba wystąpień", ascending=False)
        df.index = np.arange(1, len(df) + 1)

        st.write("Liczba liter:")
        st.dataframe(df)

        st.write("Chmura słów:")
        wordcloud = chmura_slow(text)
        st.pyplot(plt)

with tab2:
    st.header("Rzut kostką")
    if st.button("Rzuć kostką"):
        dice_results = rzut_kostka()
        st.session_state.dice += [dice_results]
        st.write(f"Wynik rzutu kostką: {dice_results}")

        number_counts = Counter(st.session_state.dice)
        df = pd.DataFrame(number_counts.items(), columns=["Wyrzut", "Liczba wyrzutów"])
        blank = [""] * len(df)
        df.index = blank

        st.dataframe(df)


with tab3:
    st.header("Rzut monetą")
    if st.button("Rzuć monetą"):
        toss_results = rzut_moneta()
        st.session_state.toss += [toss_results]
        st.write(f"Wynik rzutu monetą: {toss_results}")

        toss_counts = Counter(st.session_state.toss)
        df = pd.DataFrame(toss_counts.items(), columns=["Wyrzut", "Liczba wyrzutów"])
        blank = [""] * len(df)
        df.index = blank

        st.dataframe(df)

with tab4:
    st.header("Losowanie litery")
    if st.button("Losuj literę"):
        wylosowana_litera = losuj_litere()
        st.write(f"Wylosowana litera: {wylosowana_litera}")
