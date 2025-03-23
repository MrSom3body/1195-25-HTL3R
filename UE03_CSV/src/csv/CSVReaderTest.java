package csv;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class CSVReaderTest {
    @Test
    public void simpleTestRead() {
        CSVReader reader = new CSVReader(',', '"', false);
        assertArrayEquals(new String[]{"one", "two", " three"}, reader.read("one,two, three"));
        assertArrayEquals(new String[]{"one", "", "three"}, reader.read("one,,three"));
        assertArrayEquals(new String[]{"bomboclad1 bomboclad2"}, reader.read("bomboclad1 bomboclad2"));
    }

    @Test
    public void quotedTestRead() {
        CSVReader reader = new CSVReader(',', '"', true);
        assertArrayEquals(new String[]{"uno", "dos", "tres, quatro", "cinco"}, reader.read("\"uno\",dos,\"tres, quatro\",cin\"co\""));
        assertThrows(IllegalArgumentException.class, () -> reader.read("\"nicht\"ok"));
        assertThrows(IllegalArgumentException.class, () -> reader.read("\"nicht ok"));
    }

    @Test
    public void quoteInQuotedTestRead() {
        CSVReader reader = new CSVReader(',', '"', true);
        assertArrayEquals(new String[]{"ein,s", "zw\"ei", "drei"}, reader.read("\"ein,s\",\"zw\"\"ei\",drei"));
        assertArrayEquals(new String[]{"bomboclad69\""}, reader.read("\"bomboclad69\"\"\""));
    }

    @Test
    public void spacesTestRead() {
        CSVReader reader = new CSVReader(',', '"', true);
        assertArrayEquals(new String[]{"one", "two ", "three "}, reader.read("   one,    two ,three "));
        assertArrayEquals(new String[]{"one ", "two  ", "three   "}, reader.read(" one , two  , three   "));
    }
}
