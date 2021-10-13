package com.kyoroteam.kyoro;

import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import com.kyoroteam.kyoro.management.Manager;

import org.junit.Test;

public class ContentFilterTests {
    @Test
    public void SplitsSentenceWithWhitespace() {
        // Given
        var manager = new Manager();
        var lines = Arrays.asList("2021年3月28日\t閲覧", "United Nations Development\nProgramme");

        // When
        var filteredLines = manager.preFilterContent(lines);

        // Then
        assertEquals(4, filteredLines.size());
        assertEquals("2021年3月28日", filteredLines.get(0));
        assertEquals("閲覧", filteredLines.get(1));
        assertEquals("United Nations Development", filteredLines.get(2));
        assertEquals("Programme", filteredLines.get(3));
    }

    @Test
    public void ResultsRemoveSentnecesWithNoVerb() {
        // Given
        var jap = "日本語。日本語を通用する";

        // When
        var results = new Manager().tokenizeTextContent(jap, "tests");

        // Then
        assertEquals(1, results.size());
        assertEquals("日本語を通用する", results.get(0).Sentence);
    }
}
