from data_access.base_db_operations import get_connection


def insert_wave(wave):
    sql = '''INSERT INTO Waves(Start, RegistrationStart, ExecutionStart, AssuringStart, Finish, UsersProfiles, WaveState) 
            VALUES(?, ?, ?, ?, ?, ?, ?)'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (wave.start,
                             wave.registrations_start,
                             wave.execution_start,
                             wave.assuring_start,
                             wave.finish,
                             wave.users_profiles,
                             wave.wave_state))


def register_for_wave(username, user):
    return