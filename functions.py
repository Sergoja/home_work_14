import sqlite3


def get_result(query: str):
    """

    """
    with sqlite3.connect('data/netflix.db') as con:
        cursor = con.cursor()
        cursor = cursor.execute(query).fetchall()
        result = []

        for item in cursor.execute(query).fetchall():
            s = dict(item)

            result.append(s)

        return result


def get_one_str(query: str):
    """

    """
    with sqlite3.connect("data/netflix.db") as con:
        con.row_factory = sqlite3.Row
        result = dict(con.execute(query).fetchone())

        return result

title = 'Abyss'
query = f"""
            SELECT * FROM netflix
            WHERE title = '{title}'
            ORDER BY date_added DESC
    """
a = get_result(query)
print(a)