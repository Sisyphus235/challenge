# -*- coding: utf8 -*-

from web_server.utility.api_exception import ApiException
from web_server.utility.enum import ResponseCodeEnum


def string_clean(string: str) -> str:
    """
    clean duplicated characters in a string
    :param string:
    :return:
    """
    # initial check
    if not isinstance(string, str):
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT, 'invalid type')
    if string == '':
        return string

    # delete duplicated characters
    string_list = list(string)
    cur = 0
    for index in range(1, len(string_list)):
        if string_list[index] == string_list[cur]:
            continue
        cur += 1
        string_list[cur] = string_list[index]
    string = ''.join(string_list[:cur + 1])
    return string
