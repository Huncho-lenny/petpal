import sqlite3
import os

def setup_database():
    # Create database in the current directory
    db_path = os.path.join(os.path.dirname(__file__), 'petpal.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create owners table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    
    # Create pets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id)
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database setup complete")

if __name__ == "__main__":
    setup_database()