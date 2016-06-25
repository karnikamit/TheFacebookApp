# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import facebook
from config import PAGE_ID, ACCESS_TOKEN    # keep all your tokens, IDs in config.py


def main(msg_to_post):
    cfg = {"page_id": '%d' % PAGE_ID, "access_token": ACCESS_TOKEN}
    # api = get_api(cfg)
    api = facebook.GraphAPI(cfg['access_token'])
    api.put_wall_post(msg_to_post)


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
          page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
    return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main("Hello, World!")