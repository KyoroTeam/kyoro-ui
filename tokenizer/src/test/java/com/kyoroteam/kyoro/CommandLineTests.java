package com.kyoroteam.kyoro;

import static org.junit.Assert.assertEquals;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.util.List;
import org.junit.Test;

public class CommandLineTests {
    @Test
    public void ResultsRemoveSentnecesWithNoVerb() throws UnsupportedEncodingException {
        // Given
        var args = List.of("does-not-exist.txt").toArray(String[]::new);
        var os = new ByteArrayOutputStream();
        var ps = new PrintStream(os);

        // When
        Main.main(args, ps);

        // When
        assertEquals("{\"ErrorMessage\":\"No such file: does-not-exist.txt\"}", os.toString().trim());
    }
}
