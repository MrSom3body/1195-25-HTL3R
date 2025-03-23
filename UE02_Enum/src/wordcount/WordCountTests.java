package wordcount;

import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class WordCountTests {
    @Test
    public void testCountSimple() {
        WordCount wordCount = new WordCount();
        assertEquals(0, wordCount.count(""));
        assertEquals(0, wordCount.count("1337"));
        assertEquals(3, wordCount.count("Das sind 3 Wörter"));
    }

    @Test
    public void testCountComplex() {
        WordCount wordCount = new WordCount();
        assertEquals(9, wordCount.count("Das ist ein String mit Sonderzeichen, Zahlen (123) und 9 Wörtern!"));
    }

    @Test
    void testCountBig() throws IOException {
        try (
                BufferedReader in = Files.newBufferedReader(Paths.get("resources/crsto12.html"))
        ) {
            StringBuilder content = new StringBuilder();
            WordCount wordCount = new WordCount();
            String line;
            while ((line = in.readLine()) != null) {
                content.append(line).append("\n");
            }
            // The file contains 482515 words (Source: Luka)
            assertEquals(482515, wordCount.count(content.toString()));
        }
    }
}
