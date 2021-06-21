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

import ve.Pos;

public class Handler implements RequestHandler<Map<String, String>, Result> {
    @Override
    public Result handleRequest(Map<String, String> event, Context context) {
        var builder = new Tokenizer.Builder();
        Tokenizer tokenizer = builder.mode(Mode.SEARCH).build();
        List<Token> tokens = tokenizer.tokenize(event.get("request"));

        var parser = new ve.Parse(tokens.toArray(new Token[0]));
        var words = parser.words();

        var resultList = words.stream()
                .filter(r -> !r.getPart_of_speech().equals(Pos.Postposition)
                        && !r.getPart_of_speech().equals(Pos.Symbol) && !r.getPart_of_speech().equals(Pos.Prefix))
                .filter(r -> !r.getLemma().equals("*")).collect(Collectors.toList());

        var words2 = resultList.stream().map(r -> r.getWord()).collect(Collectors.toList());
        var lemmas = resultList.stream().map(r -> r.getLemma()).collect(Collectors.toList());
        var readings = resultList.stream().map(r -> r.getReading()).collect(Collectors.toList());

        var result = new Result(words2, lemmas, readings);

        return result;
    }
}