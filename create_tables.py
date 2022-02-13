import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS emails1
               (ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(99), emails varchar(222));''')
con.commit()

con.close()