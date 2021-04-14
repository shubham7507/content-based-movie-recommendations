# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:04:30 2020

@author: SHUBHAM
"""

import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('movie_metadata.csv')
#print(data.shape)
#print(data.columns)
import matplotlib.pyplot as plt

data.title_year.value_counts(dropna=False).sort_index().plot(kind='barh', figsize=(15, 16))
#print(plt.show())
# recommendation will be based on these features only
data = data.loc[:, ['movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'genres', 'director_name']]
print(data.head(10))
data['actor_1_name'] = data['actor_1_name'].replace(np.nan, 'unknown')
data['actor_2_name'] = data['actor_2_name'].replace(np.nan, 'unknown')
data['actor_3_name'] = data['actor_3_name'].replace(np.nan, 'unknown')
data['director_name'] = data['director_name'].replace(np.nan, 'unknown')
data.head()
data['genres'] = data['genres'].str.replace('|', ' ')
data
data['movie_title'] = data['movie_title'].str.lower()
data['movie_title'][1]
data['movie_title'] = data['movie_title'].apply(lambda x: x[:-1])
data


def combine_features(row):
    try:
        return row['movie_title'] + " " + row['actor_1_name'] + " " + row['actor_2_name'] + " " + row[
            'actor_3_name'] + " " + row['genres'] + " " + row['director_name']
    except:
        print("Error:", row)


data["combine_features"] = data.apply(combine_features, axis=1)
print("combine features", data["combine_features"].head())
#print(data.head())

#movie_title = 'avatar'


def create_similarity():
    # data = pd.read_csv('main_data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['combine_features'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data, similarity


def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['movie_title'].unique():
        return (
            'N')
    else:
        i = data.loc[data['movie_title'] == m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:11]  # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l


# from sklearn .externals.joblib import dump
# from sklearn .externals.joblib import load
# filename = 'nlp.pkl'
# dump(lii,open(filename,'wb'))
# loaded_model =load(open(filename,'rb'))
# clf = pickle.load(open(filename, 'rb'))
#from flask import Flask, render_template, request

#app = Flask(__name__)


#@app.route('/')
#def index():
 #   return render_template('index.html', list_example=list_example)


#    app.run(debug=True)


