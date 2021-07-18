from typing import *
from aqt.webview import AnkiWebView
# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import all of the Qt GUI library
from aqt.qt import *
import aqt
import io
import os
import json

addon_path = os.path.dirname(__file__)

# Migaku doing something with ogAnkiWebBridge ? Blocking commands?


class KyroWebView(QDialog):
    # Set for registering dialogs
    silentlyClose = True

    def __init__(self, mw: aqt.AnkiQt) -> None:
        QDialog.__init__(self)
        print("init")
        self.mw = mw
        self.web = mw.web
        self.show()

        w = AnkiWebView(title="browser card info")
        w.set_bridge_command(self.kyoro_pycmd_handler, self)

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

    def kyoro_pycmd_handler(message: str, context: Any):
        pass

    # def show(self):
    #     self.web.set_bridge_command(self.kyoro_pycmd_handler, self)
    #     self.web.show()
    #     self.web.setFocus()
    #     self.web.activateWindow()


def showApp():
    aqt.dialogs.open("Kyoro", mw)


KYORO_COMMAND_PREFIX = "Kyoro."

# Kyoro.getTokenizedSentences:a


def loadJson() -> List[Any]:
    with open(os.path.join(addon_path, "all_v11_out.json"), "r") as f:
        return json.loads(f.read())


items = loadJson()


def kyoro_pycmd_handler(handled: Tuple[bool, Any], message: str, context: Any):
    print("OK...", handled, message, context)
    # if not isinstance(context, KyroWebView):
    #     print("1 Not OK...")
    #     return handled
    if not message.startswith(KYORO_COMMAND_PREFIX):
        print("2 OK...")
        return handled
    cmds = message.split(":")
    cmd = cmds[0].strip()
    print("3 OK...", cmds)
    if cmd == "Kyoro.getLocalContentList":
        results = list(set(map(lambda s: s["Source"], items)))
        print("4 OK...", results)
        return (True, results)
    elif cmd == "Kyoro.getTokenizedSentences":
        contentName = cmds[1].strip()
        results = filter(lambda s: s["Source"] == contentName, items)
        print("5 OK...", results)
        return (True, results)
    print("6 OK...")
    return handled


gui_hooks.webview_did_receive_js_message.append(kyoro_pycmd_handler)

# Register a new dialog for us
aqt.dialogs.register_dialog("Kyoro", KyroWebView)

# create a new menu item, "test"
action = QAction("Kyoro", mw)

# set it to call testFunction when it's clicked
action.triggered.connect(showApp)

# and add it to the tools menu
mw.form.menuTools.addAction(action)
