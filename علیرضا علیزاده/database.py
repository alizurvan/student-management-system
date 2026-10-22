import sqlite3

con = sqlite3.connect('students.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS students
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        family TEXT NOT NULL,
        course TEXT,
        password TEXT NOT NULL
    )
''')
con.commit()


def insert_record(name, family, course, password):
    cur.execute(
        '''INSERT INTO students (name, family, course, password)
           VALUES (?, ?, ?, ?)''',
        (name, family, course, password)
    )
    con.commit()


def show_all():
    cur.execute('SELECT * FROM students')
    return cur.fetchall()


def delete_student(student_id):
    cur.execute('DELETE FROM students WHERE id = ?', (student_id,))
    con.commit()


def login(password):
    cur.execute('SELECT * FROM students WHERE password = ?', (password,))
    return cur.fetchone()


def get_student(student_id):
    cur.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    return cur.fetchone()


def close_db():
    con.close()
