from typing import Any, Tuple
from anki import hooks
from anki import gui_hooks
import aqt
from aqt.webview import AnkiWebView
# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
import io
import os
import glob

addon_path = os.path.dirname(__file__)


class KyroWebView(AnkiWebView):
    def __init__(self):
        AnkiWebView.__init__(self, title="Kyoro")

        html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta
      name="description"
      content="Web site created using create-snowpack-app"
    />
    <title>Snowpack App</title>
    <script type=\"module\">{0}</script>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <style>{1}</style>
  </body>
</html>
        """

        js = open(os.path.join(addon_path, "dist/index.js")).read()
        css = open(os.path.join(addon_path, "dist/index.css")).read()

        self.stdHtml(html.format(js, css))


def showApp():
    mw.kyoroApp = KyroWebView()
    mw.kyoroApp.show()
    mw.kyoroApp.setFocus()
    mw.kyoroApp.activateWindow()


KYORO_COMMAND_PREFIX = "Kyoro."


def myPyCmdHandler(handled: Tuple[bool, Any], message: str, context: Any):
    if not isinstance(context, KyroWebView):
        return handled
    if not message.startswith(KYORO_COMMAND_PREFIX):
        return handled
    cmd = message[len(KYORO_COMMAND_PREFIX):].strip()
    if cmd == "getLocalContentList":
        return (True, ["a", "b", "c"])
    return handled


gui_hooks.webview_did_receive_js_message.append(myPyCmdHandler)

# create a new menu item, "test"
action = QAction("Kyoro", mw)

# set it to call testFunction when it's clicked
action.triggered.connect(showApp)

# and add it to the tools menu
mw.form.menuTools.addAction(action)
