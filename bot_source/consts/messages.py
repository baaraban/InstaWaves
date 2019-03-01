from abc import ABC, abstractmethod
from telegram.parsemode import ParseMode
from consts.application_level_consts import *


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
        return f'{counter + 1}. <a href="{link}">post</a> \n'

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


class AssuringStepStartedMessage(Message):
    def render(self, **kwargs):
        return "Assuring step has been started... It may take few minutes"

    def get_parse_mode(self):
        return ParseMode.HTML


class WaveIsFinishedMessage(Message):
    @staticmethod
    def get_warned_string(warned):
        if len(warned) == 0:
            return "Nobody was warned. "
        result = "<b>Warned: </b>"
        for warn in warned:
            result += f'{warn}, '
        return f'{result[:-2]}. '

    @staticmethod
    def get_banned_string(banned):
        if len(banned) == 0:
            return "Nobody was banned."
        result = "<b>Banned: </b>"
        for ban in banned:
            result += f'{ban}, '
        return f'{result[:-2]}. '

    def render(self, **kwargs):
        summary = kwargs['summary']
        return f'{WaveIsFinishedMessage.get_warned_string(summary.warned)} \n' \
               f'{WaveIsFinishedMessage.get_banned_string(summary.banned)}'

    def get_parse_mode(self):
        return ParseMode.HTML


class SendPayLinkMessage(Message):
    def render(self, **kwargs):
        return f'<a href="{PAY_LINK}">payment link</a>'

    def get_parse_mode(self):
        return ParseMode.HTML


class InstagramProfileHasNoPostsMessage(Message):
    def render(self, **kwargs):
        return "Current profile has no posts"

    def get_parse_mode(self):
        return ParseMode.HTML


class WarnIsRemovedFromUserMessage(Message):
    def render(self, **kwargs):
        return "Warn is removed from {}".format(kwargs["username"])

    def get_parse_mode(self):
        return ParseMode.HTML


class NotRegisteredInWaveMessage(Message):
    def render(self, **kwargs):
        return "You didn't register for a wave"

    def get_parse_mode(self):
        return ParseMode.HTML


class UnregisteredFromWaveMessage(Message):
    def render(self, **kwargs):
        return "You are unregistered from current wave"

    def get_parse_mode(self):
        return ParseMode.HTML


class UserIsPrivilegedMessage(Message):
    def render(self, **kwargs):
        return f"User {kwargs['username']} is privileged now"

    def get_parse_mode(self):
        return ParseMode.HTML


class UserIsUnprivilegedMessage(Message):
    def render(self, **kwargs):
        return f"User {kwargs['username']} is unprivileged now"

    def get_parse_mode(self):
        return ParseMode.HTML
