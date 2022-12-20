from flask import Flask, jsonify
from functions import get_result

app = Flask(__name__)


@app.get('/movie/<title>')
def get_by_title(title: str):
    query = f"""
            SELECT * FROM netflix
            WHERE title = '{title}'
            ORDER BY date_added DESC
    """

    query_result = get_result(query)
    movie = {
        "title": query_result['title'],
        "country": query_result['country'],
        "release_year": query_result['release_year'],
        "genre": query_result['listed_in'],
        "description": query_result['description']
    }

    return jsonify(movie)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
