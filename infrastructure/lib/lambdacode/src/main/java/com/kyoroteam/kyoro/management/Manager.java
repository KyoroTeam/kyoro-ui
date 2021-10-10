package com.kyoroteam.kyoro.management;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.*;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizer;
import com.kyoroteam.kyoro.tokenizer.Request;
import com.worksap.nlp.sudachi.sentdetect.*;

public class Manager {

    public Manager() {

    }

    public void indexContent(String filename) throws IOException {
        var content = Files.readString(Path.of(filename));

        var japaneseText = filterJapaneseText(content);

        var request = Arrays.asList(new Request(japaneseText, "", filename));

        var tokens = new KyoroTokenizer().tokenize(request);
    }

    private String filterJapaneseText(String anyPossibleText) {
        return anyPossibleText;
    }
}
