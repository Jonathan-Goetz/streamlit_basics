import streamlit as st
import pandas as pd

dataframe = pd.read_excel("disney_messy_data_activity.xlsx", "movies_2013")

st.title("My First Streamlit Project")

st.markdown("## This is a markdown header")
st.markdown(r"""Rational preferences are defined by the following two axioms:  
    1. Completeness: $\forall a, b \in X: a \preceq b \lor b \preceq a$  
    2. Transitivity: $a \preceq b \land b \preceq c \implies a \preceq c$""")

st.markdown("## Here is some data")

selected_movies = st.multiselect(label = "Choose a movie", options = {"Frozen", "Monsters University"})

selected_data = dataframe[dataframe["title"].isin(selected_movies)]

st.dataframe(selected_data)
