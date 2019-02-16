from consts.statuses import Status
from consts.messages import *


class StatusHandler:
    _handling_dict = {
        Status.InternalError: InternalErrorMessage(),
        Status.Unauthorized: UnauthorizedMessage(),
        Status.Banned: BannedMessage(),
        Status.NewWaveCreated: NewWaveCreatedMessage(),
        Status.UserIsBanned: UserIsBannedMessage(),
        Status.UserIsWarned: UserIsWarnedMessage(),
        Status.RegisteredForWave: RegisteredForWaveMessage(),
        Status.AlreadyRegisteredForWave: AlreadyRegisteredForWaveMessage(),
        Status.InstagramProfileDoesNotExist: InstagramProfileDoesNotExistMessage(),
        Status.InstagramProfileIsPrivate: InstagramProfileIsPrivateMessage(),
        Status.UserDoesNotExist: UserDoesNotExistMessage(),
        Status.WaveStateAlreadyPresent: WaveStateAlreadyPresentMessage()
    }

    @staticmethod
    def handle_status(bot, update, status, **kwargs):
        message = StatusHandler._handling_dict[status]
        text = message.render(**kwargs)
        bot.send_message(chat_id=update.message.chat_id,
                         text=text,
                         parser=message.get_parser()
                         )
