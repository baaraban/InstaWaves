from consts.statuses import Status
from consts.messages import *


class StatusHandler:
    _handling_dict = {
        Status.Unauthorized: UnauthorizedMessage(),
        Status.Banned: BannedMessage()
    }

    @staticmethod
    def handle_status(bot, update, status, **kwargs):
        message = StatusHandler._handling_dict[status]
        text = message.render(**kwargs)
        bot.send_message(chat_id=update.message.chat_id,
                         text=text,
                         parser=message.get_parser()
                         )
