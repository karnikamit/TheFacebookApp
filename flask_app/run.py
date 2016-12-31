# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from routes.baseroutes import app
from config import HOST, PORT
import logging
logging.basicConfig(level=logging.INFO)
logging.info('Starting Falsk app...')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


try:
    app.run(HOST, PORT)
except Exception, e:
    logger.error('Exception while running application: {}'.format(e))
