import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS population")

# cursor.execute("""CREATE TABLE population
#                 (city TEXT, state TEXT, population INT)
#                 """)


cursor.execute("INSERT INTO population VALUES('New York City','NY', 8400000)")

cursor.execute("INSERT INTO population VALUES('San Fransisco','CA', 8000000)")

conn.commit()

conn.close()