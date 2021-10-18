package com.kyoroteam.kyoro.tokenizer;

import com.atilika.kuromoji.TokenizerBase.Mode;
import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.ipadic.Tokenizer;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.*;
import com.worksap.nlp.sudachi.sentdetect.*;

import ve.Pos;
import ve.Word;

public class KyoroTokenizer {
    private Tokenizer Tokenizer;

    public KyoroTokenizer() {
        var builder = new Tokenizer.Builder();
        Tokenizer = builder.mode(Mode.SEARCH).build();
    }

    public List<KyoroTokenizeResult> tokenize(Request request) {
        var sentences = SplitSentences(request.jap);

        var results = sentences.stream().map(s -> TokenizeSentence(request.source, request.eng, s))
                .collect(Collectors.toList());

        return results;
    }

    private KyoroTokenizeResult TokenizeSentence(String source, String translation, String niceSentence) {
        List<Token> tokens = Tokenizer.tokenize(niceSentence);

        var parser = new ve.Parse(tokens.toArray(new Token[0]));
        var words = parser.words();

        var resultList = words.stream()
                .filter(r -> !r.getPart_of_speech().equals(Pos.Postposition)
                        && !r.getPart_of_speech().equals(Pos.Symbol) && !r.getPart_of_speech().equals(Pos.Prefix))
                .filter(r -> !r.getLemma().equals("*")).collect(Collectors.toList());

        var words2 = resultList.stream().map(r -> r.getWord()).collect(Collectors.toList());
        var lemmas = resultList.stream().map(r -> r.getLemma()).collect(Collectors.toList());
        var readings = resultList.stream().map(r -> r.getReading()).collect(Collectors.toList());
        var wordPositions = resultList.stream().map(word -> GetPositionsOfWord(word)).collect(Collectors.toList());

        return new KyoroTokenizeResult(source, niceSentence, translation, words2, wordPositions, lemmas, readings,
                resultList);
    }

    private WordPosition GetPositionsOfWord(Word word) {
        var min = word.getTokens().stream().min((a, b) -> Integer.compare(a.getPosition(), b.getPosition())).get();
        var max = word.getTokens().stream().max((a, b) -> Integer.compare(a.getPosition(), b.getPosition())).get();
        var maxSurface = max.getSurface();
        return new WordPosition(min.getPosition(), max.getPosition() + maxSurface.length());
    }

    private List<String> SplitSentences(String crazyText) {
        var x = new SentenceDetector();
        int end = 0;
        var list = new ArrayList<String>();
        while ((end = x.getEos(crazyText, null)) > 0) {
            String sentence = crazyText.substring(0, end);
            crazyText = crazyText.substring(end);
            list.add(sentence);
        }

        // No senteces found, the remaining text is one sentence.
        if (end < 0) {
            list.add(crazyText);
        }

        return list;
    }
}