from flask import Flask, request, render_template
from matplotlib.pyplot import title
from movie_recommender import recommend_random, recommend_neighbors, recommend_popular,recommend_nmf
from utils import movies

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('MR_landing_page.html')

@app.route('/recommender/')
def recomm():
    recommended_matched_titles = recommend_random()
    popular_titles = recommend_popular()
    NMF_titles = recommend_nmf()
    NN_titles= recommend_neighbors()
    return render_template('MR_recommender.html',
                            recommended_matched_titles=recommended_matched_titles,
                            popular_titles=popular_titles,
                            NMF_titles=NMF_titles,
                            NN_titles=NN_titles)


if __name__=='__main__':
    app.run(debug=True)
