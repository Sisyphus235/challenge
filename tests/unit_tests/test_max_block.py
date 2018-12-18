# -*- coding: utf8 -*-

import pytest

from web_server.controller.max_block import max_block
from web_server.utility.api_exception import ApiException


def test_max_block():
    """
    test max block function
    :return:
    """
    assert max_block("hoopla") == 2
    assert max_block("abbCCCddBBBxx") == 3
    assert max_block("") == 0
    assert max_block("aa") == 2
    assert max_block("12as3d22") == 2

    with pytest.raises(ApiException) as exception:
        max_block(1)
    assert exception.value.args[1] == 'invalid type'
