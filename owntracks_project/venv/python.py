import sqlite3
conn = sqlite3.connect('database.db')
print("Database created successfully!")
conn.close()
