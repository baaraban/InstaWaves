import sqlite3
import os


DEFINITIONS_FOLDER = 'data_access/sql_definitions/'
DB_NAME = 'bot_db.sqlite'


def get_connection():
    return sqlite3.connect(DB_NAME)


def setup_db():
    connection = get_connection()
    for filename in os.listdir(DEFINITIONS_FOLDER):
        with open(os.path.join(DEFINITIONS_FOLDER, filename), 'r') as definition:
            stmt = definition.read()
            connection.execute(stmt)
            connection.commit()
    connection.close()