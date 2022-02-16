import base64
from types import SimpleNamespace
from typing import *
import os
import json
from pathlib import Path

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


class IKyContentInfo:
    def __init__(self, name: str, index_state: str):
        self.name: str = name
        self.index_state: str = index_state


class IKyIndexJson:
    def __init__(self, filename: str, last_modified_time: float) -> None:
        self.filename: str = filename
        self.last_modified_time: float = last_modified_time


class KyoroContentManager:
    SUPPORTED_FILE_EXTENSIONS = ["pdf", "docx", "txt", "json"]

    # Return some information about all the current existing files
    # in the content directory
    def get_current_content_info(self) -> List[IKyContentInfo]:
        files_now = self._index_to_dict(self._index_contect_directory())
        files_last_known = self._index_to_dict(self._load_current_index_json())

        result: List[IKyContentInfo] = []
        for filename, ky_file in files_now.items():
            indexed_state = "not-indexed"
            if filename in files_last_known:
                indexed_file = files_last_known[filename]
                if ky_file.last_modified_time == indexed_file.last_modified_time:
                    indexed_state = "fully-indexed"
                else:
                    indexed_state = "needs-reindex"
            result.append(IKyContentInfo(filename, indexed_state))
        return result

    def get_current_minisearch_index_b64(self) -> str:
        with open(os.path.join(files_path, "minisearch_index.json.gz"), "rb") as f:
            bytes = f.read()
            return base64.b64encode(bytes).decode("utf-8")

    def _load_current_index_json(self) -> List[IKyIndexJson]:
        filename = os.path.join(files_path, "index_stats.json")
        index_file = Path(filename)
        if index_file.is_file():
            with open(filename, "r") as f:
                return json.load(f, object_hook=lambda obj: SimpleNamespace(**obj))
        return []

    def _index_contect_directory(self) -> List[IKyIndexJson]:
        result: List[IKyIndexJson] = []
        with os.scandir(files_path) as entries:
            result = list(map(lambda e: IKyIndexJson(
                e.name, e.stat().st_mtime), entries))
        return result

    def _index_to_dict(self, items: Iterable[IKyIndexJson]) -> Dict[str, IKyIndexJson]:
        return { item.filename: item for item in items }
