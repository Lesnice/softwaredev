import sqlite3

# Connect to the database (it will create School.db if it doesn't exist)
conn = sqlite3.connect('School.db')
cursor = conn.cursor()

# Create Course table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Course (
    course_code CHAR(5) PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_description TEXT,
    teacher_name TEXT NOT NULL,
    course_level INTEGER NOT NULL
);
''')

# Create Student table with a foreign key to Course table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    course_code TEXT,
    mark INTEGER,
    FOREIGN KEY (course_code) REFERENCES Course(course_code)
);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

##create course table

CREATE TABLE IF NOT EXISTS Course (
    course_code TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_description TEXT,
    teacher_name TEXT NOT NULL,
    course_level INTEGER NOT NULL
);


##create student table


CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    course_code TEXT,
    mark INTEGER,
    FOREIGN KEY (course_code) REFERENCES Course(course_code)
);


#machine learning sql
SELECT first_name, last_name
FROM Student
INNER JOIN Course ON Student.course_code = Course.course_code
WHERE Course.course_code = 'DS03';


#easiest courses 
SELECT Student.first_name, Course.course_name
FROM Student
INNER JOIN Course ON Student.course_code = Course.course_code
WHERE Student.mark >= 70;

#all taught by Julia Python
SELECT Student.mark
FROM Student
INNER JOIN Course ON Student.course_code = Course.course_code
WHERE Course.teacher_name = 'Julia Python';


