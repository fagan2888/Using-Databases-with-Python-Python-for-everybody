
import sqlite3

#To use the module, you must first create a Connection object that represents the database. The reason this is called a "connection" is that sometimes the database is stored on a separate "database server" from the server on which we are running our application
conn = sqlite3.connect('music.sqlite')
# Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands
cur = conn.cursor()

#  the SQL keywords in uppercase and the parts of the command that we are adding (such as the table and column names) will be shown in lowercase.
# The first SQL command removes the Tracks table from the database if it exists.no undo. every thing gets deleted
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
#commit the changes
conn.commit()

#? is a placeholder much like %s or %d in C

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
     print(row)

cur.execute('DELETE FROM Tracks WHERE plays > 100')
conn.commit()


conn.close()