package com.kyoroteam.kyoro.tokenizer.result;

public class KyoroJapaneseSentence {
    public KyoroJapaneseSentence(String sentence, String translation, KyoroJapaneseFeature features) {
        Sentence = sentence;
        Translation = translation;
        Features = features;
    }

    public String Sentence;
    public String Translation;
    public KyoroJapaneseFeature Features;
}
