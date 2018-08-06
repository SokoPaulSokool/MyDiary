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

    def add_user(self, user):
        try:
            if self.get_user_by_email(user.email) == 'failed':
                cur = self.conn.cursor()
                db_query = """INSERT INTO Users (user_id,name,email, password)
                            VALUES (DEFAULT,%s,%s,%s) RETURNING user_id, name, email, password """
                cur.execute(db_query, (user.name, user.email,
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
        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Users WHERE user_id = %s""", [id])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def get_user_by_email(self, email):
        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Users WHERE email = %s  """,
                [email])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"
