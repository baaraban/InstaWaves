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


class BannedMessage(Message):
    def render(self, **kwargs):
        return "You are banned from bot functionality"

    def get_parser(self):
        return ParseMode.HTML
