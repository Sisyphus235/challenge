# -*- coding: utf8 -*-


class ApiException(Exception):
    """
    wrap internal exceptions
    """
    def __init__(self, status, message):
        self.status = status
        self.message = message
