import datetime


class Wave:
    def __init__(self, start, finish, profiles, users):
        self.start = start
        self.finish = finish
        self.profiles = profiles
        self.users = users


class WaveFactory:
    @staticmethod
    def get_new_wave():
        return Wave(
            datetime.datetime.utcnow(),
            None,
            None,
            None
        )
