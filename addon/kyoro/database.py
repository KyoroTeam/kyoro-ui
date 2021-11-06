from sqlite3.dbapi2 import Connection
import sqlite3
from typing import List, Tuple
import time
import os

from .tokenizer import KyTokenizeResult, KuromojiJavaTokenizer

addon_path = os.path.dirname(__file__)


class KyoroDatabase:
    DEFALT_DB_PATH = "content.db"

    def __init__(self) -> None:
        path = os.path.join(addon_path, KyoroDatabase.DEFALT_DB_PATH)
        self.sqlite = self._create_or_open_db(path)

    def get_indexed_source_names(self) -> List[Tuple[str, int, float]]:
        cursor = self.sqlite.cursor()
        cursor.execute(
            "select source_name, ky_source_tid, sql_modified_datetime from ky_source")
        return cursor.fetchall()

    def get_sentences_for_source(self, source_tid: int) -> KyTokenizeResult:
        cursor = self.sqlite.cursor()
        cursor.execute(
            """
            select
                s.sentence_text,
                f.feature,
                f.feature_order_index
            from ky_sentence_feature f
            inner join ky_sentence s on s.ky_sentence_tid = f.ky_sentence_tid
            inner join ky_source src on src.ky_source_tid = s.ky_source_tid
            where src.ky_source_tid = ?
            """,
            (source_tid,)
        )
        pass

    def update_source_sentences(self, content: KyTokenizeResult) -> bool:
        try:
            cursor = self.sqlite.cursor()
            now = time.time()

            # Ensure existence of source
            source_tid = None
            cursor.execute(
                "select ky_source_tid from ky_source where source_name = (?)", (content.Source,))
            fetch = cursor.fetchone()
            if fetch is not None:
                source_tid = fetch[0]
            else:
                cursor.execute(
                    "insert into ky_source (sql_created_datetime, source_name) values (?, ?)", (now, content.Source))
                source_tid = cursor.lastrowid

            for sentence in content.Sentences:
                # Inser the sentence and get the new ID
                cursor.execute(
                    """
                    insert into ky_sentence (ky_source_tid, sql_created_datetime, sentence_text)
                    values (?, ?, ?)
                    """, (source_tid, now, sentence.Sentence))
                sentence_tid = cursor.lastrowid

                # Combine the sentence features into one array and insert at once
                # (feature_type, feature, feature_index)
                all_features = list[Tuple[str, str, int]]([])
                all_features.extend(
                    [("jp_word", w, i) for (i, w) in enumerate(sentence.Features.Words)])
                all_features.extend(
                    [("jp_lemma", l, i) for (i, l) in enumerate(sentence.Features.Lemmas)])
                all_features.extend(
                    [("jp_reading", r, i) for (i, r) in enumerate(sentence.Features.Readings)])
                all_features.extend(
                    [("jp_word_position", f"{wp.Start},{wp.End}", i) for (i, wp) in enumerate(sentence.Features.WordPositions)])

                insert = [(now,
                           sentence_tid,
                           feature[1],
                           feature[0],
                           feature[2]) for feature in all_features]

                cursor.executemany(
                    """
                    insert into ky_sentence_feature (
                        sql_created_datetime,
                        ky_sentence_tid,
                        feature,
                        feature_type,
                        feature_order_index)
                    values (?, ?, ?, ?, ?)
                    """, insert)

            self.sqlite.commit()
            return True
        except Exception as e:
            self._insert_error_log(str(e))
            return False

    def _insert_error_log(self, error: str) -> None:
        try:
            now = time.time()
            cursor = self.sqlite.cursor()
            cursor.execute(
                "insert into ky_error_log (sql_created_datetime, error_text) values (?,?)", (now, error))
            self.sqlite.commit()
        except Exception as e:
            print(f"Couldn't write error log: {error} ({str(e)})")

    def _create_or_open_db(self, path: str) -> Connection:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(
            "select null from sqlite_master where type = 'table' and name = 'ky_source'")
        fetch = cur.fetchone()
        if fetch is None:
            with open(os.path.join(addon_path, "sql", "schema_1.sql")) as f:
                c = f.read()
            cur.executescript(c)
            con.commit()
        return con


if __name__ == '__main__':
    tokenizer = KuromojiJavaTokenizer()
    results = tokenizer.tokenize_file("/home/james/Desktop/datasmall.txt")
    db = KyoroDatabase()
    db.update_source_sentences(results)
