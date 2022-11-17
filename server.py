import sys

import json

import os

import app.tw2html
from flask import Flask, Response

flask_app = Flask(__name__)



@flask_app.route("/tw")
def get_tw():
    twitter_keys = {
        "consumer_key": os.environ["TW_API_KEY"],
        "consumer_secret": os.environ["TW_API_SECRET"],
        "access_token": os.environ["TW_ACCESS_TOKEN"],
        "access_token_secret": os.environ["TW_TOKEN_SECRET"],
    }

    html = app.tw2html.get_timeline_html(twitter_keys)
    return Response(html, mimetype="text/html")
