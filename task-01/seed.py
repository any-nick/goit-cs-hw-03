from faker import Faker
import psycopg2
from db_connect import DATABASE_CONFIG 

fake = Faker()

def seed_data():
    try:
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cur:
                statuses = [('new',), ('in progress',), ('completed',)]
                cur.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", statuses)

                users = [(fake.name(), fake.email()) for _ in range(10)]
                cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", users)

                cur.execute("SELECT id FROM users;")
                user_ids = [row[0] for row in cur.fetchall()]

                cur.execute("SELECT id FROM status;")
                status_ids = [row[0] for row in cur.fetchall()]

                tasks = [
                    (
                        fake.sentence(nb_words=3),
                        fake.text(max_nb_chars=200),
                        fake.random.choice(status_ids),
                        fake.random.choice(user_ids)
                    )
                    for _ in range(20)
                ]
                cur.executemany(
                    "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                    tasks
                )

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    seed_data()