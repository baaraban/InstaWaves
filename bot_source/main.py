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
# #import data_access.users_manipulations as u_man
# import data_access.wave_manipulations as w_man
# user = User(None, 1224, "insiss", 'bubu', None, False, None, None)
# # #u_man.insert_user(user)
# # res = u_man.fullfill_model(user)
# # print(res)
# w_man.register_for_wave('baaraban', user)





