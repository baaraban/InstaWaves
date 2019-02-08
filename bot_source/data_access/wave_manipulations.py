from data_access.base_db_operations import get_connection


def insert_wave(wave):
    sql = '''INSERT INTO Waves(Start, Finish, Profiles, Users) 
            VALUES(?,?,?,?)'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (wave.start,
                             wave.finish,
                             wave.profiles,
                             wave.users))


def register_for_wave(username, user):
    return