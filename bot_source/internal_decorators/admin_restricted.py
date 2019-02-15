from functools import wraps
from services.status_handler import StatusHandler, Status

LIST_OF_ADMINS = [234862974]


def admin_restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            StatusHandler.handle_status(bot, update, Status.Unauthorized)
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
