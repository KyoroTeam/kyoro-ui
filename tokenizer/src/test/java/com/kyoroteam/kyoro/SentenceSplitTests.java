package com.kyoroteam.kyoro;

import static org.junit.Assert.assertEquals;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizer;
import com.kyoroteam.kyoro.tokenizer.Request;

import org.junit.Test;

public class SentenceSplitTests {
    @Test
    public void MultipleSentences_WhenLastSentneceHasNoEnding_LastSentenceIncluded() {
        // Given
        String text = "    ^ 2021年3月28日閲覧。\n    ^ United Nations Development Programme. pp. 343-346";

        // When
        var results = new KyoroTokenizer().tokenize(new Request(text, "", ""));

        // Then
        assertEquals("    ^ 2021年3月28日閲覧。", results.get(0).Sentence);
        assertEquals("\n    ^ United Nations Development Programme. pp. 343-346", results.get(1).Sentence);
    }
}
