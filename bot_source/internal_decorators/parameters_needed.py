from functools import wraps
from services.status_handler import StatusHandler
from consts.statuses import Status


def parameters_needed(count):
    def decorator(func):
        @wraps(func)
        def wrapped(bot, update, *args, **kwargs):
            splitted_text = update.message.text.split()
            if len(splitted_text) != count + 1:
                StatusHandler.handle_status(bot,
                                            update,
                                            Status.NotCorrectParametersPassed
                                            )
                return
            return func(bot, update, *args, **kwargs)
        return wrapped
    return decorator
