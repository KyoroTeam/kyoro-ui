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

public class Handler implements RequestHandler<Map<String, String>, List<Result>> {
    @Override
    public List<Result> handleRequest(Map<String, String> event, Context context) {
        var builder = new Tokenizer.Builder();
        Tokenizer tokenizer = builder.mode(Mode.SEARCH).build();
        List<Token> tokens = tokenizer.tokenize(event.get("request"));

        var parser = new ve.Parse(tokens.toArray(new Token[0]));  
        var words = parser.words();

        var resultList = words.stream()
            .filter(r -> !r.getPart_of_speech().equals(Pos.Postposition) && !r.getPart_of_speech().equals(Pos.Symbol))
            .filter(r -> !r.getLemma().equals("*"))
            .map(r -> new Result(r.getPart_of_speech(), r.toString(), r.getLemma(), r.getReading()))
            .collect(Collectors.toList());

        return resultList;
    }
}