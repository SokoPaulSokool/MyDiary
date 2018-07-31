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
            cur = self.conn.cursor()
            db_query = """INSERT INTO Users (user_id,name,phone_number, password)
                         VALUES (DEFAULT,%s,%s,%s) """
            cur.execute(db_query, (user.name, user.phone_number,
                                   user.password))

            print("created")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def get_all(self):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute("""SELECT * from Users""")
                rows = cur.fetchall()
                return rows
            except:
                print("I can't fetch  test database!")
        except:
            print("I am unable to fetch to the database")

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

    def get_user_by_phone_and_password(self, phone_number, password):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Users WHERE phone_number = %s AND password=%s """, [phone_number, password])
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

    def delete_user(self, id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """DELETE FROM Users WHERE user_id = %s""", [id])

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't delete  test database!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to delete to the database")

    def edit_user(self, user, id):
        try:
            cur = self.conn.cursor()

            db_query = """UPDATE Users SET 
            name = %s, phone_number = %s,  password = %s WHERE user_id = %s """
            cur.execute(db_query, (user.name, user.phone_number,
                                   user.password, id))

            print("created")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I can't fetch  edit database!")
