import psycopg2
from psycopg2 import sql
from db_connect import DATABASE_CONFIG 

def create_table(conn, sql_query):
    try:
        with conn.cursor() as c:
            c.execute(sql_query)
            conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    # SQL-запити для створення таблиць
    sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
    """
    sql_create_status_table = """
        CREATE TABLE IF NOT EXISTS status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
    """
    sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        );
    """

    try:
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_status_table)
            create_table(conn, sql_create_tasks_table)
    except Exception as e:
        print(f"Error connecting to the database: {e}")