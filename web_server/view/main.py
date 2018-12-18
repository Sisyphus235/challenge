# -*- coding: utf8 -*-

from flask import Blueprint, render_template, request

from web_server.utility.api_exception import ApiException
from web_server.utility.enum import ResponseCodeEnum
from web_server.controller import string_clean as clean
from web_server.controller import max_block as max_sub
from web_server.controller import reorder_block as reorder

blueprint = Blueprint('main', __name__)


@blueprint.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@blueprint.route('/string_clean', methods=['GET', 'POST'])
def string_clean():
    data = request.args.to_dict()
    string = data.get('string')
    if not string:
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT.value, 'invalid string')

    string = clean.string_clean(string)
    return render_template('string_clean.html', string=string)


@blueprint.route('/max_block', methods=['GET', 'POST'])
def max_block():
    data = request.args.to_dict()
    string = data.get('string')
    if not string:
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT.value, 'invalid string')

    string = max_sub.max_block(string)
    return render_template('max_block.html', string=string)


@blueprint.route('/reorder_block', methods=['GET', 'POST'])
def reorder_block():
    data = request.args.to_dict()
    string = data.get('string')
    if not string:
        raise ApiException(ResponseCodeEnum.INVALID_ARGUMENT.value, 'invalid string')

    string = reorder.reorder_block(string)
    return render_template('reorder_block.html', string=string)
