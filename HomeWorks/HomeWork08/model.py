import sqlite3
from sqlite3 import Error


def connection():
    try:
        con = sqlite3.connect('main.db')
        return con
    except Error:
        print(Error)


def close_db(cur):

    cur.close()


def select_all_table(table):

    con = connection()
    cursor = con.cursor()

    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()

    close_db(cursor)

    return data


def select_table_where_timetable(pr):

    con = connection()
    cursor = con.cursor()

    cursor.execute(f"SELECT * FROM timetables WHERE class_number IN{pr}")

    data = cursor.fetchall()

    close_db(cursor)

    return data


def select_table_where_teacher(id):

    con = connection()
    cursor = con.cursor()

    cursor.execute(f"SELECT * FROM teachers WHERE id IN({id})")

    data = cursor.fetchall()

    close_db(cursor)

    return data


def insert_in_table(data):

    con = connection()
    cursor = con.cursor()

    cursor.execute(data)

    con.commit()
    close_db(cursor)


def add_in_teacher(data):
    ins = f'INSERT INTO teachers (fullname, phone, address, classroom_teacher, mainsubject) VALUES{data}'
    insert_in_table(ins)


def add_in_timetables(data=[]):
    if data:
        ins = f'INSERT INTO timetables (class_number, number_lesson, time, weekday, classroom, teacher, subject) VALUES{data}'
        insert_in_table(ins)
    else:
        return ('class_number, number_lesson, time, weekday, classroom, teacher, subject')


def add_in_contacts(data=[]):
    if data:
        ins = f'INSERT INTO contacts (fullname, phone, jobtitle, address, student_parent, class_student, gender) VALUES{data}'
        insert_in_table(ins)
    else:
        return ('fullname, phone, jobtitle, address, student_parent, class_student, gender')

