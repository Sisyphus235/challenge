# -*- coding: utf8 -*-

import pytest

from web_server.controller.string_clean import string_clean
from web_server.utility.api_exception import ApiException


def test_string_clean():
    """
    test string clean function
    :return:
    """
    assert string_clean("yyzzza") == 'yza'
    assert string_clean("abbbbcdd") == 'abcd'
    assert string_clean("Helo") == 'Helo'
    assert string_clean("") == ''
    assert string_clean("ababc") == 'ababc'
    assert string_clean("12as3d22") == '12as3d2'

    with pytest.raises(ApiException) as exception:
        string_clean(1)
    assert exception.value.args[1] == 'invalid type'
