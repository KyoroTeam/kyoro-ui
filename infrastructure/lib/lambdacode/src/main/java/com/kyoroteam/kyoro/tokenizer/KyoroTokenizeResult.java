package com.kyoroteam.kyoro.tokenizer;

import java.util.List;

public class KyoroTokenizeResult {
    public KyoroTokenizeResult(String source, String sentence, String translation, List<String> words,
            List<WordPosition> wordPositions, List<String> lemmas, List<String> readings) {
        Source = source;
        Sentence = sentence;
        Translation = translation;
        Words = words;
        WordPositions = wordPositions;
        Lemmas = lemmas;
        Readings = readings;
    }

    public String Source;
    public String Sentence;
    public String Translation;
    public List<String> Words;
    public List<WordPosition> WordPositions;
    public List<String> Lemmas;
    public List<String> Readings;
}
