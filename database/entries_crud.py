import psycopg2
from database.connection import connect
from database.create_tables import create_tables
import psycopg2.extras as extra


class entries_crud():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

        # create_tables().users_table()

    # creates table for entries

    def add_entry(self, enty):
        try:
            cur = self.conn.cursor()
            db_query = """INSERT INTO Entries (entry_id,entry_title,entry, entry_date) VALUES (%s,%s,%s,%s) """
            cur.execute(db_query, (enty.entry_id, enty.entry_title, enty.entry,
                                   enty.entry_date))

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
                cur.execute("""SELECT * from Entries""")
                rows = cur.fetchall()
                return rows
            except:
                print("I can't fetch  test database!")
        except:
            print("I am unable to fetch to the database")

    def get_entry_by_id(self, id):
        try:
            cur = self.conn.cursor()
            try:
                cur.execute(
                    """SELECT * from Entries WHERE entry_id = %s""", [id])
                rows = cur.fetchall()
                return rows[0]
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("I can't fetch  test database!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("I am unable to fetch to the database")
