package com.kyoroteam.kyoro;

import ve.Pos;
import java.util.List;

public class Result {
    public Result(List<String> words, List<String> lemmas, List<String> readings) {
        Words = words;
        Lemmas = lemmas;
        Readings = readings;
    }

    public List<String> Words;
    public List<String> Lemmas;
    public List<String> Readings;
}
