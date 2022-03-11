# import std libraries
from keys import OPENAI_API_KEY
import openai
import streamlit as st
from gpt_3 import gpt_3

# Write a title
st.write('Film recommender')
# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image('https://unsplash.com/photos/zwd435-ewb4')
# Write heading for Data
st.header('')
films = (st.text_input(
    'Give me a list of two films, separate them with a comma')).split(',')


openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=f"List 10 films similar to {films[0]} and {films[1]}:",
    temperature=0.6,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0.52,
    presence_penalty=0.5,
    stop=["11."]
)

st.write(response['choices'][0]['text'])
