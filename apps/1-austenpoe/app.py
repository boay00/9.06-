import streamlit as st
import pandas as pd
import pickle

st.title("Austen or Poe?")
st.subheader("Who do you write like?")

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Predicting')
)

if page == 'About':
    st.subheader('About this Project')
    st.write("""This is a streamlit app. 
It'll tell you who like write like, etc.""")

if page == 'EDA':
    st.subheader('Exploration Nation!')

if page == 'Predicting':
    st.title('Who do you write like?')
    model_1, model_2 = st.tabs(['Model 1', 'Model 2'])
    with model_1:
        st.write("Test out model 1")

    with model_2:
        st.write('Test out model 2')
        number = st.slider("Choose a number", 0, 10)

        st.metric('My Number', number)