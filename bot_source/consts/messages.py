from abc import ABC, abstractmethod
from telegram.parsemode import ParseMode


class Message(ABC):
    def __init(self):
        super().__init__()

    @abstractmethod
    def render(self, **kwargs):
        pass

    @abstractmethod
    def get_parser(self):
        pass


class UnauthorizedMessage(Message):
    def render(self, **kwargs):
        return "You don't have permission to complete this action"

    def get_parser(self):
        return ParseMode.HTML


class InternalErrorMessage(Message):
    def render(self, **kwargs):
        return "Internal error occurred"

    def get_parser(self):
        return ParseMode.HTML


class BannedMessage(Message):
    def render(self, **kwargs):
        return "You are banned from bot functionality"

    def get_parser(self):
        return ParseMode.HTML


class NewWaveCreatedMessage(Message):
    def render(self, **kwargs):
        return "New wave is created"

    def get_parser(self):
        return ParseMode.HTML


class UserIsBannedMessage(Message):
    def render(self, **kwargs):
        return "User {} is banned".format(kwargs["username"])

    def get_parser(self):
        return ParseMode.HTML


class UserIsUnbannedMessage(Message):
    def render(self, **kwargs):
        return "User {} is unbanned".format(kwargs["username"])

    def get_parser(self):
        return ParseMode.HTML


class UserIsWarnedMessage(Message):
    def render(self, **kwargs):
        return "User {} is warned".format(kwargs["username"])

    def get_parser(self):
        return ParseMode.HTML


class RegisteredForWaveMessage(Message):
    def render(self, **kwargs):
        return "{} profile is registered for wave".format(kwargs["insta_username"])

    def get_parser(self):
        return ParseMode.HTML


class AlreadyRegisteredForWaveMessage(Message):
    def render(self, **kwargs):
        return "{} profile is already registered for wave".format(kwargs["insta_username"])

    def get_parser(self):
        return ParseMode.HTML


class InstagramProfileDoesNotExistMessage(Message):
    def render(self, **kwargs):
        return "{} profile doesn't exist".format(kwargs["insta_username"])

    def get_parser(self):
        return ParseMode.HTML


class InstagramProfileIsPrivate(Message):
    def render(self, **kwargs):
        return "{} profile is private".format(kwargs["insta_username"])

    def get_parser(self):
        return ParseMode.HTML


class UserDoesNotExist(Message):
    def render(self, **kwargs):
        return "User {} does not exist".format(kwargs["username"])

    def get_parser(self):
        return ParseMode.HTML
