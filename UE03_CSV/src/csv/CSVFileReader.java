package csv;

import java.io.*;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class CSVFileReader implements Closeable, Iterable<String[]> {
    private final CSVReader reader;
    private final BufferedReader fileReader;

    /**
     * Creates a new CSV file reader.
     * @param filename The name of the file to read.
     * @param delimiter The delimiter character.
     * @param doublequote The double quote character.
     * @param skipinitalwhitespace Whether to skip initial whitespace.
     * @throws FileNotFoundException If the file does not exist.
     */
    public CSVFileReader(String filename, char delimiter, char doublequote, boolean skipinitalwhitespace) throws FileNotFoundException {
        reader = new CSVReader(delimiter, doublequote, skipinitalwhitespace);
        fileReader = new BufferedReader(new FileReader(filename));
    }

    /**
     * Reads the next line from the file.
     * @return The next line as an array of strings or null if there are no more lines.
     * @throws IOException If an error occurs while reading the file.
     */
    public String[] next() throws IOException {
        String fileLine = fileReader.readLine();
        return fileLine != null ? reader.read(fileLine) : null;
    }

    /**
     * Closes the file reader.
     * @throws IOException If an error occurs while closing the file.
     */
    @Override
    public void close() throws IOException {
        fileReader.close();
    }

    /**
     * Returns an iterator over the lines of the file.
     * @return An iterator over the lines of the file.
     */
    public Iterator<String[]> iterator() {
        return new Iterator<String[]>() {
            private String[] nextLine = fetchNextLine();

            /**
             * Fetches the next line from the file.
             * @return The next line as an array of strings or null if there are no more lines.
             */
            private String[] fetchNextLine() {
                try {
                    return CSVFileReader.this.next();
                } catch (IOException e) {
                    throw new RuntimeException("Error reading the CSV file", e);
                }
            }

            /**
             * Returns whether there are more lines to read.
             * @return True if there are more lines to read, false otherwise.
             */
            @Override
            public boolean hasNext() {
                return nextLine != null;
            }

            /**
             * Returns the next line from the file.
             * @return The next line as an array of strings.
             */
            @Override
            public String[] next() {
                if (nextLine == null) {
                    throw new NoSuchElementException("No more lines to read");
                }
                String[] currentLine = nextLine;
                nextLine = fetchNextLine();
                return currentLine;
            }
        };
    }
}
