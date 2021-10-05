from typing import *
from aqt.webview import AnkiWebView
# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import all of the Qt GUI library
from aqt.qt import *
import os
import json

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


def load_all_content():
    pass
