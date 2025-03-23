package secondtry;

public class WordCount {
    enum State {
        NO_WORD {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                if (c == '<') {
                    return IN_BRACKET;
                } else if (Character.isLetter(c)) {
                    context.counter++;
                    return IN_WORD;
                } else {
                    return NO_WORD;
                }
            }
        }, IN_WORD {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                if (c == '<') {
                    return IN_BRACKET;
                } else if (!Character.isLetter(c)) {
                    return NO_WORD;
                } else {
                    return IN_WORD;
                }
            }
        }, IN_BRACKET {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                if (c == '\\') {
                    return IN_BRACKET_ESCAPED;
                } else if (c == '>') {
                    return NO_WORD;
                } else if (c == '"') {
                    return IN_QUOTE;
                } else {
                    return IN_BRACKET;
                }
            }
        }, IN_BRACKET_ESCAPED {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                return IN_BRACKET;
            }
        }, IN_QUOTE {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                if (c == '\\') {
                    return IN_QUOTE_ESCAPED;
                } else if (c == '"') {
                    return IN_BRACKET;
                } else {
                    return IN_QUOTE;
                }
            }
        }, IN_QUOTE_ESCAPED {
            @Override
            WordCount.State handleChar(char c, WordCount context) {
                return IN_QUOTE;
            }
        };

        abstract WordCount.State handleChar(char c, WordCount context);
    }

    int counter;

    /**
     * Counts the number of words in the given text.
     *
     * @param text the text to be processed
     * @return the number of words in the text
     */
    public int count(String text) {
        WordCount.State state = WordCount.State.NO_WORD;
        counter = 0;
        for (char c : text.toCharArray()) {
            state = state.handleChar(c, this);
        }
        return counter;
    }
}