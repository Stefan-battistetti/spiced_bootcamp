"""
contains various implementations for recommending movies
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import movies, ratings, reco_df, get_sim_matrix


def recommend_neighbour_movie(movie_title):
    """
    Runs model and gets movies simimlar to original title
    """
    cv = CountVectorizer(max_features=5000)
    count_matrix = cv.fit_transform(reco_df["comb_feat"]).toarray()
    similarity = cosine_similarity(count_matrix)

    index = reco_df[reco_df['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(reco_df.iloc[i[0]].title)


# recommender_systems_intro_filled.ipynb
def recommend_random(query, ratings, k=10):
    """
    Recommends a list of k random movie ids
    """
    return [1, 20, 34, 25]


# recommender_systems_intro_filled.ipynb
def recommend_popular(query, ratings, k=10):
    """
    Recommend a list of k movie ids that are the most popular
    """
    return []


# matrix_factorization_filled.ipynb
def recommend_nmf(query, model, ratings, k=10):
    """
    Recommend a list of k movie ids based on a trained NMF model
    """
    return []


# neighborhood_based_filtering.ipynb
def recommend_neighbors(query, model, ratings, k=10):
    """
    Recommend a list of k movie ids based on the most similar users
    """
    return []


if __name__=='__main__':
    # list of liked movies
    query = [1, 34, 56, 21]
    print(recommend_random(query, movies))
