from internal_decorators.admin_restricted import admin_restricted
from internal_decorators.wave_status_filter import wave_status_filter
from consts.wave_states import WaveStates
from services.wave_service import WaveService
from services.user_service import UserService
from services.status_handler import StatusHandler


@admin_restricted
@wave_status_filter(WaveStates.CREATED)
def create_wave_handler(bot, update):
    StatusHandler.handle_status(bot, update, WaveService.create_wave())


@admin_restricted
@wave_status_filter(WaveStates.BIDDING)
def start_bidding_handler(bot, update):
    status, links = WaveService.start_bidding()
    StatusHandler.handle_status(bot, update, status, links=links)


@admin_restricted
@wave_status_filter(WaveStates.ASSURING)
def assuring_step_handler(bot, update):
    StatusHandler.handle_status(bot, update, WaveService.start_assuring_step())


@admin_restricted
def ban_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.ban_user(username), username=username)


@admin_restricted
def unban_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.unban_user(username), username=username)


@admin_restricted
def warn_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.warn_user(username), username=username)


