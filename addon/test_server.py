from typing import *
from command_processor import kyoro_pycmd_handler
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/<command>/")
@app.route("/<command>/<arg>")
def getIndexedSources(command: str, arg: Union[None, str] = None):
    argSting = f":{arg}" if arg is not None else ""
    commandString = f"Kyoro.{command}{argSting}"
    handled = (False, None)
    resp = kyoro_pycmd_handler(handled, commandString, None)
    return json.dumps(resp[1], default=vars)
