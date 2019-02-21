from internal_decorators.admin_restricted import admin_restricted
from internal_decorators.wave_status_filter import wave_status_filter
from internal_decorators.parameters_needed import parameters_needed
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
    try:
        state, summary = WaveService.finish_wave()
        StatusHandler.handle_status(bot, update, state, summary=summary)
    except:
        StatusHandler.handle_status(bot, update, WaveService.rollback_from_assuring_to_bidding())

@admin_restricted
@parameters_needed(1)
def give_privilege_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.give_user_privilege(username), username=username)


@admin_restricted
@parameters_needed(1)
def ban_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.ban_user(username), username=username)


@admin_restricted
@parameters_needed(1)
def unban_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.unban_user(username), username=username)


@admin_restricted
@parameters_needed(1)
def warn_user_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.warn_user(username), username=username)


@admin_restricted
@parameters_needed(1)
def remove_warn_handler(bot, update):
    username = update.message.text.split()[1]
    StatusHandler.handle_status(bot, update, UserService.remove_warn_from_user(username), username=username)


