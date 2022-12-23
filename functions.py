import json
import sqlite3
from collections import Counter


def get_result(query: str):
    """
    Функция, получает SQL-запрос и выдаёт результат работы запроса с БД
    """
    with sqlite3.connect('data/netflix.db') as con:
        cursor = con.cursor()
        sql_result = cursor.execute(query).fetchall()

        return sql_result


def get_sqlite_duet(first_actor, second_actor):
    """
    Функция, которая получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки cast
    и возвращает список тех, кто играет с ними в паре больше 2 раз.
    """
    with sqlite3.connect('data/netflix.db') as con:
        cursor = con.cursor()
        query = f"""
                SELECT "Cast" FROM netflix
                WHERE "Cast" LIKE '%{first_actor}%' And "Cast" LIKE '%{second_actor}%'
                """
        # Получили список всех фильмов с нужными актёрами
        sql_result = cursor.execute(query).fetchall()

        # Собираем в список всех актёров из результата
        list_of_actors = []
        for element in sql_result:
            list_of_actors += list(element)

        # Разделяем строки и добавляем в список актёров по отдельности
        second_list_of_actors = []
        for actor in list_of_actors:
            second_list_of_actors += actor.split(", ")

        # Считаем количество повторяющихся имён
        counter_actors = Counter(second_list_of_actors).most_common(100)

        # Создаём список из актёров, которые учавствовали больше чем в двух фильмах
        actors = []
        for actor in counter_actors:
            if actor[1] > 2:
                actors.append(actor[0])

        # Убираем из списка первого актёра, котого задавали в зарросе
        necessary_actors = []
        for actor in actors:
            if first_actor not in actor:
                necessary_actors.append(actor)

        # Убираем из списка второго актёра, которого задавали в запросе
        actors = []
        for actor in necessary_actors:
            if second_actor not in actor:
                actors.append(actor)

        return actors


def get_description(type_of_film, release_year, listed_in):
    """
    Функция, с помощью которой можно будет передавать тип картины (фильм или сериал),
    год выпуска и ее жанр и получать на выходе список названий картин с их описаниями в JSON
    """
    with sqlite3.connect('data/netflix.db') as con:
        cursor = con.cursor()
        query = f"""
                SELECT title, description FROM netflix
                WHERE "type" LIKE '{type_of_film}' 
                AND release_year LIKE {release_year}
                AND listed_in LIKE '%{listed_in}%'
                """
        # Получили список всех фильмов с нужными параметрами
        sql_result = cursor.execute(query).fetchall()

        #Создаём словарь с названием фильма и его описанием
        list_movie = {}
        for element in sql_result:
            list_movie.update({element[0]: element[1]})

        #Запаковываем словарь в JSON
        json_list_movie = json.dumps(list_movie)

    return json_list_movie
