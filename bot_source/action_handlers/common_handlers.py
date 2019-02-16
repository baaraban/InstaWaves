from services.wave_service import WaveService
from services.status_handler import StatusHandler
from internal_decorators.ban_restricted import ban_restricted
from internal_decorators.username_needed import username_needed
from models.user import UserFactory


@username_needed
@ban_restricted
def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    insta_username = update.message.text.split()[1]
    StatusHandler.handle_status(bot,
                                update,
                                WaveService.register_for_wave(user, insta_username),
                                insta_username=insta_username)


@ban_restricted
def pay_handler(bot, update):
    return None



