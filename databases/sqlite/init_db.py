import sqlite3
import os

if os.path.exists("data.db"):
    os.remove("data.db")

conn = sqlite3.connect(database="data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE students(" \
                "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                "name TEXT," \
                "grade INTEGER" \
                ")")

cur.execute("INSERT INTO students (name, grade) VALUES ('Alice', 10)")
cur.execute("INSERT INTO students (name, grade) VALUES ('Bia', 9)")
cur.execute("INSERT INTO students (name, grade) VALUES ('Clara', 8)")

cur.execute("SELECT * FROM students")
out = cur.fetchall()

for id, name, grade in out:
    print(f"{id:<2} | {name:<8} | {grade}")

cur.close()

conn.commit()
conn.close()
