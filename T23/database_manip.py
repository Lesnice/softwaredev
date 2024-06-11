import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
db = sqlite3.connect('student_db.db')

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the python_programming table with id, name, and grade columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INT PRIMARY KEY,        -- id: integer, primary key
        name VARCHAR(50) NOT NULL, -- name: variable character with a max length of 50, cannot be null
        grade INT                  -- grade: integer
    )
''')

# Inserting sample data into the python_programming table
cursor.execute('''
    INSERT INTO python_programming (id, name, grade) VALUES
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
''')

db.commit()

# Select all records from the python_programming table where grade is between 60 and 80
cursor.execute('''
    SELECT * 
    FROM python_programming
    WHERE grade >= 60 AND grade <= 80
''')
results = cursor.fetchall()
print("Students with grades between 60 and 80:", results)

# Update Carl's grade in the python_programming table
cursor.execute('''
    UPDATE python_programming
    SET grade = 65
    WHERE name = 'Carl Davis'
''')
db.commit()

# Select Dennis' row from the python_programming table
cursor.execute('''
    SELECT * 
    FROM python_programming
    WHERE name = 'Dennis Fredrickson'
''')
dennis_row = cursor.fetchone()
print("Dennis Fredrickson's row:", dennis_row)

# Update the grade for all students with an id greater than 55
cursor.execute('''
    UPDATE python_programming
    SET grade = 80
    WHERE id > 55
''')
db.commit()

# Close the connection
db.close()
