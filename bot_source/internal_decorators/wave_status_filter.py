from functools import wraps
from services.status_handler import StatusHandler
from consts.statuses import Status
import data_access.wave_manipulations as w_man


def wave_status_filter(wave_state):
    def decorator(func):
        @wraps(func)
        def wrapped(bot, update, *args, **kwargs):
            if w_man.get_wave_in_state(wave_state):
                StatusHandler.handle_status(bot,
                                            update,
                                            Status.WaveStateAlreadyPresent,
                                            state=wave_state)
                return
            return func(bot, update, *args, **kwargs)
        return wrapped
    return decorator
