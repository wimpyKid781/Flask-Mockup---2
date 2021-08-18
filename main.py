from flask import Flask,jsonify
import csv

all_movies = []
with open("movies.csv", encoding='utf8') as f:
    reader_data = csv.reader(f)
    data  = list(reader_data)
all_movies = data[1:]
like_movies = []
dislike_movies = []
not_watched_movies = []

app = Flask(__name__)
@app.route('/get-movie')
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":'success'
    })
@app.route("/liked-movie",methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies.pop(0)
    like_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-movie",methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies.pop(0)
    dislike_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-watch",methods = ["POST"])
def did_not_watch_movie():
    movie = all_movies[0]
    all_movies.pop(0)
    not_watched_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
            "title":movie[0],
            "poster_link":movie[1],
            "release_date":movie[2] or "M/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5],
            
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    }),200
@app.route('/recommended-movie')
def recommended_moives():
    all_recommed = []
    for liked_movie in liked_movie:
        output  = get_recommendations(liked_movie[19])
        for data in output:
            all_recommed.append(data)
    import itertools;
    all_recommed.sort()
    all_recommed = list(all_recommed for all_recommed,_ in itertools.groupby(all_recommed))
    movie_data = []
    for recommded in all_recommed:
        _d = {
            "title":recommded[0],
            "poster_link":recommded[1],
            "release_date":recommded[2] or "M/A",
            "duration":recommded[3],
            "rating":recommded[4],
            "overview":recommded[5]
        }
    movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":'success'
    }),200



if __name__ == "__main__":
    app.run(debug=True)