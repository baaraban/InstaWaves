import datetime
from consts.wave_states import WaveStates


class Wave:
    def __init__(self,
                 ID,
                 start,
                 registrations_start,
                 execution_start,
                 assuring_start,
                 finish,
                 users_profiles,
                 posts,
                 wave_state):
        self.ID = ID
        self.start = start
        self.registrations_start = registrations_start
        self.execution_start = execution_start
        self.assuring_start = assuring_start
        self.finish = finish
        self.users_profiles = users_profiles
        self.posts = posts
        self.wave_state = wave_state


class WaveFactory:
    @staticmethod
    def get_new_wave():
        return Wave(
            None,
            datetime.datetime.utcnow(),
            None,
            None,
            None,
            None,
            '{}',
            '{}',
            WaveStates.CREATED
        )

    @staticmethod
    def get_wave_from_db_row(db_row):
        return Wave(
            db_row[0],
            db_row[1],
            db_row[2],
            db_row[3],
            db_row[4],
            db_row[5],
            db_row[6],
            db_row[7],
            db_row[8]
        )