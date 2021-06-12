package com.kyoroteam.kyoro;



import static org.junit.Assert.assertTrue;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.*;

import com.amazonaws.services.lambda.runtime.Context;

import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.TokenizerBase.Mode;
import com.atilika.kuromoji.ipadic.Tokenizer;

import org.junit.Test;
import org.mockito.Mockito;

import ve.Parse;
import ve.Pos;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        var handler = new Handler();
        var request = new HashMap<String, String>();
        var context = Mockito.mock(Context.class);
        request.put("request", "この言語は少しばかげているように見える");
        var results = handler.handleRequest(request, context);
        System.out.print(results);
        assertTrue( true );
    }

    @Test
    public void Test()
    {
        var builder = new Tokenizer.Builder();
        Tokenizer tokenizer = builder.mode(Mode.SEARCH).build();
        var tokens = tokenizer.tokenize("＜Ａ＞画面表記での使用になんらかの『ルール』(口頭での指示や了解事項を含む)を設けていますか？　⇒たとえば、「使用はスポーツ系番組やスポーツニュースに限る」「一般の報道ニュースでは乱用しない」「見出し、メインタイトル、サイドタイトルに限る」など。＜Ｂ＞『表記』はどうしていますか？　⇒「vs.」は本来小文字で「省略符（ピリオド）」が必要ですが、「大文字(前後の文字と同じ大きさということ)でも可」としていますか。「省略符は不要ですか必要ですか」。＜Ｃ＞『読み』はどうしていますか？　⇒英語の発音はバーサス(versus　ヴァーサス)ですが、この読み方は聞いたことがありません。ふつうは「○○\"対\"××」と読むでしょう。ブイエス(ヴイエス)と読むこともありますか。局のアナウンサーだけでなく、外部のリポーターやナレーターにどのように読ませているでしょうか。テレビ朝日の報道では、表記も読みもルールはない。ただ、最近よく出て来るものの、そもそも「vs.」は「日本語ではない」（外来語でもない）と思うのだが・・・・。");
        var parser = new ve.Parse(tokens.toArray(new Token[0]));  
        var words = parser.words();
        var fixedWords = words.stream()
            .filter(r -> !r.getPart_of_speech().equals(Pos.Postposition) && !r.getPart_of_speech().equals(Pos.Symbol))
            .filter(r -> !r.getLemma().equals("*"))
            .map(r -> new Result(r.getPart_of_speech(), r.toString(), r.getLemma(), r.getReading()))
            .collect(Collectors.toList());
        for (var word : fixedWords) {
            System.out.println(word.Word + " " + word.PartOfSpeeach + " " + word.Lemma + " " + word.Reading);
        }
    }
}
