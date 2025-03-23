package csv;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class CSVFileReaderTest {
    @Test
    public void testNext() throws IOException {
        CSVFileReader reader = new CSVFileReader("resources/adjacency.csv", ';', '"', true);
        assertArrayEquals(new String[]{"", "A", "B", "C", "D", "E", "F", "G", "H"}, reader.next());
        assertArrayEquals(new String[]{"A", "", "4", "7", "8", "", "", "", ""}, reader.next());
        assertArrayEquals(new String[]{"B", "4", "", "", "", "5", "3", "", ""}, reader.next());
        assertArrayEquals(new String[]{"C", "7", "", "", "2", "", "", "1", ""}, reader.next());
        assertArrayEquals(new String[]{"D", "8", "5", "2", "", "1", "", "2", ""}, reader.next());
        assertArrayEquals(new String[]{"E", "", "3", "", "1", "", "1", "", "5"}, reader.next());
        assertArrayEquals(new String[]{"F", "", "3", "", "", "1", "", "", "1"}, reader.next());
        assertArrayEquals(new String[]{"G", "", "", "1", "2", "", "", "", "1"}, reader.next());
        assertArrayEquals(new String[]{"H", "", "", "", "", "5", "1", "1", ""}, reader.next());
        assertArrayEquals(null, reader.next());
    }

    @Test
    public void testNextWithTry() throws IOException {
        try (CSVFileReader reader = new CSVFileReader("resources/adjacency.csv", ';', '"', true)) {
            assertArrayEquals(new String[]{"", "A", "B", "C", "D", "E", "F", "G", "H"}, reader.next());
            assertArrayEquals(new String[]{"A", "", "4", "7", "8", "", "", "", ""}, reader.next());
        }
    }

    public static void main(String[] args) throws IOException {
        try (CSVFileReader reader = new CSVFileReader("03_CSV/resources/adjacency.csv", ';', '"', true)) {
            ArrayList<ArrayList<String>> adjacency = new ArrayList<>();
            StringBuilder line = new StringBuilder();

            for (String[] csvLine : reader) {
                adjacency.add(new ArrayList<>(Arrays.asList(csvLine)));
            }

            for (int row = 1; row < adjacency.size(); row++) {
                line.setLength(0);
                line.append(String.format("%s: ", adjacency.get(0).get(row)));
                for (int col = 1; col < adjacency.get(row).size(); col++) {
                    if (!adjacency.get(row).get(col).isEmpty()) {
                        line.append(String.format("nach %s:%s, ", adjacency.get(0).get(col), adjacency.get(row).get(col)));
                    }
                }

                line.setLength(Math.max(line.length() - 2, 0));
                System.out.println(line);
            }
        }
    }
}
