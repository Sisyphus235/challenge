# -*- coding: utf8 -*-

import pytest

from web_server.controller.reorder_block import _transfer_letter, _compare, _partition, _quick_sort, reorder_block
from web_server.utility.api_exception import ApiException


def test_transfer_letter():
    """
    test transfer letter function
    :return:
    """
    assert _transfer_letter('A') == 96.5


def test_compare():
    """
    test compare function
    :return:
    """
    assert _compare('D', 'c') == False


def test_reorder_block():
    """
    test reorder block function, based on unicode
    :return:
    """
    assert reorder_block('bbAAccAadF') == 'AAAabbccdF'
    assert reorder_block('hoopla') == 'ahloop'
    assert reorder_block('bbA/s1Acc3Aak-dF') == '-/13AAAabbccdFks'
    assert reorder_block('我adc') == 'acd我'
