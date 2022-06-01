import sys

sys.path.append("..")
sys.path.append("../azure_functions")
import json

import azure_functions.shared_code.note2html
import azure_functions.shared_code.tw2html
from flask import Flask, Response

app = Flask(__name__)


@app.route("/notes")
def get_notes():
    with open("../azure_functions/local.settings.json", "r") as f:
        keys = json.load(f)["Values"]
        connection_string = keys["StorageAccountConnectionString"]

    html = azure_functions.shared_code.note2html.get_notes_timeline(connection_string)
    return Response(html, mimetype="text/html")


@app.route("/tw")
def get_tw():
    with open("../azure_functions/local.settings.json", "r") as f:
        keys = json.load(f)["Values"]

    twitter_keys = {
        "consumer_key": keys["api_key"],
        "consumer_secret": keys["api_secret"],
        "access_token": keys["access"],
        "access_token_secret": keys["secret"],
    }

    html = azure_functions.shared_code.tw2html.get_timeline_html(twitter_keys)
    return Response(html, mimetype="text/html")
