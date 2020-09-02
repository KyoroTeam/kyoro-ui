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
        with open(os.path.join(addon_path, "app.js"), "r") as f:
            appContents = f.read()
        style = """
html, body {
    position: relative;
    width: 100%;
    height: 100%;
}

body {
    color: #333;
    margin: 0;
    padding: 8px;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
}

a {
    color: rgb(0,100,200);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

a:visited {
    color: rgb(0,80,160);
}

label {
    display: block;
}

input, button, select, textarea {
    font-family: inherit;
    font-size: inherit;
    -webkit-padding: 0.4em 0;
    padding: 0.4em;
    margin: 0 0 0.5em 0;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 2px;
}

input:disabled {
    color: #ccc;
}

button {
    color: #333;
    background-color: #f4f4f4;
    outline: none;
}

button:disabled {
    color: #999;
}

button:not(:disabled):active {
    background-color: #ddd;
}

button:focus {
    border-color: #666;
}
"""

        html = """
<script defer>
{0}
</script>
<style>
{1}
</style>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width,initial-scale=1'>

    <title>Svelte app</title>

    <link rel='icon' type='image/png' href='/favicon.png'>
    <link rel='stylesheet' href='/global.css'>
    <link rel='stylesheet' href='/build/bundle.css'>
</head>

<body>
</body>
</html>
        """.format(appContents, style)
        self.stdHtml(html)


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
