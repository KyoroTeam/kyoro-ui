package com.kyoroteam.kyoro;

import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.ipadic.Tokenizer;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        Tokenizer tokenizer = new Tokenizer();
        List<Token> tokens = tokenizer.tokenize("猫はお寿司が食べたい。");
        for (Token token : tokens) {
            System.out.println(token.getBaseForm() + "\t" + token.getAllFeatures());
        }
        System.out.println("Hello World!");
    }
}
