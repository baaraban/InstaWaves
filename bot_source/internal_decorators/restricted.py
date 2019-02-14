from functools import wraps

LIST_OF_ADMINS = [234862974]


def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            bot.send_message(chat_id=update.message.chat_id, text="You don't have permission to complete this action")
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
