from typing import *
from kyoro.content import KyoroContentManager
from kyoro.tokenizer import KuromojiJavaTokenizer

KYORO_COMMAND_PREFIX = "Kyoro."


def kyoro_pycmd_handler(handled: Tuple[bool, Any], message: str, context: Any):
    print("Kyoro Command -->", handled, message, context)

    if not message.startswith(KYORO_COMMAND_PREFIX):
        return handled

    cmds = message.split(":")
    cmd = cmds[0].strip()

    if cmd == "Kyoro.getCurrentIndexState":
        db = KyoroContentManager()
        json = db.get_current_content_info()
        return (True, json)
    elif cmd == "Kyoro.tokenizeOnDiskSource":
        sourceFilename = cmds[1].strip()
        tokenizer = KuromojiJavaTokenizer()
        json_string = tokenizer.tokenize_file_to_ky_json(sourceFilename)
        if json_string is None:
            return (True, {"error": "Failed to parse file.", "success": False})
        return (True, {"error": "Failed to write to database. Check error log.", "success": True})
    elif cmd == "Kyoro.getMinisearchIndexGzip":
        content = KyoroContentManager()
        index = content.get_current_minisearch_index_b64()
        return (True, index)

    return handled
