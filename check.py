import sqlite3
from collections import Counter

from functions import get_sqlite_duet

first_actor = 'Jack Black'
second_actor = 'Dustin Hoffman'
# list_of_actors = get_sqlite_duet(first_actor, second_actor)
# print(list_of_actors)

with sqlite3.connect('data/netflix.db') as con:
    cursor = con.cursor()
    query = f"""
            SELECT "Cast" FROM netflix
            WHERE "Cast" LIKE '%{first_actor}%' And "Cast" LIKE '%{second_actor}%'
            """
    sql_result = cursor.execute(query).fetchall()

    list_of_actors = []
    for element in sql_result:
        list_of_actors += list(element)
    second_list_of_actors = []
    for actor in list_of_actors:
        second_list_of_actors += actor.split(", ")

    counter_actors = Counter(second_list_of_actors)
    print(counter_actors)

