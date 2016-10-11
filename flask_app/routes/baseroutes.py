# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from flask_app.app import make_flask_app
from flask import request, jsonify, render_template, url_for

app = make_flask_app()


@app.route('/')
def greet():
    return 'Hello Amit'


@app.route('/write_wall', methods=['POST'])
def fb_post():
    request_body = request.json
    return jsonify(request_body)
