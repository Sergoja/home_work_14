import sqlite3


def get_result(query: str):
    """

    """
    with sqlite3.connect('data/netflix.db') as con:
        cursor = con.cursor()
        sql_result = cursor.execute(query).fetchall()

        return sql_result


def get_one_str(query: str):
    """

    """
    with sqlite3.connect("data/netflix.db") as con:
        con.row_factory = sqlite3.Row
        result = dict(con.execute(query).fetchone())

        return result


# def get_sqlite_rating()