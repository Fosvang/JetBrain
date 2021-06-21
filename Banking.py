import sys
import random
import sqlite3
from sqlite3 import Error
import functools


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e, "can not connect")

    return conn

if __name__ == '__main__':

    create_connection = (r"C:\sqlite\db\card.db")


def c_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, sql):

    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()
        conn.close()
    except Error as e:
        print(e)


def main():

    database = (r"C:\sqlite\db\card.db")



    sql = '''CREATE TABLE IF NOT EXISTS cards (
                                            id integer PRIMARY KEY,
                                            number text,
                                            pin text,
                                            balance integer default 0
                                        )'''
    # create a database connection
    conn = c_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
