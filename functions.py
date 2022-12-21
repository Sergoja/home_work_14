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


def get_sqlite_duet(first_actor, second_actor):
    query = f"""
            SELECT "Cast" FROM netflix
            WHERE "Cast" = '%{first_actor}%' And "Cast" = '%{second_actor}%'
            """
    list_of_actors = []
    for element in get_result(query):
        list_of_actors.append(element)

    return list_of_actors
