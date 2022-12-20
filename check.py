import sqlite3


year_first = 2010
year_second = 2011
with sqlite3.connect("data/netflix.db") as con:
    cur = con.cursor()
    sqlite_query = f"""
    SELECT title, release_year FROM netflix
            WHERE release_year BETWEEN {year_first} AND {year_second}
            AND "type" = 'Movie'
            LIMIT 100
    """
    sql_result = cur.execute(sqlite_query).fetchall()


if __name__ == '__main__':
    print(sql_result)
