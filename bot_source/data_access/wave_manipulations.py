from data_access.base_db_operations import get_connection
from models.wave import WaveFactory
from consts.wave_states import WaveStates
import json


def update_wave(wave):
    sql = '''UPDATE Waves 
            SET Start = ?,
                RegistrationStart = ?,
                ExecutionStart = ?,
                AssuringStart = ?,
                Finish = ?,
                UsersProfiles = ?,
                WaveState = ?
            WHERE ID = ?'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (wave.start,
                       wave.registrations_start,
                       wave.execution_start,
                       wave.assuring_start,
                       wave.finish,
                       wave.users_profiles,
                       wave.wave_state,
                       wave.ID))


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


def get_wave_in_state(state):
    sql = '''SELECT * FROM Waves
            WHERE WaveState = ?'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (state,))
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return WaveFactory.get_wave_from_db_row(row)


def register_for_wave(insta_username, user):
    wave = get_wave_in_state(WaveStates.CREATED)
    to_work_with = json.loads(wave.users_profiles)
    if user.username not in to_work_with.keys():
        to_work_with[user.username] = insta_username
        wave.users_profiles = json.dumps(to_work_with)
        update_wave(wave)