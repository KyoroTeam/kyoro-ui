from typing import *
from aqt.webview import AnkiWebView
# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import all of the Qt GUI library
from aqt.qt import *
import os
import json
from command_processor import kyoro_pycmd_handler

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


class KyroWebView(QScrollArea):
    def __init__(self) -> None:
        QScrollArea.__init__(self)

        w = AnkiWebView(title="browser card info")
        # w.set_bridge_command(self.kyoro_pycmd_handler, self)

        l = QVBoxLayout()
        l.setContentsMargins(0, 0, 0, 0)
        l.addWidget(w)

        self.setLayout(l)

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

        w.stdHtml(html.format(js, css))

        self.show()


mw.kyoro = None


def showApp():
    if not mw.kyoro:
        mw.kyoro = KyroWebView()
    mw.kyoro.show()
    if mw.kyoro.windowState() == Qt.WindowMinimized:
        # Window is minimised. Restore it.
        mw.kyoro.setWindowState(Qt.WindowNoState)
    mw.kyoro.setFocus()
    mw.kyoro.activateWindow()


def loadJson() -> List[Any]:
    with open(os.path.join(addon_path, "all_v11_out.json"), "r") as f:
        return json.loads(f.read())


gui_hooks.webview_did_receive_js_message.append(kyoro_pycmd_handler)

# create a new menu item, "test"
action = QAction("Kyoro", mw)

# set it to call testFunction when it's clicked
action.triggered.connect(showApp)

# and add it to the tools menu
mw.form.menuTools.addAction(action)
