package com.kyoroteam.kyoro.management;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizeResult;
import com.kyoroteam.kyoro.tokenizer.KyoroTokenizer;
import com.kyoroteam.kyoro.tokenizer.Request;

public class Manager {

    public Manager() {

    }

    public List<KyoroTokenizeResult> tokenizeContent(String filename) throws IOException {
        var content = Files.readString(Path.of(filename));

        var japaneseText = filterJapaneseText(content);

        var request = Arrays.asList(new Request(japaneseText, "", filename));

        return new KyoroTokenizer().tokenize(request);
    }

    private String filterJapaneseText(String anyPossibleText) {
        return anyPossibleText;
    }
}
