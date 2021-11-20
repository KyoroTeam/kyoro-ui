from ..kyoro.database import KyoroDatabase
from ..kyoro.tokenizer import KuromojiJavaTokenizer


def test_works():
    tokenizer = KuromojiJavaTokenizer()
    tokens = tokenizer.tokenize_file("/home/james/Desktop/datasmall.txt")
    db = KyoroDatabase(":memory:")
    result = db.update_source_sentences(tokens)
    assert result == True
