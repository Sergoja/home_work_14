import sqlite3

with sqlite3.connect("data/netflix.db") as con:
    cur = con.cursor()
    sqlite_query = """
    SELECT * FROM netflix
            WHERE title = 'Abyss'
            ORDER BY date_added DESC
    """
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    result = result[0]
    all_tables = []
    for item in result:
        s = dict(item)
        all_tables.append(s)


if __name__ == '__main__':
    print(all_tables)