"""
contains various implementations for recommending movies
"""

from distutils.command.clean import clean
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import random
import pickle
from utils import movies, ratings, popular_movies, clean_ratings, create_user_vec, clean_scores


# recommender_systems_intro_filled.ipynb
def recommend_random(query, movies, k=10):
    """
    Recommends a list of k random movie ids
    """
    movies = movies.drop(index=query.keys())
    list_ids = random.choices(
        movies.index, weights=None, cum_weights=None, k=k)
    return list_ids


# recommender_systems_intro_filled.ipynb
def recommend_popular(query, ratings, k=10):
    """
    Recommend a list of k movie ids that are the most popular
    """
    ratings, _ = popular_movies(ratings)
    ratings.set_index('movieId').drop(index=query.keys(), inplace=True)
    popular_ids = ratings.sort_values(ascending=False)[:k]
    return popular_ids


# matrix_factorization_filled.ipynb
def recommend_nmf(query, ratings, model='../models/nmf_recommender.pkl', k=10):
    """
    Recommend a list of k movie ids based on a trained NMF model
    """
    ratings = clean_ratings(ratings, popular_movies(ratings))
    with open(model, 'rb') as file:
        model_nmf = pickle.load(file)
    # Initialize a sparse user-item rating matrix
    # (data, (row_ind, col_ind)
    R = csr_matrix(
        (ratings['rating'], (ratings['userId'], ratings['movieId'])))
    user_vec = create_user_vec(query, R)
    # user_vec -> encoding -> p_user_vec -> decoding -> user_vec_hat
    scores = model_nmf.inverse_transform(model.transform(user_vec))
    recommendations = clean_scores(scores, query)

    return recommendations


# neighborhood_based_filtering.ipynb
def recommend_neighbors(query, ratings, model='../models/distance_recommender.pkl', k=10):
    """
    Recommend a list of k movie ids based on the most similar users
    """
    ratings = clean_ratings(ratings, popular_movies(ratings))
    R = csr_matrix(
        (ratings['rating'], (ratings['userId'], ratings['movieId'])))
    # initialize the unsupervised model
    model = NearestNeighbors(metric='cosine')
    # fit it to the user-item rating matrix
    model.fit(R)
    # create user vector
    user_vec = create_user_vec(query, R)
    # calculates the distances to all other users in the data!
    distances, userIds = model.kneighbors(
        user_vec, n_neighbors=10, return_distance=True
    )
    # sklearn returns a list of predictions - extract the first and only value of the list
    distances = distances[0]
    userIds = userIds[0]
    # only look at ratings for users that are similar!
    neighborhood = ratings.set_index('userId').loc[userIds]
    scores = neighborhood.groupby('movieId')['rating'].mean()
    recommendations = clean_scores(scores, query)

    return recommendations


if __name__ == '__main__':
    # list of liked movies
    query = [1, 34, 56, 21]
    print(recommend_random(query, movies))
