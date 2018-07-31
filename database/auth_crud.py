import psycopg2
from database.connection import connect
from database.create_tables import create_tables
import psycopg2.extras as extra


class auth_crud():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

        # create_tables().users_table()

    # creates table for entries

    def add_user(self, user):
        try:
            if self.get_user_by_phone(user.phone_number) == 'failed':
                cur = self.conn.cursor()
                db_query = """INSERT INTO Users (user_id,name,phone_number, password)
                            VALUES (DEFAULT,%s,%s,%s) RETURNING user_id, name, phone_number, password """
                cur.execute(db_query, (user.name, user.phone_number,
                                       user.password))

                print("created")
                rows = cur.fetchone()
                return rows
            else:
                return 'user exists'

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'failed'

    def get_user_by_id(self, id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Users WHERE user_id = %s""", [id])
                rows = cur.fetchall()
                return rows[0]
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't fetch  test database!")
                return "failed"
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to fetch to the database")
            return "failed"

    def get_user_by_phone(self, phone_number):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Users WHERE phone_number = %s  """, [phone_number])
                rows = cur.fetchall()
                return rows[0]
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't fetch  test database!")
                return "failed"
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to fetch to the database")
            return "failed"
