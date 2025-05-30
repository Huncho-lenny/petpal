import sqlite3

CONN = sqlite3.connect('db/petpal.db')
CURSOR = CONN.cursor()
