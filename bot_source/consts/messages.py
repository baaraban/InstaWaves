from abc import ABC, abstractmethod
from telegram.parsemode import ParseMode


class Message(ABC):
    def __init(self):
        super().__init__()

    @abstractmethod
    def render(self, **kwargs):
        pass

    @abstractmethod
    def get_parse_mode(self):
        pass


class UnauthorizedMessage(Message):
    def render(self, **kwargs):
        return "You don't have permission to complete this action"

    def get_parse_mode(self):
        return ParseMode.HTML


class InternalErrorMessage(Message):
    def render(self, **kwargs):
        return "Internal error occurred"

    def get_parse_mode(self):
        return ParseMode.HTML


class BannedMessage(Message):
    def render(self, **kwargs):
        return "You are banned from bot functionality"

    def get_parse_mode(self):
        return ParseMode.HTML


class NewWaveCreatedMessage(Message):
    def render(self, **kwargs):
        return "New wave is created"

    def get_parse_mode(self):
        return ParseMode.HTML


class UserIsBannedMessage(Message):
    def render(self, **kwargs):
        return "User {} is banned".format(kwargs["username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class UserIsUnbannedMessage(Message):
    def render(self, **kwargs):
        return "User {} is unbanned".format(kwargs["username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class UserIsWarnedMessage(Message):
    def render(self, **kwargs):
        return "User {} is warned".format(kwargs["username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class RegisteredForWaveMessage(Message):
    def render(self, **kwargs):
        return "{} profile is registered for wave".format(kwargs["insta_username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class AlreadyRegisteredForWaveMessage(Message):
    def render(self, **kwargs):
        return "{} profile is already registered for wave".format(kwargs["insta_username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class InstagramProfileDoesNotExistMessage(Message):
    def render(self, **kwargs):
        return "{} profile doesn't exist".format(kwargs["insta_username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class InstagramProfileIsPrivateMessage(Message):
    def render(self, **kwargs):
        return "{} profile is private".format(kwargs["insta_username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class UserDoesNotExistMessage(Message):
    def render(self, **kwargs):
        return "User {} does not exist".format(kwargs["username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class WaveStateAlreadyPresentMessage(Message):
    def render(self, **kwargs):
        return "Wave in {} state already exists".format(kwargs["state"])

    def get_parse_mode(self):
        return ParseMode.HTML


class WaveBiddingStartedMessage(Message):
    @staticmethod
    def _link_to_html(counter, link):
        return f'{counter + 1}. <a href="{link}">post</a>'

    def render(self, **kwargs):
        links = kwargs["links"]
        result_string = ''
        for i in range(len(links)):
            result_string += WaveBiddingStartedMessage._link_to_html(i, links[i])
        return result_string

    def get_parse_mode(self):
        return ParseMode.HTML


class NoWaveForRegistrationMessage(Message):
    def render(self, **kwargs):
        return "No wave available for registration"

    def get_parse_mode(self):
        return ParseMode.HTML


class UsernameIsNeededMessage(Message):
    def render(self, **kwargs):
        return "Please, set your username before using this logic"

    def get_parse_mode(self):
        return ParseMode.HTML


class NotCorrectParametersPassedMessage(Message):
    def render(self, **kwargs):
        return "Incorrect parameters passed"

    def get_parse_mode(self):
        return ParseMode.HTML
