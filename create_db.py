import sqlite3

# Создание соединения с базой данных (если БД не существует, она будет создана)
conn = sqlite3.connect("fest_searcher.db")
cursor = conn.cursor()


def create_tables():
    # Создание таблицы Пользователи
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)
    # Создание таблицы Аккаунт пользователя пользователя
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)


    # Создание таблицы Мероприятия
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fest (
        id INTEGER PRIMARY KEY,
        name text,
        description TEXT,
        date_time TEXT NOT NULL,
        category_name TEXT NOT NULL,
        price STRING NOT NULL
        location TEXT
    )
    """)



    # Завершение создания таблиц и сохранение изменений
    conn.commit()

    # Закрытие соединения с базой данных
    conn.close()
