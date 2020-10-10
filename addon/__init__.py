from anki import hooks
from aqt.webview import AnkiWebView
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
import io
import os

addon_path = os.path.dirname(__file__)


class KyroWebView(AnkiWebView):
    def __init__(self):
        AnkiWebView.__init__(self, title="Kyoro")

        with open(os.path.join(addon_path, "bundle.js"), "r") as f:
            appContents = f.read()
        with open(os.path.join(addon_path, "bundle.css"), "r") as f:
            appCss = f.read()
        with open(os.path.join(addon_path, "carbon.css"), "r") as f:
            carbonCss = f.read()

        html = """
            <script defer>{0}</script>
            <style>{1}</style>
            <style>{2}</style>
            <!DOCTYPE html><body></body></html>
        """.format(appContents, appCss, carbonCss)

        self.stdHtml(
            html, css=["all.css"])


def showApp():
    mw.kyoroApp = KyroWebView()
    mw.kyoroApp.show()
    mw.kyoroApp.setFocus()
    mw.kyoroApp.activateWindow()


# create a new menu item, "test"
action = QAction("Kyoro", mw)

# set it to call testFunction when it's clicked
action.triggered.connect(showApp)

# and add it to the tools menu
mw.form.menuTools.addAction(action)
