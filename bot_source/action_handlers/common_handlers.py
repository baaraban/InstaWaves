from models.user import UserFactory
from services.user_service import UserService


def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    username = update.message.text.split()[1]
    UserService.register_for_wave(user, username)
    bot.send_message(chat_id=update.message.chat_id, text='You are successfully registered')


def pay_handler(bot, update):
    return None





