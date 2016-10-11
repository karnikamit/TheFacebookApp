# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from routes.baseroutes import app
from flask_app import HOST, PORT


try:
    app.run(HOST, PORT)
except Exception, e:
    print 'Exception while running application: {}'.format(e)
