from telegram.ext import Updater, CommandHandler


TOKEN = '702406299:AAF_J4EuBaMexNmpVR4Lu4hNOiDtz9dhd0c'

updater = Updater(TOKEN)


def test(bot, update):
    update.message.reply_text(
        'Extension is kinda cool'
    )


updater.dispatcher.add_handler(CommandHandler('nextwave', test))

updater.start_polling()

updater.idle()

