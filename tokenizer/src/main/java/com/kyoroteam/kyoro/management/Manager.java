package com.kyoroteam.kyoro.management;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizeResult;
import com.kyoroteam.kyoro.tokenizer.KyoroTokenizer;
import com.kyoroteam.kyoro.tokenizer.Request;

import ve.Pos;

public class Manager {
    public List<KyoroTokenizeResult> tokenizeFileContent(String filePath) throws IOException {
        var lines = Files.readAllLines(Path.of(filePath));
        return tokenizeTextContent(lines, filePath);
    }

    public List<KyoroTokenizeResult> tokenizeTextContent(String text, String source) {
        var lines = Arrays.asList(text);
        return tokenizeTextContent(lines, source);
    }

    public List<KyoroTokenizeResult> tokenizeTextContent(List<String> lines, String source) {
        var result = new ArrayList<KyoroTokenizeResult>();
        var tokenizer = new KyoroTokenizer();

        var cleanLines = preFilterContent(lines);
        for (String line : cleanLines) {
            var rawTokens = tokenizer.tokenize(new Request(line, "", source));
            var tokens = postFilterContent(rawTokens);
            result.addAll(tokens);
        }

        return result;
    }

    public List<String> preFilterContent(List<String> lines) {
        return splitByNewlines(lines);
    }

    public List<String> splitByNewlines(List<String> lines) {
        var results = new ArrayList<String>();

        for (String line : lines) {
            var splitByWhite = line.split("[\n\t]");
            for (String line2 : splitByWhite) {
                results.add(line2);
            }
        }

        return results;
    }

    private List<KyoroTokenizeResult> postFilterContent(List<KyoroTokenizeResult> results) {
        return removeSentencesWithoutVerbs(results);
    }

    private List<KyoroTokenizeResult> removeSentencesWithoutVerbs(List<KyoroTokenizeResult> results) {
        return results.stream()
                .filter(result -> result.VeWords.stream().anyMatch(word -> word.getPart_of_speech() == Pos.Verb))
                .collect(Collectors.toList());
    }
}
