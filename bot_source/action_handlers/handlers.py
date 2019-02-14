from models.user import UserFactory
from services.user_service import UserService
from services.wave_service import WaveService


def ban_user_handler(bot, update):
    return None


def warn_user_handler(bot, update):
    username = update.message.text.split()[1]
    UserService.warn_user(username)
    bot.send_message(chat_id=update.message.chat_id, text="{} user is warned".format(username))


def start_bidding_handler(bot, update):
    return None


def assuring_step_handler(bot, update):
    return None


def finish_wave_handler(bot, update):
    return None


def create_wave_handler(bot, update):
    WaveService.create_wave()
    bot.send_message(chat_id=update.message.chat_id, text='New wave created')


def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    username = update.message.text.split()[1]
    UserService.register_for_wave(user, username)
    bot.send_message(chat_id=update.message.chat_id, text='You are successfully registered')


def pay_handler(bot, update):
    return None





