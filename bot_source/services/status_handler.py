from consts.statuses import Status
from consts.messages import Message


class StatusHandler:
    _handling_dict = {
        Status.Unauthorized: Message.Unauthorized,
        Status.Banned: Message.Banned
    }

    @staticmethod
    def handle_status(bot, update, status):
        bot.send_message(chat_id=update.message.chat_id, text=StatusHandler._handling_dict[status])
