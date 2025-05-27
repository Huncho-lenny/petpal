import sqlite3

CONN = sqlite3.connect('petpal.db')
CURSOR = CONN.cursor()
