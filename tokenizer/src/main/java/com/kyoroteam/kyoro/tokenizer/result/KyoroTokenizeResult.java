package com.kyoroteam.kyoro.tokenizer.result;

import java.util.List;

public class KyoroTokenizeResult {
    public KyoroTokenizeResult(String source, List<KyoroJapaneseSentence> sentences) {
        Source = source;
        Sentences = sentences;
    }

    public String Source;
    public List<KyoroJapaneseSentence> Sentences;
}
