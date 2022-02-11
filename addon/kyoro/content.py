import base64
from typing import *
import os

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


class KyContentInfo:
    def __init__(self, name: str, filetype: str, is_supported: bool):
        self.name = name
        self.filetype = filetype
        self.is_supported = is_supported


class KyoroContentManager:
    SUPPORTED_FILE_EXTENSIONS = ["pdf", "docx", "txt", "json"]

    # Return some information about all the current existing files
    # in the content directory
    def get_current_content_info(self) -> List[KyContentInfo]:
        result: List[KyContentInfo] = []
        for file in os.listdir(files_path):
            split = os.path.splitext(file)
            ext = "none" if split[1] == "" else split[1]
            supported = ext in KyoroContentManager.SUPPORTED_FILE_EXTENSIONS
            result.append(KyContentInfo(file, ext, supported))
        print(str(result))
        return result

    def get_current_search_index_b64(self) -> str:
        with open(os.path.join(files_path, "minisearch_index.json.gz"), "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode("utf-8")
            return b64
