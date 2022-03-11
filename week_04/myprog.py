from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import requests
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download(
    "wordnet"
)  # only done once! we have to download the WordNet database locally


# It returns a regular Python list
eng_stop_words = stopwords.words("english")


####################### FUNCTIONS #####################
def scrape_lyrics(link):
    """
        Function scraper, create a wordcloud, return list of lyrics, and relative artist name
    """

    prefix_url = "https://www.lyrics.com"
    complete_url_list = []
    lst_lyrics = []
    lst_artist = []

    artist = link.split("/")[-2]  # get name artist
    html = requests.get(link).text  # scrape page artist
    # with open(f"html_{artist}.txt", "w") as f:  # write down the page on a file
    #    f.write(html)

    hyper_list = re.findall(
        pattern='/lyric/[^"]+', string=html
    )  # take out the lyrics' links

    for h in hyper_list:  # create list with working links
        complete_url_list.append(prefix_url + h)

    for i in complete_url_list:  # scrape lyrics
        request_response = requests.head(i)
        status_code = request_response.status_code
        if status_code == 200:
            lst_lyrics.append(
                BeautifulSoup(requests.get(i).text, "html.parser")
                .find(id="lyric-body-text")
                .text.lower()
            )
            lst_artist.append(artist)
        else:
            continue

    # ________Wordcloud_________

    data = pd.DataFrame({"text": lst_lyrics})
    text = " ".join(i for i in data.text)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color="white").generate(text)
    # plt.figure( figsize=(30,20))
    plt.title(f"Wordcloud {artist}")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f"cloud{artist}.svg", format="svg", dpi=1200)
    # plt.show()

    # write down the lyrics on a file
    with open(f"lst_lyrics_{artist}.txt", "w") as f:
        for item in lst_lyrics:
            f.write("%s\n" % item + "\n" + "_____" + "\n")

    with open(
        f"lst_artist_{artist}.txt", "w"
    ) as f:  # write down the artist list on a file
        for item in lst_artist:
            f.write("%s\n" % item)

    return lst_lyrics, lst_artist


# -----------------------------------


def cleaning(lst):
    """
            Function for cleaning the corpus from numbers and special chars
    """

    clean_lst = [
        re.sub(r"([^a-zA-Z ]+?)", " ", l) for l in lst
    ]
    return clean_lst


def features_split(link1, link2):
    """

    """

    lst_lyr_1, lst_art_1 = scrape_lyrics(link1)
    lst_lyr_2, lst_art_2 = scrape_lyrics(link2)

    X = cleaning(lst_lyr_1) + cleaning(lst_lyr_2)
    y = lst_art_1 + lst_art_2
    X = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=10, stratify=y
    )
    return X_train, X_test, y_train, y_test


# ------------------------------------
# Script for checking which artist belongs a text given two lyrics.com artist's links

vectorizer = TfidfVectorizer(stop_words=eng_stop_words)

lnk_1, lnk_2 = input(
    "Give me two links of your favorite artists profile page in lyrics.com..."
).split()

text_test = input(
    "Thank you, now please give me a test to check..").splitlines()
print(text_test)

X_train, X_test, y_train, y_test = features_split(lnk_1, lnk_2)
print("I")

model = MultinomialNB()
model = model.fit(X_train, y_train)  # model.fit
print(f"Your model's score is {model.score(X_test, y_test)}")


t = vectorizer.transform(cleaning(text_test[0]))
prediction = model.predict(t)
print(prediction)
