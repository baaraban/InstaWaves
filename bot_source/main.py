from routing.routing import initialize_handlers
from telegram.ext import Updater
from data_access.base_db_operations import create_db_if_not_exists
from consts.application_level_consts import *

create_db_if_not_exists()

updater = Updater(TOKEN)

initialize_handlers(updater.dispatcher)

updater.start_polling()

updater.idle()




