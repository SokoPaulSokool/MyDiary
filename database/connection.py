import psycopg2

import os

DATABASE_URL = 'postgres://rtoomoesiqakui:3f567be47163a5ccc4b1ce14ce4a131a2e23a44d7c3dd43ddcf0d6de950bbfab@ec2-54-204-23-228.compute-1.amazonaws.com:5432/d62ahk5c6fpk6m'


def connect():
    # conn = psycopg2.connect(
    #     user='rtoomoesiqakui',
    #     password='3f567be47163a5ccc4b1ce14ce4a131a2e23a44d7c3dd43ddcf0d6de950bbfab',
    #     host='ec2-54-204-23-228.compute-1.amazonaws.com',
    #     port='5432', sslmode='require')
    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='spolspol',
        host='localhost',
        port='5434')
    return conn
