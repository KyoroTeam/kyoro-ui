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
    {0}
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    {1}
  </body>
</html>
        """

        cssTemplate = "<style>{0}</style>"
        jsTemplate = "<script>{0}</script>"

        jsFiles = glob.glob(os.path.join(addon_path, "js/*"))
        cssFiles = glob.glob(os.path.join(addon_path, "css/*"))

        jsHtml = [jsTemplate.format(open(fileName).read()) for fileName in jsFiles]
        cssHtml = [cssTemplate.format(open(fileName).read()) for fileName in cssFiles]   

        self.stdHtml(html.format(jsHtml, cssHtml))

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
