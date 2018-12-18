# -*- coding: utf8 -*-

from enum import Enum


class ResponseCodeEnum(Enum):
    """
    status code
    """
    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    NOT_FOUND = 4
    ALREADY_EXISTS = 5
    PERMISSION_DENIED = 6
    INTERNAL = 7
    UNAVAILABLE = 8
