# -*- coding: utf8 -*-

from web_server.utility.api_exception import ApiException
from web_server.utility.enum import ResponseCodeEnum

CAPITAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SMALL = 'abcdefghifklmnopqrstuvwxyz'


def _transfer_letter(letter: str) -> float:
    """
    tarnsfer capital letters' ord values
    :param letter:
    :return:
    """
    return ord(SMALL[CAPITAL.index(letter)]) - 0.5


def _compare(char_a: str, char_b: str) -> bool:
    """
    compare characters
    :param char_a:
    :param char_b:
    :return:
    """
    a = _transfer_letter(char_a) if char_a in CAPITAL else ord(char_a)
    b = _transfer_letter(char_b) if char_b in CAPITAL else ord(char_b)
    return a <= b


def _partition(array: list, start: int, end: int) -> int:
    """
    find pivot value
    :param array:
    :param start:
    :param end:
    :return:
    """
    i = start - 1
    x = array[end]

    for j in range(start, end):
        if _compare(array[j], x):
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def _quick_sort(array: list, start: int, end: int) -> str:
    """
    sort list strings using quick sort
    :param array:
    :param start:
    :param end:
    :return:
    """
    # create stack
    size = end - start + 1
    stack = [0] * size

    # init top
    top = -1

    # init stack
    top += 1
    stack[top] = start
    top += 1
    stack[top] = end

    # quick sort
    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        pivot = _partition(array, start, end)

        if pivot - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < end:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = end

    return ''.join(array)


def reorder_block(string: str) -> str:
    """
    reorder block based on UTF8 order, treating capital letters as values just less than small letters
    :param string:
    :return:
    """
    if not isinstance(string, str):
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT, 'invalid type')
    if string == '':
        return string

    string = _quick_sort(list(string), 0, len(string) - 1)
    return string
