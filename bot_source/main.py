from data_access.setup import setup_db
from routing.routing import initialize_handlers
from telegram.ext import Updater

TOKEN = '702406299:AAF_J4EuBaMexNmpVR4Lu4hNOiDtz9dhd0c'

updater = Updater(TOKEN)

initialize_handlers(updater.dispatcher)

updater.start_polling()

updater.idle()


