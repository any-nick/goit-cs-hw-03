from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Підключення до бази даних
uri = "mongodb+srv://andriivynar:QwriPQDd13jZVUlo@cluster0.kabwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))


db = client["cat_database"]
collection = db["cats"]

# Додавання документів
def create_cat(name, age, features):
    try:
        document = {"name": name, "age": age, "features": features}
        result = collection.insert_one(document)
        print(f"Кіт успішно доданий з ID: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при створенні документа: {e}")

# Виведення всіх записів
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні документів: {e}")

# Пошук кота за іменем
def find_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кота з таким іменем не знайдено.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")

# Оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print("Вік кота успішно оновлено.")
        else:
            print("Кота з таким іменем не знайдено.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")

# Додавання характеристики до кота
def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.matched_count > 0:
            print("Характеристика успішно додана.")
        else:
            print("Кота з таким іменем не знайдено.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

# Видалення кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Кота успішно видалено.")
        else:
            print("Кота з таким іменем не знайдено.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")

# Видалення всіх записів
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Успішно видалено {result.deleted_count} записів.")
    except Exception as e:
        print(f"Помилка при видаленні всіх записів: {e}")

def main():
# Додавання котів
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("tom", 3, ["дає себе гладити", "чорний"])
    create_cat("murzik", 5, ["любит ковбаску", "білий", "любить спати"])
    create_cat("lapka", 5, ["сірий", "п'є багато води"])

    # Виведення всіх котів
    print("\n Перелік всіх коти:")
    read_all_cats()

    # Пошук кота за ім'ям
    print("\n Пошук кота 'tom':")
    find_cat_by_name("tom")

    # Нeвдалий пошук кота за ім'ям
    print("\n Пошук кота 'shelly':")
    find_cat_by_name("shelly")

    # Оновлення віку
    print("\n Оновлення віку кота 'barsik':")
    update_cat_age("barsik", 4)
    find_cat_by_name("barsik")

    # Додавання характеристики
    print("\n Додавання характеристики до 'barsik':")
    add_feature_to_cat("barsik", "ловить мишей")
    find_cat_by_name("barsik")

    # Видалення кота
    print("\n Видалення кота 'tom':")
    delete_cat_by_name("tom")
    read_all_cats()

    # Видалення всіх котів
    print("\n Видалення всіх котів:")
    delete_all_cats()
    read_all_cats()



if __name__ == "__main__":
    main()