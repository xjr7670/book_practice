package practice;

import java.io.*;

public class FileIO {
    public static void main(String[] args) {
        String filePath = "e://temp/predeal.sh";
        String outputPath = "e://temp/iotest.txt";
        try {
            String data = readFile(filePath);
            writeFile(outputPath, data);
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public static void writeFile(String path, String data) throws IOException {
        FileWriter fw = new FileWriter(path, true);
        BufferedWriter writer = new BufferedWriter(fw);

        writer.write(data);

        writer.close();
    }

    public static String readFile(String path) throws IOException {
        StringBuilder sb = new StringBuilder();

        FileReader fr = new FileReader(path);
        BufferedReader reader = new BufferedReader(fr);

        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
            sb.append("\n");
        }

        fr.close();
        reader.close();

        return sb.toString();
    }
}
