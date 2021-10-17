import sqlite3
from abc import abstractmethod
from typing import List

from tokenizer import KyTokenizeResult


class IKyoroDatabase:
    @abstractmethod
    def get_index_source_names() -> List[str]:
        pass

    @abstractmethod
    def get_sentences_for_source(this, source_name: str) -> List[KyTokenizeResult]:
        pass

    @abstractmethod
    def update_source_sentences(this, source_name: str, content: List[KyTokenizeResult]):
        pass


class KyoroDatabase(IKyoroDatabase):
    def __init__(self, con: sqlite3.Connection) -> None:
        pass

    def get_index_source_names() -> List[str]:
        pass

    def get_sentences_for_source(this, source_name: str) -> List[KyTokenizeResult]:
        pass

    def update_source_sentences(this, source_name: str, content: List[KyTokenizeResult]):
        pass
