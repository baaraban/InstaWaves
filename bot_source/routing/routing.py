from telegram.ext import CommandHandler
import action_handlers.common_handlers as ch
import action_handlers.admin_handlers as ah


def initialize_handlers(dispatcher):
    # common actions handlers
    dispatcher.add_handler(CommandHandler('register', ch.register_handler))
    dispatcher.add_handler(CommandHandler('pay', ch.pay_handler))
    dispatcher.add_handler(CommandHandler('quit_wave', ch.quit_wave_handler))

    # admin actions handlers
    dispatcher.add_handler(CommandHandler('create_wave', ah.create_wave_handler))
    dispatcher.add_handler(CommandHandler('warn', ah.warn_user_handler))
    dispatcher.add_handler(CommandHandler('ban', ah.ban_user_handler))
    dispatcher.add_handler(CommandHandler('unban', ah.unban_user_handler))
    dispatcher.add_handler(CommandHandler('start_bidding', ah.start_bidding_handler))
    dispatcher.add_handler(CommandHandler('assuring_step', ah.assuring_step_handler))