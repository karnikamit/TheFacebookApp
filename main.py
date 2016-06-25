# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import facebook
from config import facebook_creds    # keep all your tokens, IDs in config.py


def main(msg_to_post):
    cfg = {"page_id": facebook_creds['PAGE_ID'], "access_token": facebook_creds['ACCESS_TOKEN']}
    # api = get_api(cfg)
    api = facebook.GraphAPI(cfg['access_token'])
    api.put_wall_post(msg_to_post)


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
    return graph


if __name__ == "__main__":
  main("Hello, World!")
