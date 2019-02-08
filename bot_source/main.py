# from data_access.base_db_operations import setup_db
# setup_db()


from routing.routing import initialize_handlers
from telegram.ext import Updater

TOKEN = '702406299:AAF_J4EuBaMexNmpVR4Lu4hNOiDtz9dhd0c'

updater = Updater(TOKEN)

initialize_handlers(updater.dispatcher)

updater.start_polling()

updater.idle()

from models.wave import WaveFactory
from data_access.wave_manipulations import insert_wave
wave = WaveFactory.get_new_wave()
insert_wave(wave)

# from models.user import User
# import data_access.users_manipulations as u_man
# user = User("insiss", '1224', 'bubu', '', False, 0, False)
# insert_user(user)
# u_man.fullfill_model(user)




