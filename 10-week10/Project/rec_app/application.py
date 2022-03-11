from flask import Flask, request, render_template
from recommender import recommend_random, recommend_neighbors, recommend_neighbour_movie
from utils import movies, movie_title_search

# we instanciate the flask oject, (__name__) used to declare this file as the home script 
app = Flask(__name__)

# each view (or webpage) is defined by a function and app.route tells flask at which URL to render it
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/recommender/')
def recommender():
    '''
    recommends movies based on cosine sim score
    '''
    recs = recommend_neighbour_movie(movies)
    #pass recs to html and render
    return render_template('recommender.html', matched_titles=matched_titles)


# ensures the code below is only executed when this file is directly run
if __name__=='__main__':
    # runs app and sets debug level on so that the errors are shows in the terminal
    # and the server restarts when any changes are made to this file!
    app.run(debug=True)
