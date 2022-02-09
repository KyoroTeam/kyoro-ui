from typing import *
from kyoro.content import KyoroContentManager
from kyoro.tokenizer import KuromojiJavaTokenizer
from kyoro.database import KyoroDatabase

KYORO_COMMAND_PREFIX = "Kyoro."


def kyoro_pycmd_handler(handled: Tuple[bool, Any], message: str, context: Any):
    print("Kyoro Command -->", handled, message, context)

    if not message.startswith(KYORO_COMMAND_PREFIX):
        return handled

    cmds = message.split(":")
    cmd = cmds[0].strip()

    if cmd == "Kyoro.getIndexedSources":
        db = KyoroDatabase()
        tokens = db.get_indexed_source_names()
        return (True, tokens)
    elif cmd == "Kyoro.getTokenizedSentences":
        sourceTidStr = cmds[1].strip()
        sounceTid = int(sourceTidStr)
        db = KyoroDatabase()
        tokens = db.get_sentences_for_source(sounceTid)
        return (True, tokens)
    elif cmd == "Kyoro.getOnDiskSources":
        content = KyoroContentManager()
        tokens = content.get_current_content_info()
        return (True, tokens)
    elif cmd == "Kyoro.tokenizeOnDiskSource":
        sourceTidStr = cmds[1].strip()
        tokenizer = KuromojiJavaTokenizer()
        tokens = tokenizer.tokenize_file(sourceTidStr)
        if tokens is None:
            return (True, {"err": "Failed to parse file.", "success": False})
        db = KyoroDatabase()
        if db.update_source_sentences(tokens) == False:
            return (True, {"err": "Failed to write to database. Check error log.", "success": False})
        return (True, {"err": None, "success": True})
    elif cmd == "Kyoro.getMinisearchIndexGzip":
        content = KyoroContentManager()
        index = content.get_current_search_index_b64()
        print(len(index))
        return (True, index)
        pass

    return handled
