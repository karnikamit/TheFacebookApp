# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from flask import request, jsonify, render_template
import os
from flask import Flask
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
_here = os.path.dirname(__file__)
_templates = r'%s\templates' % _here        # windows path
_static_folder = r'%s\templates\static'
app = Flask(__name__)
# , static_folder=_templates, static_url_path='/templates'
import urllib
import facebook, soundcloud
import logging
from config import facebook_creds, sound_cloud_creds    # keep all your tokens, IDs in config.py


def get_client(client_id=None):
    """

    :param client_id:
    :return: client objct
    """
    try:
        if not client_id:
            client_id = sound_cloud_creds['client_id']
        client = soundcloud.Client(client_id=client_id)
    except Exception, e:
        logger.error('Exception while geetting soundCloud client: %s' % e)
    else:
        return client


@app.route('/get-tracks/<limit>', methods=['GET'])
def get_tracks(limit=10, client_id=sound_cloud_creds['client_id']):
    '''
    Souond Cloud Resource obj attrs!

    [u'attachments_uri', u'video_url', u'track_type', u'release_month', u'original_format', u'label_name', u'duration',
     u'id', u'streamable', u'user_id', u'title', u'favoritings_count', u'commentable', u'label_id', u'state',
      u'downloadable', u'waveform_url', u'sharing', u'description', u'release_day', u'purchase_url', u'permalink',
       u'comment_count', u'purchase_title', u'stream_url', u'last_modified', u'user', u'genre', u'isrc', u'download_count',
        u'permalink_url', u'playback_count', u'kind', u'release_year', u'license', u'artwork_url', u'created_at', u'bpm',
         u'uri', u'original_content_size', u'key_signature', u'release', u'tag_list', u'embeddable_by']

    '''

    client = get_client(client_id)
    tracks = client.get('/tracks', limit=int(limit))
    sound_cloud_tracks = []
    for track in tracks:
        if hasattr(track, 'title') and hasattr(track, 'stream_url'):
            track_details = {
                'title':  track.title,
                'url': track.permalink_url,
            }
            sound_cloud_tracks.append(track_details)
    return jsonify(sound_cloud_tracks)


@app.route('/getWidget', methods=['POST'])
def get_widget():
    widget = {'html': ''}
    data = request.json
    client = get_client()
    embed_info = client.get('/oembed', url=data.get('url', ''))
    if hasattr(embed_info, 'html'):
        widget['html'] = embed_info.html
    return jsonify(widget)


def get_fb_api(access_token=facebook_creds['ACCESS_TOKEN']):
    try:
        api = facebook.GraphAPI(access_token)
    except Exception, e:
        logging.error('exception while getting fb api: %s' % e)
    else:
        return api


@app.route('/t1')
def get_angular():
    return render_template('t1.html')


@app.route('/index')
def get_index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>HI</p>
</body>
</html>'''


@app.route('/write_wall', methods=['POST'])
def fb_post(attachments={}, profile_id='me'):
    request_body = request.json
    fb_api = get_fb_api()
    status = urllib.unquote_plus(request_body['msg'])
    try:
        posting = fb_api.put_wall_post(status, attachment=attachments, profile_id=profile_id)
    except Exception, e:
        posting = {'response': 'failed'}
        logger.error('Exception while Posting on FB: {}'.format(e))
    return jsonify(posting)


if __name__ == '__main__':
    tracks = get_tracks()
