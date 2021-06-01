package com.kyoroteam.kyoro;

public class Result {
    public Result(PartOfSpeach partOfSpeeach, String dictionaryForm, String conjugatedForm, String pronounciation) {
        PartOfSpeeach = partOfSpeeach;
        DictionaryForm = dictionaryForm;
        ConjugatedForm = conjugatedForm;
        Pronounciation = pronounciation;
    }

    public PartOfSpeach PartOfSpeeach;
    public String DictionaryForm;
    public String ConjugatedForm;
    public String Pronounciation;
}
