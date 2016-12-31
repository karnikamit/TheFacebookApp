# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
# from flask_app.app import make_flask_app
from flask import request, jsonify, render_template, url_for
import os
from flask import Flask
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
_here = os.path.dirname(__file__)
_templates = r'%s\templates' % _here        # windows path
_static_folder = r'%s\templates\static'
app = Flask(__name__, static_folder=_templates, static_url_path='/templates')
# static_url_path=_templates,

@app.route('/t1')
def get_angular():
    logger.info(_templates)
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
def fb_post():
    request_body = request.json
    return jsonify(request_body)
