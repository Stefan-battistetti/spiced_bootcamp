import pandas as pd
import re
import pprint
import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
#nltk.download("wordnet")  # only done once! we have to download the WordNet database locally

from nltk.tokenize import TreebankWordTokenizer # very good tokenizer for english, considers sentence structure
from nltk.stem import WordNetLemmatizer
from sklearn.naive_bayes import MultinomialNB

#########################################################################################
#path_lyrics = '/home/damoon/damoon_spiced_academy/04_week/song_lyrics/'
path_lyrics = os.path.abspath(os.getcwd()) + '/'
prefix_url = "https://www.lyrics.com"
#############################################################################
def get_urls(url, singer_name):
    html = requests.get(url).text
    hyper_list = re.findall(pattern='<a href="(/lyric/[^"]+)', string=html)
    complete_url_list = []
    song_name_list = []
    for hyper_link in hyper_list:
        complete_url = prefix_url + hyper_link
        complete_url_list.append(complete_url)
        song_name = re.findall(pattern= singer_name + '/([^"]+)', string=hyper_link)
        song_name_list.append(song_name[0])

    dic = {'song_name': song_name_list, 'song_url': complete_url_list}
    df = pd.DataFrame(dic)
    df.drop_duplicates(['song_name'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df



#data_frame = get_urls(hyper_list, 'Blunt')

#################################################################
def download_lyrics(df, singer_name):
    os.mkdir(path_lyrics + singer_name)
    save_path = path_lyrics + singer_name+ '/'
    save_path
    #for i in range(0, df.shape[0]):
    for i in range(0, 10):     #to prevent taking long time
        file_name = df['song_name'][i]
        completeName = os.path.join(save_path, file_name)
        song_html = requests.get(df['song_url'][i]).text
        text_soup = BeautifulSoup(song_html, 'html.parser')
        lyrics = text_soup.pre.get_text()
        with open (completeName, "w") as f:
            f.write(lyrics)
        f.close()

#download_lyrics(data_frame, 'Blunt')

####################################################################
def clean_lyrics(string):
    str_no_tag = re.sub('<.*?>' ,'', string)
    str_no_nextline =re.sub('\n', ' ', str_no_tag)
    str_no_nonalpha =re.sub('\W', ' ', str_no_nextline)
    return(str_no_nonalpha)
############################open the lyrics documents and form the corpus ######################################
def make_corpus(path, singer_name, url):
    data_frame = get_urls(url, singer_name)
    download_lyrics(data_frame, singer_name)
    corpus = []
    labels = []
    open_path = path + singer_name+ '/'
    for fn in os.listdir(open_path):
        lyrics = open(open_path + fn).read()
        lyrics_cleaned = clean_lyrics(lyrics)
        corpus.append(lyrics_cleaned)
        labels.append(singer_name)
    return corpus, labels
##################################################################################################################
url1 = 'https://www.lyrics.com/artist/James-Blunt'
url2 = "https://www.lyrics.com/artist/Cher"
corpus1, labels1 = make_corpus(path_lyrics, 'Blunt', url1)
corpus2, labels2 = make_corpus(path_lyrics, 'Cher', url2)

#merge corpuses
corpus = corpus1 + corpus2
labels = labels1 + labels2
####################################################vectorization#############################################

nltk.download('stopwords')
STOPWORDS = stopwords.words('english')
print(STOPWORDS)
vectorizer = TfidfVectorizer(stop_words=STOPWORDS) # instanciation

vectors = vectorizer.fit_transform(corpus)  # fit bag of words model on our corpus


# for us to see the vectorized labeled data
pd.DataFrame(vectors.todense(), columns=vectorizer.get_feature_names(), index=labels) # check result of vectorization
#############################################################################################################
model = MultinomialNB()
model.fit(vectors, labels)
model.score(vectors, labels)

############################################################################################################
new_lyrics = ["Do you believe in life after love", "take care of your heart"]
new_vectors = vectorizer.transform(new_lyrics)
new_vectors.todense()
model.predict(new_vectors)