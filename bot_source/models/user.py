class User:
    def __init__(self,
                 ID,
                 user_id,
                 username,
                 first_name,
                 profiles,
                 is_banned,
                 warnings,
                 is_privileged):
        self.ID = ID
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.profiles = profiles
        self.is_banned = is_banned
        self.warnings = warnings
        self.is_privileged = is_privileged


class UserFactory:
    @staticmethod
    def get_user_from_update(update):
        return User(
            None,
            update.effective_user.id,
            update.effective_user.username,
            update.effective_user.first_name,
            '{}',
            False,
            0,
            False
        )

    @staticmethod
    def get_user_from_db_row(db_row):
        return User(
            db_row[0],
            db_row[1],
            db_row[2],
            db_row[3],
            db_row[4],
            db_row[5],
            db_row[6],
            db_row[7]
        )
