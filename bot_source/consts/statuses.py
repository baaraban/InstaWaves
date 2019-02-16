from enum import Enum


class Status(Enum):
    InternalError = 0
    Unauthorized = 1
    Banned = 2
    NewWaveCreated = 3
    UserIsBanned = 4
    UserIsUnbanned = 5
    UserIsWarned = 6
    RegisteredForWave = 7
    AlreadyRegisteredForWave = 8
    InstagramProfileDoesNotExist = 9
    InstagramProfileIsPrivate = 10
    UserDoesNotExist = 11
    WaveStateAlreadyPresent = 12

