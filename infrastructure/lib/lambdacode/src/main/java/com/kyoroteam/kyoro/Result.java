package com.kyoroteam.kyoro;
import ve.Pos;

public class Result {
    public Result(Pos partOfSpeeach, String word, String lemma, String reading) {
        PartOfSpeeach = partOfSpeeach;
        Word = word;
        Lemma = lemma;
        Reading = reading;
    }
    public Pos PartOfSpeeach;
    public String Word;
    public String Lemma;
    public String Reading;
}
