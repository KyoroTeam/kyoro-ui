package com.kyoroteam.kyoro;

import static org.junit.Assert.assertTrue;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.stream.*;
import java.util.*;

import com.amazonaws.services.lambda.runtime.Context;

import com.atilika.kuromoji.ipadic.Token;
import com.atilika.kuromoji.TokenizerBase.Mode;
import com.atilika.kuromoji.ipadic.Tokenizer;
import com.google.gson.Gson;
import com.google.gson.JsonIOException;
import com.google.gson.stream.JsonReader;
import com.google.gson.reflect.*;

import org.junit.Test;
import org.mockito.Mockito;

import com.worksap.nlp.sudachi.sentdetect.*;

import ve.Pos;

/**
 * Unit test for simple App.
 */
public class AppTest {
    static String LONG_TEXT = "＜Ａ＞画面表記での使用になんらかの『ルール』(口頭での指示や了解事項を含む)を設けていますか？　⇒たとえば、「使用はスポーツ系番組やスポーツニュースに限る」「一般の報道ニュースでは乱用しない」「見出し、メインタイトル、サイドタイトルに限る」など。＜Ｂ＞『表記』はどうしていますか？　⇒「vs.」は本来小文字で「省略符（ピリオド）」が必要ですが、「大文字(前後の文字と同じ大きさということ)でも可」としていますか。「省略符は不要ですか必要ですか」。＜Ｃ＞『読み』はどうしていますか？　⇒英語の発音はバーサス(versus　ヴァーサス)ですが、この読み方は聞いたことがありません。ふつうは「○○\"対\"××」と読むでしょう。ブイエス(ヴイエス)と読むこともありますか。局のアナウンサーだけでなく、外部のリポーターやナレーターにどのように読ませているでしょうか。テレビ朝日の報道では、表記も読みもルールはない。ただ、最近よく出て来るものの、そもそも「vs.」は「日本語ではない」（外来語でもない）と思うのだが・・・・。";

    /**
     * Rigorous Test :-)
     * 
     * @throws IOException
     * @throws JsonIOException
     */
    @Test
    public void shouldAnswerWithTrue() throws JsonIOException, IOException {
        // var handler = new Handler();
        // var request = new HashMap<String, String>();
        // var context = Mockito.mock(Context.class);
        // request.put("request", LONG_TEXT);
        // var results = handler.handleRequest(request, context);
        // System.out.print(results);
        // assertTrue(true);

        Gson gson = new Gson();
        JsonReader r = new JsonReader(new FileReader("/home/james/Desktop/all_v11.json"));
        var type = new TypeToken<ArrayList<Request>>() {
        }.getType();
        ArrayList<Request> request = gson.fromJson(r, type);

        var handler = new Handler();
        var context = Mockito.mock(Context.class);

        var results = handler.handleRequest(request, context);

        gson.toJson(results, new FileWriter("/home/james/Desktop/all_v11_out.json"));
    }

    @Test
    public void Test() {

    }

    @Test
    public void Sudachi() throws IOException {
        var text = LONG_TEXT;
        var x = new SentenceDetector();
        int end = 0;
        var list = new ArrayList<String>();
        while ((end = x.getEos(text, null)) != 0) {
            String sentence = text.substring(0, end);
            text = text.substring(end);
            list.add(sentence);
        }
    }
}
