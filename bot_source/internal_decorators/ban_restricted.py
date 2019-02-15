from functools import wraps
from services.status_handler import StatusHandler, Status
from data_access.users_manipulations import is_user_banned


def ban_restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if is_user_banned(user_id):
            StatusHandler.handle_status(bot, update, Status.Banned)
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
