import psycopg2
from db_connect import DATABASE_CONFIG 

def execute_query(query, params=None):
    try:
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchall() if cur.description else None
                conn.commit()
                return result
    except Exception as error:
        print(f"Error: {error}")
        return None
    
if __name__ == "__main__":

    # 1. Отримати всі завдання певного користувача
    print(f"Отримати всі завдання певного користувача :\n {execute_query("SELECT * FROM tasks WHERE user_id = 1;")}\n\n")

    # 2. Вибрати завдання за певним статусом
    print(f"Вибрати завдання за певним статусом:\n {execute_query("SELECT * FROM tasks WHERE status_id = 1;")} \n\n")

    # 3. Оновити статус конкретного завдання
    print(f"Old: {execute_query("SELECT * FROM tasks WHERE id = 1;")} \n")
    print(f"Оновити статус конкретного завдання:\n {execute_query("UPDATE tasks SET status_id = 2 WHERE id = 1;")} \n")
    print(f"Changed: {execute_query("SELECT * FROM tasks WHERE id = 1;")} \n")

    # 4. Отримати список користувачів, які не мають жодного завдання
    print(f"Отримати список користувачів, які не мають жодного завдання:\n {execute_query("SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)")} \n\n")

    # 5. Додати нове завдання для конкретного користувача
    print(f"Додати нове завдання для конкретного користувача:\n {execute_query("""
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES ('New Task', 'Description of the task', 1, 1);
    """)} \n")
    print(f"Added task: {execute_query("SELECT * FROM tasks WHERE title = 'New Task';")} \n\n")

    # 6. Отримати всі завдання, які ще не завершено
    print(f"Отримати всі завдання, які ще не завершено:\n {execute_query("SELECT * FROM tasks WHERE status_id != 3")} \n\n")
    
    # 7. Видалити конкретне завдання
    print(f"Видалити конкретне завдання:\n {execute_query("DELETE FROM tasks WHERE id = 5")} \n\n")
    
    # 8. Знайти користувачів з певною електронною поштою
    print(f"Знайти користувачів з певною електронною поштою:\n {execute_query("SELECT * FROM users WHERE email LIKE '%@example.org'")} \n\n")
    
    # 9. Оновити ім'я користувача
    print(f"Оновити ім'я користувача:\n {execute_query("UPDATE users SET fullname = 'Dogy Duke'  WHERE id = 2")} \n\n")
    
    # 10. Отримати кількість завдань для кожного статусу
    print(f"Отримати кількість завдань для кожного статусу:\n {execute_query("""
    SELECT s.name AS status, COUNT(t.id) AS task_count
    FROM status s
    LEFT JOIN tasks t ON s.id = t.status_id
    GROUP BY s.name
""")} \n\n")
    
    # 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
    print(f"Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:\n {execute_query("""
        SELECT t.id, t.title, t.description, u.fullname, u.email
        FROM tasks t
        INNER JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE '%example.com'
    """)} \n\n")

    # 12. Отримати список завдань, що не мають опису
    print(f"Отримати список завдань, що не мають опису:\n {execute_query("SELECT id, title, status_id, user_id FROM tasks WHERE description IS NULL OR description = ''")} \n\n")
    
    # 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
    print(f"Вибрати користувачів та їхні завдання, які є у статусі 'in progress':\n {execute_query("""
        SELECT u.id AS user_id, u.fullname, t.id AS task_id, t.title
        FROM users u
        INNER JOIN tasks t ON u.id = t.user_id
        INNER JOIN status s ON t.status_id = s.id
        WHERE s.name = 'in progress'
    """)} \n\n")

    # 12. Отримати користувачів та кількість їхніх завдань
    print(f"Отримати користувачів та кількість їхніх завдань:\n {execute_query("""
        SELECT u.id AS user_id, u.fullname, COUNT(t.id) AS task_count
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id, u.fullname
    """)} \n\n")
    

    



