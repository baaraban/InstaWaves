from data_access.base_db_operations import get_connection
from models.user import UserFactory
from consts.user_queries import UserQueries


def insert_user(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.INSERT, (user.chat_id,
                                            user.username,
                                            user.first_name,
                                            user.profiles,
                                            user.is_banned,
                                            user.warnings,
                                            user.is_privileged))


def update_user(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.UPDATE, (user.chat_id,
                                            user.username,
                                            user.first_name,
                                            user.profiles,
                                            user.is_banned,
                                            user.warnings,
                                            user.is_privileged,
                                            user.ID))


def is_banned(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.CHECK_USER_BANNED, (user.username, ))
        data = cursor.fetchone()
        return data is not None


def user_exists(username):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_BY_USERNAME, (username, ))
        data = cursor.fetchall()
        return len(data) != 0


def get_by_username(username):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_BY_USERNAME, (username, ))
        data = cursor.fetchone()
        return UserFactory.get_user_from_db_row(data)


def fullfill_model(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_BY_USERNAME, (user.username, ))
        data = cursor.fetchone()
        if data is None:
            insert_user(user)
            return user
        else:
            return UserFactory.get_user_from_db_row(data)


