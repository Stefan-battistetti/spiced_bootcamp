import pandas as pd
from utils import movies, ratings
import random
from flask import request
import pickle
from scipy.sparse import csr_matrix


def recommend_random():
    user_movies = [int(i) for i in request.args.getlist('movies')]
    movie_ids = [random.randint(1,9741) for i in range(0,5) if random.randint(1,9741) not in user_movies]
    recs = [movies['title'][i] for i in movie_ids if i in movies['movieId']]
    return dict(zip(movie_ids,recs))


def recommend_popular():
    ratings_per_movie = ratings.groupby('movieId')['userId'].count()
    popular_movies = (ratings_per_movie.loc[ratings_per_movie > 20]).head(5)
    recsus = [movies['title'][i] for i in popular_movies if i in movies['movieId']]
    return dict(zip(popular_movies,recsus))


def recommend_nmf():
    user_movieha = [int(i) for i in request.args.getlist('movies')]
    top_5 = [5,5,5,5,5]
    query = dict(zip(user_movieha,top_5))
    with open('./nmf_recommender.pkl', 'rb') as file:
        model = pickle.load(file)
    data = list(query.values())       
    row_ind = [0]*len(data)             
    col_ind = list(query.keys())           
    user_vec = csr_matrix((data, (row_ind, col_ind)), shape=(1, 168253))
    scores = pd.Series((model.inverse_transform(model.transform(user_vec)))[0])
    scores[query.keys()] = 0
    scores = scores.sort_values(ascending=False)
    recommendations = scores.head(5).index
    recommendations = movies.set_index('movieId').loc[recommendations]
    return recommendations['title']


def recommend_neighbors():
    user_movieha = [int(i) for i in request.args.getlist('movies')]
    top_5 = [5,5,5,5,5]
    query = dict(zip(user_movieha,top_5))
    with open('./NearestNeighbors_recommender.pkl', 'rb') as file:
        model = pickle.load(file)
    data = list(query.values())
    row_ind = [0]*len(data)
    col_ind = list(query.keys())
    data, row_ind, col_ind
    user_vec = csr_matrix((data, (row_ind, col_ind)), shape=(1, 168253))
    distances, userIds = model.kneighbors(user_vec, n_neighbors=10, return_distance=True)
    distances = distances[0]
    userIds = userIds[0]
    neighborhood = ratings.set_index('userId').loc[userIds]
    scores = neighborhood.groupby('movieId')['rating'].mean()
    scores.loc[scores.index.isin(query.keys())] = 0 
    scores.sort_values(ascending=False,inplace=True)
    scores_5 = scores.head(5)
    recommendations = movies.set_index('movieId').loc[scores_5.index]
    return recommendations['title']


if __name__=='__main__':
    query = [1, 34, 56, 21]
    print(recommend_random(query, movies))
