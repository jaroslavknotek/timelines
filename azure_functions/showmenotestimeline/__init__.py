import logging
import os

import azure.functions as func

import shared_code.note2html


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    connection_string = os.environ["StorageAccountConnectionString"]
    html = shared_code.note2html.get_notes_timeline(connection_string)
    return func.HttpResponse(html, mimetype="text/html")
