from typing import *
from command_processor import kyoro_pycmd_handler
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Run: FLASK_APP=test_server.py FLASK_ENV=development flask run --port 8006


@app.route("/<command>/")
@app.route("/<command>/<arg>/")
def runKyoroCommand(command: str, arg: Union[None, str] = None):
    argSting = f":{arg}" if arg is not None else ""
    commandString = f"Kyoro.{command}{argSting}"
    handled = (False, None)
    resp = kyoro_pycmd_handler(handled, commandString, None)
    # This must be json.dumps() only to be compatible with Anki's intenrals
    return json.dumps(resp[1])
