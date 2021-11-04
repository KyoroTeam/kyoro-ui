from types import SimpleNamespace
import subprocess
import json
from typing import List


class KyWordPosition:
    def __init__(self) -> None:
        self.Start = 0
        self.End = 0


class KyJapaneseFeatures:
    def __init__(self) -> None:
        self.Words = List[str]([])
        self.WordPositions = List[KyWordPosition]([])
        self.Lemmas = List[str]([])
        self.Readings = List[str]([])


class KyJapaneseSentence:
    def __init__(self) -> None:
        self.Sentence = ""
        self.Translation = ""
        self.Features = KyJapaneseFeatures()


class KyTokenizeResult:
    def __init__(self) -> None:
        self.Source = ""
        self.Sentences = List[KyJapaneseSentence]([])


class KuromojiJavaTokenizer:
    def tokenize_file(self, filename: str) -> KyTokenizeResult:
        result = subprocess.run(
            ["java", "-jar", "/home/james/Desktop/Git/kyoro-ui/tokenizer/target/kuromoji-tokenizer-1.0-SNAPSHOT.jar", filename], capture_output=True)
        if result.returncode == 0:
            json_results = result.stdout
            x = json.loads(
                json_results, object_hook=lambda obj: SimpleNamespace(**obj))
            return x
        else:
            print("Oh no")
            return []
