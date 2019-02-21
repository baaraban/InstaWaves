from data_access.base_db_operations import get_connection
from models.user import UserFactory
from consts.user_queries import UserQueries


def insert_user(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.INSERT, (user.user_id,
                                            user.username,
                                            user.first_name,
                                            user.profiles,
                                            user.is_banned,
                                            user.warnings,
                                            user.is_privileged))


def update_user(user):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.UPDATE, (user.user_id,
                                            user.username,
                                            user.first_name,
                                            user.profiles,
                                            user.is_banned,
                                            user.warnings,
                                            user.is_privileged,
                                            user.ID))


def is_user_banned(user_id):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.CHECK_USER_BANNED, (user_id, ))
        data = cursor.fetchone()
        return data is not None


def user_exists_with_user_id(user_id):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_BY_USER_ID, (user_id, ))
        data = cursor.fetchall()
        return len(data) != 0


def user_exists_with_username(username):
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
        if data is None:
            return None
        else:
            return UserFactory.get_user_from_db_row(data)


def get_all_privileged_users():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_PRIVILEGED)
        data = cursor.fetchall()
        return UserFactory.get_users_from_db_rows(data)


def get_by_user_id(user_id):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(UserQueries.SELECT_BY_USER_ID, (user_id, ))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return UserFactory.get_user_from_db_row(data)


