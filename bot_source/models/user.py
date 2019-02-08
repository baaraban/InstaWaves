class User:
    def __init__(self, name, chat_id, username, profiles, is_banned, warnings, is_privileged):
        self.name = name
        self.chat_id = chat_id
        self.username = username
        self.profiles = profiles
        self.is_banned = is_banned
        self.warnings = warnings
        self.is_privileged = is_privileged


class UserFactory:
    @staticmethod
    def get_user_from_update(update):
        return User(
            update.message.chat.first_name,
            update.message.chat.id,
            update.message.chat.username,
            '',
            False,
            0,
            False
        )

    @staticmethod
    def get_user_from_db_row(db_row):
        return User(
            'whatever',
            db_row[1],
            db_row[2],
            db_row[3],
            db_row[4],
            db_row[5],
            db_row[6]
        )
