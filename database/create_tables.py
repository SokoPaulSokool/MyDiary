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
                    """CREATE TABLE IF NOT EXISTS Entries (
                        entry_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        entry_title VARCHAR(255) NOT NULL,
                        entry VARCHAR(255) NOT NULL, 
                        entry_date VARCHAR(255) NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES Users (user_id) ON DELETE CASCADE
                        )
                        """)
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
                """CREATE TABLE Users(
                user_id SERIAL PRIMARY KEY, 
                name VARCHAR(20),
                phone_number VARCHAR(20),
                password VARCHAR(20)
                );
                """)
            # FOREIGN KEY (user_id) REFERENCES Entries (entry_id) ON DELETE CASCADE

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('create table for users')

    def entries_drop_table(self):
        try:
            self.conn
            try:
                self.cursor.execute('DROP TABLE Entries ;')
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't  drop entries!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to drop entries")

        print("entries table drop")

    def users_drop_table(self):
        try:
            self.conn
            try:
                self.cursor.execute('DROP  TABLE Users CASCADE;')
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't  drop users!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to drop users")

        print("entries table users")
