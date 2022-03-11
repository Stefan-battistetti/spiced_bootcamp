'''
    Gpt-3 API script
'''

import openai
from keys import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY


def gpt_3(films):
    '''
        function for requesting list of films from gpt-3 api
    '''
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

    return response['choices'][0]['text']
