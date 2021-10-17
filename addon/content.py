from typing import *
import os

from database import IKyoroDatabase

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


class KyContentInfo:
    def __init__(self, name: str, filetype: str, is_supported: bool) -> None:
        self.name = name
        self.filetype = filetype
        self.is_supported = is_supported


class KyoroContentManager:
    SUPPORTED_FILE_EXTENSIONS = ["pdf", "docx", "txt", "json"]

    def __init__(self, db: IKyoroDatabase) -> None:
        self.db = db
        pass

    # Return some information about all the current existing files
    # in the content directory
    def get_current_content_info() -> List[KyContentInfo]:
        result: List[KyContentInfo] = []
        for file in os.listdir(files_path):
            split = os.path.splitext(file)
            ext = "none" if split[1] == "" else split[1]
            supported = ext in KyoroContentManager.SUPPORTED_FILE_EXTENSIONS
            result.append(KyContentInfo(file, ext, supported))
        return result
