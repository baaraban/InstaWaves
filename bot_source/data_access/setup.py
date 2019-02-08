import sqlite3
import os


DEFINITIONS_FOLDER = 'data_access/sql_definitions/'
DB_NAME = 'bot_db.sqlite'


def setup_db():
    connection = sqlite3.connect(DB_NAME)
    for filename in os.listdir(DEFINITIONS_FOLDER):
        with open(os.path.join(DEFINITIONS_FOLDER, filename), 'r') as definition:
            stmt = definition.read()
            connection.execute(stmt)
            connection.commit()
    connection.close()