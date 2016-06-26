# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import facebook
from pyramid.config import Configurator


def make_app(package):
    config = Configurator()
    config.add_route('myview', '/')
    config.add_route('fb_post', '/facebook/post')
    config.scan(package=package)
    return config.make_wsgi_app()


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
    return graph
