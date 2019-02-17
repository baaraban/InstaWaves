from services.wave_service import WaveService
from services.status_handler import StatusHandler
from internal_decorators.ban_restricted import ban_restricted
from internal_decorators.username_needed import username_needed
from internal_decorators.parameters_needed import parameters_needed
from models.user import UserFactory
from consts.statuses import Status


@username_needed
@ban_restricted
@parameters_needed(1)
def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    insta_username = update.message.text.split()[1]
    StatusHandler.handle_status(bot,
                                update,
                                WaveService.register_for_wave(user, insta_username),
                                insta_username=insta_username)


@ban_restricted
def pay_handler(bot, update):
    StatusHandler.handle_status(bot,
                                update,
                                Status.SendPayLink)


@ban_restricted
def quit_wave_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    StatusHandler.handle_status(bot,
                                update,
                                WaveService.delete_user_from_wave(user))



