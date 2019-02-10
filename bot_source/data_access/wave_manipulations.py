from data_access.base_db_operations import get_connection
from models.wave import WaveFactory
from consts.wave_states import WaveStates
import json
from consts.wave_queries import WaveQueries


def update_wave(wave):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(WaveQueries.UPDATE, (wave.start,
                       wave.registrations_start,
                       wave.execution_start,
                       wave.assuring_start,
                       wave.finish,
                       wave.users_profiles,
                       wave.wave_state,
                       wave.ID))


def insert_wave(wave):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(WaveQueries.INSERT, (wave.start,
                                            wave.registrations_start,
                                            wave.execution_start,
                                            wave.assuring_start,
                                            wave.finish,
                                            wave.users_profiles,
                                            wave.wave_state))


def get_wave_in_state(state):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(WaveQueries.SELECT_BY_STATE, (state,))
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return WaveFactory.get_wave_from_db_row(row)


def register_for_wave(insta_username, user):
    wave = get_wave_in_state(WaveStates.CREATED)
    to_work_with = json.loads(wave.users_profiles)
    if user.username in to_work_with.keys():
        return
    to_work_with[user.username] = insta_username
    wave.users_profiles = json.dumps(to_work_with)
    update_wave(wave)