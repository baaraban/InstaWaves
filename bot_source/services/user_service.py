import data_access.users_manipulations as u_man
from consts.statuses import Status
from consts.application_level_consts import *


class UserService:
    @staticmethod
    def warn_user(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.warnings += 1
        if user.warnings >= WARNINGS_LIMIT:
            user.is_banned = True
            u_man.update_user(user)
            return Status.UserIsBanned
        u_man.update_user(user)
        return Status.UserIsWarned

    @staticmethod
    def remove_warn_from_user(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.warnings -= 1
        u_man.update_user(user)
        return Status.WarnIsRemovedFromUser

    @staticmethod
    def give_user_privilege(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.is_privileged = True
        u_man.update_user(user)
        return Status.UserIsPrivileged

    @staticmethod
    def take_privilege_from_user(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.is_privileged = False
        u_man.update_user(user)
        return Status.UserIsUnprivileged

    @staticmethod
    def ban_user(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.is_banned = True
        u_man.update_user(user)
        return Status.UserIsBanned

    @staticmethod
    def unban_user(username):
        if not u_man.user_exists_with_username(username):
            return Status.UserDoesNotExist
        user = u_man.get_by_username(username)
        user.is_banned = False
        u_man.update_user(user)
        return Status.UserIsUnbanned
