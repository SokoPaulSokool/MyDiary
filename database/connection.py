import psycopg2

import os


def connect():

    # conn = psycopg2.connect(
    #     database='mydiary',
    #     user='postgres',
    #     password='',
    #     host='localhost',
    #     port='5432')

    conn = psycopg2.connect(
        database='mydiary',
        user='soko',
        password='sokool',
        host='localhost',
        port='5434')

    return conn
