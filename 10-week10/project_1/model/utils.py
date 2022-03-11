from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pandas as pd

def create_user_vec(query, R):
    data = list(query.values())             # the ratings of the new user
    row_ind = [0]*len(data)              # we use just a single row 0 for this user 
    col_ind = list(query.keys())                           # the columns (=movieId) of the ratings
    #data, row_ind, col_ind

    user_vec = csr_matrix((data, (row_ind, col_ind)), shape=(1, R.shape[1]))
    return user_vec


ratings = pd.read_csv("../../project/data/ml-latest-small/ratings.csv")
movies = pd.read_csv("../../project/data/ml-latest-small/movies.csv")

def get_ratings_matrix(ratings):
    # calculate the number of ratings per movie
    ratings_per_movie = ratings.groupby('movieId')['rating'].count()

    # filter for movies with more than 20 ratings and extract the index
    popular_movies = ratings_per_movie.loc[ratings_per_movie > 20]

    # filter the ratings matrix and only keep the popular movies
    ratings_pop = ratings.loc[ratings['movieId'].isin(popular_movies.index)]

    # Initialize a sparse user-item rating matrix
    # (data, (row_ind, col_ind)
    R = csr_matrix((ratings_pop['rating'], (ratings_pop['userId'], ratings_pop['movieId'])))
    return R


