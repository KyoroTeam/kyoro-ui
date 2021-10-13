package com.kyoroteam.kyoro;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.*;

import com.google.gson.Gson;
import com.google.gson.JsonIOException;
import com.google.gson.stream.JsonReader;
import com.kyoroteam.kyoro.tokenizer.KyoroTokenizer;
import com.kyoroteam.kyoro.tokenizer.Request;
import com.google.gson.reflect.*;

import org.junit.Test;

import com.worksap.nlp.sudachi.sentdetect.*;

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
    // @Test
    private void shouldAnswerWithTrue() throws JsonIOException, IOException {
        // Gson gson = new Gson();
        // JsonReader r = new JsonReader(new
        // FileReader("/home/james/Desktop/data/all_v11.json"));
        // var type = new TypeToken<ArrayList<Request>>() {
        // }.getType();
        // ArrayList<Request> request = gson.fromJson(r, type);

        // var handler = new KyoroTokenizer();

        // var results = handler.tokenize(request);

        // var writer = new FileWriter("/home/james/Desktop/data/all_v11_out.json");
        // gson.toJson(results, writer);
        // writer.flush();
        // writer.close();
    }
}
