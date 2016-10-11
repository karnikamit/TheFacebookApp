# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from flask import Flask


def make_flask_app():
    """

    :return: Flask wsgi app
    """
    return Flask(__name__)
