# -*- coding: utf8 -*-

from web_server.utility.api_exception import ApiException
from web_server.utility.enum import ResponseCodeEnum


def max_block(string: str) -> str:
    """
    return max block in a string
    :param string:
    :return:
    """
    # initial check
    if not isinstance(string, str):
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT, 'invalid type')
    if string == '':
        return 0

    # search max block length
    cur, count, record = 0, 1, 1
    for index in range(1, len(string)):
        if string[index] == string[cur]:
            count += 1
            continue
        if count > record:
            record = count
        cur, count = index, 1

    if count > record:
        record = count
    return record
