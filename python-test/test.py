import sqlite3

connection = sqlite3.connect("test_data.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.executescript("""
        DROP TABLE IF EXISTS People;
        CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
        INSERT INTO People VALUES('Ron', 'Obvious', '42');
""")


connection.commit()