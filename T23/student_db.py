import sqlite3

#creates and opens a file called student_db with sqlite3

db= sqlite3.connect('data/student_db.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, name TEXT, 
                        grade INTEGER)
    ''')
db.commit

name1 = 'Andres'
grade1 = 60

name2 = 'John'
grade2 = 90

cursor. execute(''' INSERT INTO student(name, grade)
                    VALUES(?, ?)''', (name1,grade1))

print('First user inserted')

cursor. execute(''' INSERT INTO student(name, grade)
                    VALUES(?, ?)''', (name2,grade2))

print('second user inserted')

db.commit


name3 ='Sheila'
grade3 = 40

cursor. execute(''' INSERT INTO student(name, grade)
                    VALUES(:name, :grade)''', {'name':name3, 'grade': grade3})

print('Third user inserted')


cursor.execute('''UPDATE student SET grade = ? WHERE id = ? ''', (65, 2))

db.rollback()