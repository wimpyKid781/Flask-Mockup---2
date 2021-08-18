import pandas as pd;
import numpy;
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]
count = CountVectorizer(stop_words = 'english')
count_metrics = count.fit_transform(df['soup'])
cosine_sind = cosine_similarity(count,count_metrics)
df = df.reset_index()
indices = pd.Series(df.index,index = df['title'])

def get_recommendations(title):
    idx = indices(title)
    sim_scores = list(enumerate(cosine_sind[idx]))
    sim_scores = sorted(sim_scores,key = lambda x:x[1],reverse = True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title','vote_count','vote_average','posted_link']].iloc[movie_indices].values.tolist()
