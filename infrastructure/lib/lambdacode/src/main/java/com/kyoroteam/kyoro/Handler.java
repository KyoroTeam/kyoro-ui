package com.kyoroteam.kyoro;

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
        // Gson gson = new GsonBuilder().setPrettyPrinting().create();
        LambdaLogger logger = context.getLogger();

        logger.log("Function name: " + context.getFunctionName());

        Tokenizer tokenizer = new Tokenizer();
        List<Token> tokens = tokenizer.tokenize(event.get("request"));

        for (Token token : tokens) {
            logger.log(token.getBaseForm() + "\t" + token.getAllFeatures());
        }

        var resultList = tokens.stream()
                .filter(r -> r.getPartOfSpeechLevel1() == "動詞" || r.getPartOfSpeechLevel1() == "名詞")
                .map(token -> new Result(token.getPartOfSpeechLevel1() == "動詞" ? PartOfSpeach.VERB : PartOfSpeach.NOUN,
                        token.getBaseForm(), token.getConjugationForm(), token.getPronunciation()))
                .collect(Collectors.toList());

        return resultList;
    }
}