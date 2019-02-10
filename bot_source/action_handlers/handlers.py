from models.user import UserFactory
from services.user_service import UserService
from services.wave_service import WaveService


def create_wave_handler(bot, update):
    WaveService.create_wave()
    bot.send_message(chat_id=update.message.chat_id, text='New wave created')


def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    username = update.message.text.split()[1]
    UserService.register_for_wave(user, username)
    bot.send_message(chat_id=update.message.chat_id, text='You are successfully registered')



