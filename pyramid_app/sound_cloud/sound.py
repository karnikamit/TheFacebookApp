# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import logging
import soundcloud
from pyramid_app.config import sound_cloud_creds

logger = logging.getLogger(__name__)


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


def get_tracks(client_id=None):
    client = get_client(client_id)
    tracks = client.get('/tracks', limit=10)
    track_details = {track.title: track.stream_url for track in tracks}
    return track_details

'''
Souond Cloud Resource obj attrs!

[u'attachments_uri', u'video_url', u'track_type', u'release_month', u'original_format', u'label_name', u'duration',
 u'id', u'streamable', u'user_id', u'title', u'favoritings_count', u'commentable', u'label_id', u'state',
  u'downloadable', u'waveform_url', u'sharing', u'description', u'release_day', u'purchase_url', u'permalink',
   u'comment_count', u'purchase_title', u'stream_url', u'last_modified', u'user', u'genre', u'isrc', u'download_count',
    u'permalink_url', u'playback_count', u'kind', u'release_year', u'license', u'artwork_url', u'created_at', u'bpm',
     u'uri', u'original_content_size', u'key_signature', u'release', u'tag_list', u'embeddable_by']

'''
if __name__ == '__main__':
    print get_tracks(sound_cloud_creds['client_id'])
