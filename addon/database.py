from enum import Enum
import sqlite3
from abc import abstractmethod
from typing import List, Tuple

from tokenizer import KyTokenizeResult


class IKyoroDatabase:
    @abstractmethod
    def get_indexed_source_names() -> List[str]:
        pass

    @abstractmethod
    def get_sentences_for_source(this, source_name: str) -> List[KyTokenizeResult]:
        pass

    @abstractmethod
    def update_source_sentences(this, source_name: str, content: List[KyTokenizeResult]):
        pass


class KyFeatureTid(Enum):
    WORD = 0,
    LEMMA = 1,
    WORDPOSITION = 2,
    READING = 3


class KyoroDatabase(IKyoroDatabase):
    def __init__(self, con: sqlite3.Connection) -> None:
        self.sqlite = con
        pass

    def get_indexed_source_names(self) -> List[Tuple[str, int]]:
        cursor = self.sqlite.cursor()
        cursor.execute("select source_name, ky_source_tid from ky_source")
        return cursor.fetchall()

    def get_sentences_for_source(self, source_tid: int) -> List[KyTokenizeResult]:
        cursor = self.sqlite.cursor()
        cursor.execute(
            """
            select 
                s.sentence,
                f.feature, 
                f.feature_order_index 
            from ky_sentence_feature f
            inner join ky_sentence s on s.ky_sentence_tid = f.ky_sentence_tid
            inner join ky_source src on src.ky_souce_tid = s.ky_souce_tid
            where src.ky_source_tid = ?
            """,
            source_tid
        )
        pass

    def update_source_sentences(self, source_name: str, content: KyTokenizeResult):
        pass
