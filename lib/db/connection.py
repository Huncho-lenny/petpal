import sqlite3

connection = sqlite3.connect('petpal.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS owners;")
cursor.execute("DROP TABLE IF EXISTS pets;")

cursor.execute("""
CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pet_type TEXT NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY(owner_id) REFERENCES owners(id)
);
""")

connection.commit()
connection.close()
