package com.kyoroteam.kyoro.tokenizer;

import java.util.List;

import ve.Word;

public class KyoroTokenizeResult {
    public KyoroTokenizeResult(String source, String sentence, String translation, List<String> words,
            List<WordPosition> wordPositions, List<String> lemmas, List<String> readings, List<Word> veWords) {
        Source = source;
        Sentence = sentence;
        Translation = translation;
        Words = words;
        WordPositions = wordPositions;
        Lemmas = lemmas;
        Readings = readings;
        VeWords = veWords;
    }

    public String Source;
    public String Sentence;
    public String Translation;
    public List<String> Words;
    public List<WordPosition> WordPositions;
    public List<String> Lemmas;
    public List<String> Readings;
    public List<Word> VeWords;
}
