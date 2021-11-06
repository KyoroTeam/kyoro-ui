from ..kyoro.database import KyoroDatabase
from ..kyoro.tokenizer import KuromojiJavaTokenizer


def test_works():
    tokenizer = KuromojiJavaTokenizer()
    results = tokenizer.tokenize_file("/home/james/Desktop/datasmall.txt")
    db = KyoroDatabase()
    db.update_source_sentences(results)
