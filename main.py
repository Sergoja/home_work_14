from flask import Flask, jsonify
from functions import get_result, get_sqlite_duet

app = Flask(__name__)


@app.get('/movie/<title>')
def get_by_title(title: str):
    query = f"""
            SELECT title, country, release_year, listed_in, description  FROM netflix
            WHERE title = '{title}'
            ORDER BY date_added DESC
    """

    query_result = get_result(query)
    movie = {
        "title": query_result[0],
        "country": query_result[1],
        "release_year": query_result[2],
        "genre": query_result[3],
        "description": query_result[4]
    }

    return jsonify(movie)


@app.get('/movie/<year_first>/to/<year_second>')
def get_result_by_year(year_first, year_second):
    query = f"""
            SELECT title, release_year FROM netflix
            WHERE release_year BETWEEN {year_first} AND {year_second}
            AND "type" = 'Movie'
            LIMIT 100
    """
    query_result = get_result(query)
    movies = []

    for kolumn in query_result:
        movie_dict = {"release_year": kolumn[0],
                      "title": kolumn[1]}
        movies.append(movie_dict)

    return jsonify(movies)


@app.get('/rating/children')
def get_result_by_rating_children():
    query = """
                SELECT title, rating, description FROM netflix
                WHERE rating = 'G'
                LIMIT 100
        """
    query_result = get_result(query)
    movies = []

    for kolumn in query_result:
        movie_dict = {"title": kolumn[0],
                      "rating": kolumn[1],
                      "description": kolumn[2]}
        movies.append(movie_dict)

    return jsonify(movies)


@app.get('/rating/family')
def get_result_by_rating_family():
    query = """
                SELECT title, rating, description FROM netflix
                WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
                LIMIT 100
        """
    query_result = get_result(query)
    movies = []

    for kolumn in query_result:
        movie_dict = {"title": kolumn[0],
                      "rating": kolumn[1],
                      "description": kolumn[2]}
        movies.append(movie_dict)

    return jsonify(movies)


@app.get('/rating/adult')
def get_result_by_rating_adult():
    query = """
                SELECT title, rating, description FROM netflix
                WHERE rating = 'R' OR rating = 'NC-17'
                LIMIT 100
        """
    query_result = get_result(query)
    movies = []

    for kolumn in query_result:
        movie_dict = {"title": kolumn[0],
                      "rating": kolumn[1],
                      "description": kolumn[2]}
        movies.append(movie_dict)

    return jsonify(movies)


@app.get('/genre/<genre>')
def get_result_by_genre(genre: str):
    query = f"""
                SELECT title, description FROM netflix
                WHERE listed_in = '{genre}'
                ORDER BY release_year DESC
                LIMIT 10
        """
    query_result = get_result(query)
    movies = []

    for kolumn in query_result:
        movie_dict = {"title": kolumn[0],
                      "description": kolumn[1]}
        movies.append(movie_dict)

    return jsonify(movies)



if __name__ == '__main__':
    app.run(host='localhost', port=5000)

first_actor = 'Rose McIver'
second_actor = 'Ben Lamb'
list_of_actors = get_sqlite_duet(first_actor, second_actor)
print(list_of_actors)