import sqlite3

conn = sqlite3.connect("students.sqlite")
cursor = conn.cursor()

sql_query = """ CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    gender TEXT NOT NULL,
    age TEXT
)"""

cursor.execute(sql_query)
conn.commit()
conn.close()
