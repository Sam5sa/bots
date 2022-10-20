import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

'''     ввод логина и поаролся(зашифрованно)
try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
'''

'''     авторегистрация + вывод листа БД
try:
    with connect(
        host="localhost",
        user="root",
        password="",
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)
'''

'''     показать структуру таблицы
try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="sql_test",
    ) as connection:
        show_table_query = "DESCRIBE main"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
'''

'''     показать элементы из БД
try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="sql_test",
    ) as connection:
        select_movies_query = "SELECT * FROM main"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
'''


'''     добавление в БД списка строк
try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="sql_test",
    ) as connection:
        insert_reviewers_query = """
        INSERT INTO main
        (name, price)
        VALUES ( %s, %s )
        """
        reviewers_records = [
            ("кондёр3", "3000"),
            ("кондёр4", "4000"),
            ("кондёр5", "5000"),
        ]
        with connection.cursor() as cursor:
            cursor.executemany(insert_reviewers_query, reviewers_records)
            connection.commit()
except Error as e:
    print(e)        
'''