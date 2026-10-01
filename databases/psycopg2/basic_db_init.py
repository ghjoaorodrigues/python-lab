import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    host="localhost",
    port=5433
)

conn.autocommit = True

cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE psycopg2")
    print("Database created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists, skipping...")

cur.close()
conn.close()