import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;
import java.io.File;
import java.io.IOException;

public class Practice21_2 {
    public static void main(String[] args) {
        File file = new File(args[0]);
        if (file.exists()) {
            System.out.println("the word of the file: " + getWords(file));
        } else {
            System.out.println("file does not exists.");
        }
    }

    public static String getWords(File file) {
        Set<String> wordSet = new TreeSet<>();
        try {
            // 从文件读入
            Scanner input = new Scanner(file);
            while (input.hasNext()) {
                // 一行行读
                String line = input.nextLine();
                String[] words = line.split("[\\s\\p{P}]");
                for (String word : words) {
                    wordSet.add(word);       
                }
            }
            input.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return wordSet.toString();
    }
}