def nextwave_handler(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text=str(update.message))


