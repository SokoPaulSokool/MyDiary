import psycopg2

import os


def connect():

    conn = psycopg2.connect(
        database='mydiary',
        user='postgres',
        password='spolspol',
        host='localhost',
        port='5432')

    return conn
