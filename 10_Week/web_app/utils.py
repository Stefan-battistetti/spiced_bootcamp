'''
import data here and have utility functions that could help
'''
from thefuzz import process, fuzz
import pandas as pd

movies = pd.read_csv('./data/movies.csv')
ratings = pd.read_csv('./data/ratings.csv')
#model = ...

#print(movies.head(5))

def movie_title_search(fuzzy_title, movies):
    '''
    does a fuzzy search and returns best matched movie
    '''
    matches = process.extractBests(fuzzy_title, movies, limit=1, scorer=fuzz.token_set_ratio)
    return matches

def movie_to_id(title, movies):
    '''
    converts movie title to id for use in algorithms
    '''
    return movieId

def id_to_movie(movieId, movies):
    '''
    converts movie Id to title
    '''
    return title

if __name__ == '__main__':
    fuzzy_matches = movie_title_search('star cars', movies.set_index('movieId')['title'])
    print(fuzzy_matches)
