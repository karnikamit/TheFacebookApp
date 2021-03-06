# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import logging
import os
import urllib

import facebook
from pyramid.config import Configurator
from pyramid.response import FileResponse
from pyramid.view import view_config

from config import facebook_creds    # keep all your tokens, IDs in config.py
from pyramid_app.sound_cloud.sound import get_tracks

# import json
_here = os.path.dirname(__file__)
_templates = r'%s\templates' % _here        # windows path
logger = logging.getLogger(__name__)


@view_config(route_name='myview')
def my_view(request):
    response = FileResponse(_templates+r'\index.html')
    return response


@view_config(route_name='fb_post', request_method='POST', renderer='json')
def post_to_wall(request, access_token=facebook_creds['ACCESS_TOKEN'], attachments={}, profile_id='me'):
    fb_api = get_fb_api(access_token=access_token)
    try:
        msg = request.body.split('=')[-1]
        status = urllib.unquote_plus(msg)
        posting = fb_api.put_wall_post(status, attachment=attachments, profile_id=profile_id)
    except Exception, e:
        logging.error('Exception while posting: %s' %e)
    else:
        return posting


@view_config(route_name='get_tracks', request_method='GET', renderer='json')
def tracks():
    tracks = get_tracks()
    return tracks


@view_config(route_name='play_tic_tac_toe', request_method='GET', renderer='json')
def play_tic(request):
    response = FileResponse(_templates + r'\tictac.html')
    return response


def make_pyramid_app(route_details={}):
    """

    :param route_details: {route_name: fn,...}
    :return: pyramid wsgi App
    """
    try:
        config = Configurator()
        for name, fn in route_details.iteritems():
            config.add_route('%s' % name, '/%s' % name)
            config.add_view(fn, route_name='%s' % name)
        return config.make_wsgi_app()
    except Exception, e:
        logging.error('Exception while making pyramid app: %s' % e)


def get_fb_api(access_token):
    try:
        api = facebook.GraphAPI(access_token)
    except Exception, e:
        logging.error('exception while getting fb api: %s' % e)
    else:
        return api


if __name__ == '__main__':
    config = Configurator()
    config.add_route('test', '/test')
    config.add_route('fb_post', '/facebook/post')
    config.scan()
    app = config.make_wsgi_app()

