# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import logging
from wsgiref.simple_server import make_server
from main import make_app
from fb import post


def start_server(pyramid_app, host='127.0.0.1', port=9000):
    """

    :param pyramid_app: pyramid wsgi App
    :param host: default 127.0.0.1
    :param port: default 9000
    :return: start server on host:port
    """
    logging.info('pyramid wsgi app running on {0}:{1}'.format(host, port))
    server = make_server(host, port, pyramid_app)
    return server.serve_forever()

if __name__ == '__main__':
    app = make_app(post)
    start_server(app)
