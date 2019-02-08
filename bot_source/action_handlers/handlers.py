from models.user import User, UserFactory
from models.wave import Wave, WaveFactory
import data_access.wave_manipulations as w_man
import data_access.users_manipulations as u_man


def nextwave_handler(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text=str(update.message))


def create_wave_handler(bot, update):
    new_wave = WaveFactory.get_new_wave()
    wave_name = update.message.text.split()[1]
    new_wave.name = wave_name
    w_man.insert_wave(new_wave)
    bot.send_message(chat_id=update.message.chat_id, text='New wave created')


def register_handler(bot, update):
    user = UserFactory.get_user_from_update(update)
    if u_man.is_banned(user):
        return
    username = update.message.text.split()[1]
    user = u_man.fullfill_model(user)
    w_man.register_for_wave(username, user)
    bot.send_message(chat_id=update.message.chat_id, text='You are successfully registered')



