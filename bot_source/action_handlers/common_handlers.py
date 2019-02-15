from models.user import UserFactory
from services.user_service import UserService
from internal_decorators.ban_restricted import ban_restricted


@ban_restricted
def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    username = update.message.text.split()[1]
    UserService.register_for_wave(user, username)
    bot.send_message(chat_id=update.message.chat_id, text='You are successfully registered')


@ban_restricted
def pay_handler(bot, update):
    return None





