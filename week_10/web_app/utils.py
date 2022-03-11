'''
import data here and have utility functions that could help
'''
import re
from thefuzz import process, fuzz
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF

ratings = pd.read_csv('../data/ml-latest-small/ratings.csv')
movies = pd.read_csv('../data/ml-latest-small/movies.csv', index_col=0)


def popular_movies(ratings, min_rate=2, min_users=20):
    # filter out movies with an average rating lower than 2
    avg_rating_movie = ratings.groupby('movieId')['rating'].mean()
    avg_rating_good_movies = avg_rating_movie.loc[avg_rating_movie > min_rate]
    # calculate the number of ratings per movie
    ratings_per_movie = ratings.groupby('movieId')['userId'].count()
    # filter for movies with more than 20 ratings and extract the index
    popular_movies = ratings_per_movie.loc[ratings_per_movie > min_users]

    return popular_movies, avg_rating_good_movies


def clean_ratings(ratings, popular_movies, avg_rating_good_movies):
    filtered_movie_ids = list(
        set((list(popular_movies.index)
             + list(avg_rating_good_movies.index)))
    )
    # filter the ratings matrix and only keep the popular movies
    ratings = ratings.set_index('movieId').loc[filtered_movie_ids]
    ratings = ratings.reset_index()

    return ratings


def create_user_vec(query, R):
    # the ratings of the new user
    data = list(query.values())
    # we use just a single row 0 for this user
    row_ind = [0]*len(data)
    # the columns (=movieId) of the ratings
    col_ind = list(query.keys())
    data, row_ind, col_ind

    # new user vector: needs to have the same format as the training data
    user_vec = csr_matrix((data, (row_ind, col_ind)), shape=(1, R.shape[1]))
    return user_vec


def clean_scores(scores, query):
    # convert to a pandas series
    scores = pd.Series(scores[0])
    # give a zero score to movies the user has allready seen
    scores[query.keys()] = 0
    # sort the scores from high to low
    scores.sort_values(ascending=False, inplace=True)
    # get the movieIds of the top 10 entries
    recommendations = scores.head(10).index

    return recommendations


def movie_title_search(fuzzy_title, movies):
    '''
    does a fuzzy search and returns best matched movie
    '''
    matches = process.extractBests(
        fuzzy_title, movies, limit=1, scorer=fuzz.token_set_ratio)
    return matches


def movie_to_id(title, movies):
    '''
    converts movie title to id for use in algorithms
    '''
    # If title not full
    #movieId = movies[movies.title.str.contains('Jumanji')].index[0]
    movieId = movies[movies.title == title].index
    return movieId


def id_to_movie(movieId, movies):
    '''
    converts movie Id to title
    '''
    title = movies.loc[movieId]
    return title


if __name__ == '__main__':
    # fuzzy_matches = movie_title_search(
    #     'star cars', movies.set_index('movieId')['title'])
    # print(fuzzy_matches)
    print(ratings)
