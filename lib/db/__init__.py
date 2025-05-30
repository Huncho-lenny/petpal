import sqlite3

CONN = sqlite3.connect('lib/db/petpal.db')
CURSOR = CONN.cursor()
