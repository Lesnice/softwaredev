import sqlite3

db = sqlite3.connect('data/student_db.db')


cursor = db.cursor()

cursor.execute('''
        CREATE TABLE student (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
        
''')

db.commit()