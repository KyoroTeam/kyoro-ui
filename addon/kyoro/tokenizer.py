from types import SimpleNamespace
import subprocess
import json
import os
from typing import List, Optional

addon_path = os.path.dirname(__file__)
files_path = os.path.join(addon_path, "content")


class KyWordPosition:
    def __init__(self) -> None:
        self.Start = 0
        self.End = 0


class KyJapaneseFeatures:
    def __init__(self) -> None:
        self.Words: List[str] = []
        self.WordPositions: List[KyWordPosition] = []
        self.Lemmas: List[str] = []
        self.Readings: List[str] = []


class KyJapaneseSentence:
    def __init__(self) -> None:
        self.Sentence = ""
        self.Translation = ""
        self.Features = KyJapaneseFeatures()


class KyTokenizeResult:
    def __init__(self) -> None:
        self.Source = ""
        self.Sentences: List[KyJapaneseSentence] = []


class KuromojiJavaTokenizer:
    def tokenize_file(self, filename: str) -> Optional[KyTokenizeResult]:
        json_results = self.tokenize_file_to_ky_json(filename)
        if json_results is not None:
            x = json.loads(
                json_results, object_hook=lambda obj: SimpleNamespace(**obj))
            return x

    def tokenize_file_to_ky_json(self, filename: str) -> Optional[str]:
        result = subprocess.run(
            [
                "java",
                "-jar",
                "/home/james/Desktop/Git/kyoro-ui/tokenizer/target/kuromoji-tokenizer-1.0-SNAPSHOT.jar",
                os.path.join(files_path, filename)
            ],
            capture_output=True)
        if result.returncode == 0:
            json_results = result.stdout
            return json_results
        else:
            print("Oh no")
            return None


if __name__ == '__main__':
    print(1 + 1)
