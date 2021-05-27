package com.kyoroteam.kyoro;

import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.ipadic.Tokenizer;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;

/**
 * Hello world!
 *
 */
public class Handler implements RequestHandler<Map<String, String>, ArrayList<String[]>> {
    @Override
    public ArrayList<String[]> handleRequest(Map<String, String> event, Context context) {
        // Gson gson = new GsonBuilder().setPrettyPrinting().create();
        LambdaLogger logger = context.getLogger();

        logger.log("Function name: " + context.getFunctionName());

        Tokenizer tokenizer = new Tokenizer();
        List<Token> tokens = tokenizer.tokenize(event.get("request"));

        var results = new ArrayList<String[]>();
        for (Token token : tokens) {
            results.add(token.getAllFeaturesArray());
            logger.log(token.getBaseForm() + "\t" + token.getAllFeatures());
        }

        return results;
    }
}