import json
import data_access.users_manipulations as u_man
import data_access.wave_manipulations as w_man


class UserService:
    @staticmethod
    def register_for_wave(user, insta_username):
        if u_man.user_exists_with_username(user.user_id):
            user = u_man.get_by_user_id(user.user_id)
        else:
            u_man.insert_user(user)
        if user.is_banned:
            return
        w_man.register_for_wave(insta_username, user)
        profiles = json.loads(user.profiles)
        if insta_username not in profiles.keys():
            profiles[insta_username] = insta_username
        user.profiles = json.dumps(profiles)
        u_man.update_user(user)

    @staticmethod
    def warn_user(username):
        if not u_man.user_exists_with_username(username):
            return
        user = u_man.get_by_username(username)
        user.warnings += 1
        u_man.update_user(user)

    @staticmethod
    def ban_user(username):
        if not u_man.user_exists_with_username(username):
            return
        user = u_man.get_by_username(username)
        if user.is_banned:
            return
        user.is_banned = True
        u_man.update_user(user)

    @staticmethod
    def unban_user(username):
        if not u_man.user_exists_with_username(username):
            return
        user = u_man.get_by_username(username)
        if not user.is_banned:
            return
        user.is_banned = False
        u_man.update_user(user)