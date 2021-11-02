from tokenizer import KyTokenizeResult
import sqlite3
from typing import List, Tuple
import time


class KyoroDatabase:
    def __init__(self, path: str) -> None:
        self.sqlite = self._create_or_open_db(path)
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

    def update_source_sentences(self, content: KyTokenizeResult):
        cursor = self.sqlite.cursor()
        now = time.time()

        # Ensure existence of source
        source_tid = None
        result = cursor.execute(
            "select ky_source_tid from ky_source where source_name = (?)", content.Source)
        if len(result) > 0:
            source_tid = result.fetchone()[0]
        if len(result) == 0:
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
            all_features = List[Tuple[str, str]]([])  # (feature_type, feature)
            all_features.append(
                [("jp_word", w) for w in sentence.Features.Words])
            all_features.append(
                [("jp_lemma", l) for l in sentence.Features.Lemmas])
            all_features.append(
                [("jp_reading", r) for r in sentence.Features.Readings])
            all_features.append(
                [("jp_word_position", f"{wp.Start},{wp.End}") for wp in sentence.Features.WordPositions])

            insert = [(now, sentence_tid, feature[1][1], feature[1][0], feature[0])
                      for feature in enumerate(all_features)]

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

    def _create_or_open_db(self, path: str):
        con = sqlite3.connect(path)
        is_created_test = con.execute(
            "select null from sqlite_master where type = 'table' and name = 'ky_source'")
        if len(is_created_test) == 0:
            with open(path.join("sql", "schema_1.sql")) as f:
                c = f.read()
            con.execute(c)
        return con
