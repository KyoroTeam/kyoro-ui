package com.kyoroteam.kyoro.tokenizer.result;

import java.util.List;

import ve.Word;

public class KyoroJapaneseFeature {
    public KyoroJapaneseFeature(List<String> words, List<WordPosition> wordPositions, List<String> lemmas,
            List<String> readings, List<Word> veWords) {
        Words = words;
        WordPositions = wordPositions;
        Lemmas = lemmas;
        Readings = readings;
        VeWords = veWords;
    }

    public List<String> Words;
    public List<WordPosition> WordPositions;
    public List<String> Lemmas;
    public List<String> Readings;
    public transient List<Word> VeWords;
}
