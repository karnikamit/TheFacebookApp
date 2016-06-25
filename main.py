# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import logging
import facebook
from wsgiref.simple_server import make_server
from fb import post





def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
    return graph
