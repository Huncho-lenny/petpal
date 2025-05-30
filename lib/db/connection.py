import sqlite3

CONN = sqlite3.connect('lib/db/petpal.db')
CURSOR = CONN.cursor()

CURSOR.execute("PRAGMA foreign_keys = ON;")


CURSOR.execute("DROP TABLE IF EXISTS owners;")
CURSOR.execute("DROP TABLE IF EXISTS pets;")

CURSOR.execute("""
CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

CURSOR.execute("""
CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pet_type TEXT NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY(owner_id) REFERENCES owners(id)
);
""")

CONN.commit()
CONN.close()
