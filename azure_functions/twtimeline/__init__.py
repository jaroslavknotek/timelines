import os
import logging
import shared_code.tw2html
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    twitter_keys = {
    'consumer_key':os.environ["api_key"],
    'consumer_secret': os.environ["api_secret"],
    'access_token':  os.environ["access"],
    'access_token_secret' : os.environ["secret"]
    }

    html = shared_code.tw2html.get_timeline_html(twitter_keys)    
    return func.HttpResponse(html, mimetype="text/html")
