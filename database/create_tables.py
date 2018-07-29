import psycopg2
from database.connection import connect
import psycopg2.extras as extra
import os


class create_tables():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    # creates table for entries

    def entries_table(self):
        try:
            self.conn
            try:
                # entry_id, entry_title, entry, entry_date
                # self.cursor.execute('DROP  TABLE Entries ;')
                create_table_query = (
                    """CREATE TABLE IF NOT EXISTS Entries (entry_id SERIAL PRIMARY KEY,entry_title VARCHAR(255) NOT NULL, entry VARCHAR(255) NOT NULL, entry_date VARCHAR(255) NOT NULL)""")
                self.cursor.execute(create_table_query)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't  create entries!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to create entries")

        print("entries table creation")

    # create table for users

    def users_table(self):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "CREATE TABLE Userd(Id INTEGER PRIMARY KEY, username VARCHAR(20), phonenumber VARCHAR(20), password VARCHAR(20));")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('create table for users')
