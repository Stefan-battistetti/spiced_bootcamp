'''
import data here and have utility functions that could help
'''

# from thefuzz import process, fuzz
import pandas as pd
from imdb import Cinemagoer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

tmdv_credits = pd.read_csv("./data/tmdb_5000_credits.csv")
tmdv_movies = pd.read_csv("./data/tmdb_5000_movies.csv")
reco_df = pd.read_csv("./data/reco_mat.csv")
#model = ...


def convert(text):
    '''
    convert list to set of strings
    '''
    keyword_list = []
    for i in ast.literal_eval(text):
        keyword_list.append(i['name']) 
    return keyword_list

def get_director(text):
    ''' 
    extract directors name from list
    '''
    directors = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            directors.append(i['name'])
    return directors 

# def get_sim_matrix(df_col):
#     '''
#     running model on df
#     '''
#     cv = CountVectorizer(max_features=5000)
#     count_matrix = cv.fit_transform(df_col).toarray()
#     similarity = cosine_similarity(count_matrix)
#     return similarity

# def movie_title_search(fuzzy_title, movies):
#     '''
#     does a fuzzy search and returns best matched movie
#     '''
#     matches = process.extractBests(fuzzy_title, movies, limit=1, scorer=fuzz.token_set_ratio)
#     return matches

# def movie_to_id(title, movies):
#     '''
#     converts movie title to id for use in algorithms
#     '''
#     return movieId

# def id_to_movie(movieId, movies):
#     '''
#     converts movie Id to title
#     '''
#     return title

# if __name__ == '__main__':
#     fuzzy_matches = movie_title_search('star cars', movies.set_index('movieId')['title'])
#     print(fuzzy_matches)
