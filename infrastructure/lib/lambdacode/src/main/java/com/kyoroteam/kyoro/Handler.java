package com.kyoroteam.kyoro;

import com.atilika.kuromoji.TokenizerBase.Mode;
import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.ipadic.Tokenizer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.*;
import com.worksap.nlp.sudachi.sentdetect.*;

import ve.Pos;

public class Handler implements RequestHandler<Map<String, String>, List<KyoroTokenizeResult>> {
    @Override
    public List<KyoroTokenizeResult> handleRequest(Map<String, String> event, Context context) {
        var builder = new Tokenizer.Builder();
        var tokenizer = builder.mode(Mode.SEARCH).build();
        var sentences = SplitSentences(event.get("request"));
        var results = sentences.stream().map(s -> TokenizeSentence(tokenizer, s)).collect(Collectors.toList());
        return results;
    }

    private KyoroTokenizeResult TokenizeSentence(Tokenizer tokenizer, String niceSentence) {
        List<Token> tokens = tokenizer.tokenize(niceSentence);

        var parser = new ve.Parse(tokens.toArray(new Token[0]));
        var words = parser.words();

        var resultList = words.stream()
                .filter(r -> !r.getPart_of_speech().equals(Pos.Postposition)
                        && !r.getPart_of_speech().equals(Pos.Symbol) && !r.getPart_of_speech().equals(Pos.Prefix))
                .filter(r -> !r.getLemma().equals("*")).collect(Collectors.toList());

        var words2 = resultList.stream().map(r -> r.getWord()).collect(Collectors.toList());
        var lemmas = resultList.stream().map(r -> r.getLemma()).collect(Collectors.toList());
        var readings = resultList.stream().map(r -> r.getReading()).collect(Collectors.toList());

        return new KyoroTokenizeResult(niceSentence, words2, lemmas, readings);
    }

    private List<String> SplitSentences(String crazyText) {
        var x = new SentenceDetector();
        int end = 0;
        var list = new ArrayList<String>();
        while ((end = x.getEos(crazyText, null)) != 0) {
            String sentence = crazyText.substring(0, end);
            crazyText = crazyText.substring(end);
            list.add(sentence);
        }
        return list;
    }
}