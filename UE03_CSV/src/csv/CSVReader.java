package csv;

import java.util.ArrayList;

import static csv.CSVReader.State.*;

public class CSVReader {
    private final char delimiter;
    private final char doublequote;
    private final boolean skipinitalwhitespace;

    private ArrayList<String> words;
    private String word;

    /**
     * Adds the current word to the list of words and resets the word.
     */
    private void addWord() {
        words.add(word);
        word = "";
    }

    /**
     * Handles the basic reading of a character.
     * @param ch The character to read.
     * @return The next state.
     */
    private State basicReading(char ch) {
        if (ch == delimiter || ch == '\0') {
            addWord();
            return START_READING;
        } else if (ch == doublequote) {
            return QUOTED;
        } else {
            word += ch;
            return READING;
        }
    }

    enum State {
        START_READING {
            State handleChar(char ch, CSVReader context) {
                if (Character.isWhitespace(ch) && context.skipinitalwhitespace) {
                    return START_READING;
                } else  {
                    return context.basicReading(ch);
                }
            }
        }, READING {
            State handleChar(char ch, CSVReader context) {
                return context.basicReading(ch);
            }
        }, QUOTED {
            State handleChar(char ch, CSVReader context) {
                if (ch == '\0') {
                    throw new IllegalArgumentException("Open quote after: " + ch);
                } else if (ch == context.doublequote) {
                    return DISABLE_QUOTED;
                } else {
                    context.word += ch;
                    return QUOTED;
                }
            }
        }, DISABLE_QUOTED {
            State handleChar(char ch, CSVReader context) {
                if (ch == '\0') {
                    context.addWord();
                    return DISABLE_QUOTED;
                } else if (ch == context.delimiter) {
                    context.addWord();
                    return START_READING;
                } else if (ch == context.doublequote) {
                    context.word += ch;
                    return QUOTED;
                } else {
                    throw new IllegalArgumentException("Unexpected token after closing quote: " + ch);
                }
            }
        };

        abstract State handleChar(char ch, CSVReader context);
    }

    /**
     * Constructor for the CSVReader.
     * @param delimiter The delimiter character.
     * @param doublequote The double quote character.
     * @param skipinitwhitespace Whether to skip initial whitespace.
     */
    public CSVReader(char delimiter, char doublequote, boolean skipinitwhitespace) {
        this.delimiter = delimiter;
        this.doublequote = doublequote;
        this.skipinitalwhitespace = skipinitwhitespace;
    }

    /**
     * Reads the input string and returns the words.
     * @param input The input string.
     * @return The words.
     */
    public String[] read(String input) {
        word = "";
        words = new ArrayList<>();
        State state = START_READING;
        String modInput = input + "\0";

        for (char ch : modInput.toCharArray()) {
            state = state.handleChar(ch, this);
        }

        return words.toArray(new String[0]);
    }
}
