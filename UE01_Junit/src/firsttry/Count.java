package firsttry;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Count {
    /**
     * Counts the number of words in a text.
     *
     * @param text The text to count the words in.
     * @return The number of words in the text.
     */
    public static long count(String text) {
        // text = text.replaceAll("(?<!\")<.*?>(?!\")", " ");
        text = text.replaceAll("< *(\\w+)( +\\w+=\".*\")*( +\\w+)* *>", " ");
        text = text.replaceAll("(<.*)|(.*>)", "");

        Pattern p = Pattern.compile("\\w+");
        Matcher m = p.matcher(text);
        
        int counter = 0;
        while (m.find()) {
            counter++;
        }
        
        return counter;
    }
}
