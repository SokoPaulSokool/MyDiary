import psycopg2
from database.connection import connect
from database.create_tables import create_tables
import psycopg2.extras as extra
from database.auth_crud import auth_crud


class entries_crud():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    # create_tables().users_table()

    # creates table for entries

    def add_entry(self, user_id, enty):
        try:
            if auth_crud().get_user_by_id(user_id) != "failed":
                cur = self.conn.cursor()
                db_query = """INSERT INTO Entries (entry_id,user_id,entry_title,entry, entry_date)
                            VALUES (DEFAULT,%s,%s,%s,%s) """
                cur.execute(db_query, (user_id, enty.entry_title, enty.entry,
                                       enty.entry_date))

                print("created")
            else:
                print("user not found")

        except (Exception, psycopg2.DatabaseError) as error:

            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def get_all(self):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute("""SELECT * from Entries""")
                rows = cur.fetchall()
                return rows
            except:
                print("I can't fetch  test database!")
        except:
            print("I am unable to fetch to the database")

    def get_all_user_entries(self, user_id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Entries WHERE user_id=%s""", [user_id])
                rows = cur.fetchall()
                return rows
            except:
                print("I can't fetch  test database!")
        except:
            print("I am unable to fetch to the database")

    def get_entry_by_id(self, user_id, entry_id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Entries WHERE user_id =%s, entry_id = %s""", [user_id, entry_id])
                rows = cur.fetchall()
                return rows[0]
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't fetch  test database!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to fetch to the database")

    def delete_entry(self, user_id, entry_id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """DELETE FROM Entries WHERE user_id =%s, entry_id = %s""", [user_id, entry_id])

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't delete  test database!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to delete to the database")

    def edit_entry(self, user_id, entry_id, enty):
        try:
            cur = self.conn.cursor()

            db_query = """UPDATE Entries SET  entry_id = %s, entry_title =  %s, entry =  %s  WHERE user_id= %s, entry_id = %s """
            cur.execute(db_query, (enty.id, enty.entry_title, enty.entry, user_id,
                                   entry_id))

            print("edited")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I can't fetch  edit database!")
        finally:
            if self.conn is not None:
                self.conn.close()
                print("I am unable to edit to the database")
