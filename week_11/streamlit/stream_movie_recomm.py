'''
    main.py using streamlit to create a webapp
'''


# import std libraries
import streamlit as st
from gpt_3 import gpt_3
from keys import OPENAI_API_KEY
import openai
# Write a title
st.write('Film recommender')
# Put image
st.image('img_ai.jpg')
# Write heading for Data
st.header('')
films = (st.text_input(
    'Give me a list of two films, separate them with a comma')).split(',')


if len(films) > 1:
    st.write('here the list of films you might like ;)')
    st.write(gpt_3(films))
