package com.kyoroteam.kyoro;

import java.util.List;

public class KyoroTokenizeResult {
    public KyoroTokenizeResult(String sentence, List<String> words, List<String> lemmas, List<String> readings) {
        Sentence = sentence;
        Words = words;
        Lemmas = lemmas;
        Readings = readings;
    }

    public String Sentence;
    public List<String> Words;
    public List<String> Lemmas;
    public List<String> Readings;
}
