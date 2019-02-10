from telegram.ext import CommandHandler
import action_handlers.handlers as ah


def initialize_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('create_wave', ah.create_wave_handler))
    dispatcher.add_handler(CommandHandler('register', ah.register_handler))
