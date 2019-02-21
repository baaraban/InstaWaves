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
    WaveBiddingStarted = 13
    NoWaveForRegistration = 14
    UsernameIsNeeded = 15
    NotCorrectParametersPassed = 16
    AssuringStepStarted = 17
    WaveIsFinished = 18
    SendPayLink = 19
    InstagramProfileHasNoPosts = 20
    WarnIsRemovedFromUser = 21
    NotRegisteredInWave = 22
    UnregisteredFromWave = 23
    UserIsPrivileged = 24


