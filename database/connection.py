import psycopg2

import os


def connect():

    conn = psycopg2.connect(
        database='mydiary',
        user='soko',
        password='sokool',
        host='localhost',
        port='5432')
    return conn
