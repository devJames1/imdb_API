from flask import Flask, request
import csv
import json
app = Flask(__name__)


@app.route('/')
def genre_film():
    genre = request.args.get('genre')
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        print('ehhl')
        for movie in reader:
            if genre  in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

@app.route('/action')
def genre_film_action():
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        # print('ehhl')
        for movie in reader:
            if "Action" in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

@app.route('/adventure')
def genre_film_adventure():
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        # print('ehhl')
        for movie in reader:
            if "Adventure" in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

@app.route('/comedy')
def genre_film_comedy():
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        # print('ehhl')
        for movie in reader:
            if "Comedy" in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

@app.route('/drama')
def genre_film_drama():
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        # print('ehhl')
        for movie in reader:
            if "Drama" in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

@app.route('/romance')
def genre_film_romance():
    movies_csv_file = 'imdb-movie-data.csv'
    with open(movies_csv_file, newline ="") as csvfile:
        reader = csv.DictReader(csvfile)
        movies =[]
        # print('ehhl')
        for movie in reader:
            if "Romance" in movie["Genre"]:
                movies.append(movie)
        return json.dumps(movies)

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080)
