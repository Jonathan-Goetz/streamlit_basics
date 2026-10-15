import streamlit as st

st.title("My First Streamlit Project")

st.markdown("## This is a markdown header")
st.markdown(r"""Rational preferences are defined by the following two axioms:  
    1. $\forall a, b \in X: a \preceq b \lor b \preceq a$  
    2. $a \preceq b \land b \preceq c \implies a \preceq c$""")

st.markdown("## Here is some data")
st.dataframe()