from functools import wraps
from services.status_handler import StatusHandler, Status


def username_needed(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        username = update.effective_user.username
        if username is None:
            StatusHandler.handle_status(bot, update, Status.UsernameIsNeeded)
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
