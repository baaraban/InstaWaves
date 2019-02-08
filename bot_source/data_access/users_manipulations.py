from data_access.base_db_operations import get_connection
from models.user import UserFactory


def insert_user(user):
    sql = '''INSERT INTO Users(ChatId, Username, Profiles, IsBanned, WarningsAmount, IsPrivileged) 
                VALUES(?, ?, ?, ?, ?, ?)'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (user.chat_id,
                             user.username,
                             user.profiles,
                             user.is_banned,
                             user.warnings,
                             user.is_privileged))


def is_banned(user):
    sql = '''SELECT ID FROM USERS WHERE 
             Username = ? AND IsBanned = "True"'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (user.username, ))
        data = cursor.fetchone()
        return data is not None


def fullfill_model(user):
    sql = '''SELECT ID, ChatId, Username, Profiles, IsBanned, WarningsAmount, IsPrivileged FROM USERS WHERE 
                 Username = ?'''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, (user.username, ))
        data = cursor.fetchone()
        if data is None:
            insert_user(user)
            return user
        else:
            return UserFactory.get_user_from_db_row(data)


