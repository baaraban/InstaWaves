import datetime


class Wave:
    def __init__(self,
                 ID,
                 start,
                 registrations_start,
                 execution_start,
                 assuring_start,
                 finish,
                 users_profiles,
                 wave_state):
        self.ID = ID
        self.start = start
        self.registrations_start = registrations_start
        self.execution_start = execution_start
        self.assuring_start = assuring_start
        self.finish = finish
        self.users_profiles = users_profiles
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
            None,
            "Created"
        )
