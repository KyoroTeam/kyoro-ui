package com.kyoroteam.kyoro;

import com.atilika.kuromoji.TokenizerBase.Mode;
import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.ipadic.Tokenizer;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import java.util.List;
import java.util.Map;
import java.util.stream.*;

public class Handler implements RequestHandler<Map<String, String>, List<Result>> {
    @Override
    public List<Result> handleRequest(Map<String, String> event, Context context) {
        var builder = new Tokenizer.Builder();
        Tokenizer tokenizer = builder.mode(Mode.SEARCH).build();
        // Tokenizer tokenizer = new Tokenizer();
        List<Token> tokens = tokenizer.tokenize(event.get("request"));

        // 助動詞: (ex: tai in tabetai) should be grouped with the previous verb
        // 副詞: Add support for adjectives
        // 非自立 nouns should be filtered (e.g, you)

        var resultList = tokens.stream()
            .filter(r -> r.getPartOfSpeechLevel1().equals("動詞") || r.getPartOfSpeechLevel1().equals("名詞"))
            .map(token -> new Result(token.getPartOfSpeechLevel1().equals("動詞") ? PartOfSpeach.VERB : PartOfSpeach.NOUN,
                    token.getBaseForm(), token.getSurface(), token.getPronunciation(), token.getAllFeatures()))
            .collect(Collectors.toList());

        return resultList;
    }
}