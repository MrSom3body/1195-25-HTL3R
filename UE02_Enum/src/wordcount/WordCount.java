package wordcount;

public class WordCount {
    enum State {
        INWORD {
            @Override
            State handleChar(char c, WordCount context) {
                if (!Character.isLetter(c)) {
                    return NOWORD;
                } else {
                    return INWORD;
                }
            }
        },

        NOWORD {
            @Override
            State handleChar(char c, WordCount context) {
                if (Character.isLetter(c)) {
                    context.counter++;
                    return INWORD;
                } else {
                    return NOWORD;
                }
            }
        };

        abstract State handleChar(char c, WordCount context);
    }

    int counter;

    /**
     * Counts the number of words in the given text.
     *
     * @param text the text to be processed
     * @return the number of words in the text
     */
    public int count(String text) {
        State state = State.NOWORD;
        counter = 0;
        for (char c : text.toCharArray()) {
            state = state.handleChar(c, this);
        }
        return counter;
    }
}