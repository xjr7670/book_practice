package practice;

import java.io.*;

public class FileIO2 {
    public static void main(String[] args) throws IOException {
        String srcPath = "e:/temp/iotest.txt";
        String tgtPath = "e:/temp/writeresult.txt";
        String data = "";
        data = readData(srcPath);
//        System.out.println(data);
        writeData(tgtPath, data);
    }

    private static void writeData(String path, String data) throws IOException{
        BufferedWriter writer = new BufferedWriter(new FileWriter(path, true));
        writer.write(data);
        writer.close();
    }

    public static String readData(String path) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(path));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        return sb.toString();
    }
}
