from typing import *
from kyoro.content import KyoroContentManager
from kyoro.tokenizer import KuromojiJavaTokenizer

KYORO_COMMAND_PREFIX = "Kyoro."

# https://stackoverflow.com/a/1118038
# To use items in Anki's pycmd, all items needs be
# serializable with json.dumps(obj)
# Solution: Convert objects to a raw dict


def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


def make_pycmd_response(data: Any, error: Optional[str]):
    return (True, todict({"error": error, "result": data}))


def kyoro_pycmd_handler(handled: Tuple[bool, Any], message: str, context: Any):
    print("Kyoro Command -->", handled, message, context)

    if not message.startswith(KYORO_COMMAND_PREFIX):
        return handled

    cmds = message.split(":")
    cmd = cmds[0].strip()

    if cmd == "Kyoro.getCurrentIndexState":
        db = KyoroContentManager()
        json = db.get_current_content_info()
        return make_pycmd_response(json, None)
    elif cmd == "Kyoro.tokenizeOnDiskSource":
        sourceFilename = cmds[1].strip()
        tokenizer = KuromojiJavaTokenizer()
        json_string = tokenizer.tokenize_file_to_ky_json(sourceFilename)
        if json_string is None:
            return make_pycmd_response(None, "Failed to tokenize sentence")
        return make_pycmd_response(json_string, None)
    elif cmd == "Kyoro.getMinisearchIndexGzip":
        content = KyoroContentManager()
        index = content.get_current_minisearch_index_b64()
        return make_pycmd_response(index, None)

    return handled
