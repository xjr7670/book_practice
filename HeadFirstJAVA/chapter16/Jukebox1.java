import java.util.*;
import java.io.*;

public class Jukebox1 {
    ArrayList<String> songList = new ArrayList<String>();

    public static void main(String[] args) {
        Jukebox1 jb = new Jukebox1();
        jb.go();
    }

    public void go() {
        getSongs();
        Collections.sort(songList);
        System.out.println(songList);
    }

    // 读取文件
    void getSongs() {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream("SongList.txt"), "UTF-8"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                addSong(line);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    void addSong(String lineToParse) {
        String[] tokens = lineToParse.split("/");
        songList.add(tokens[0]);
    }
}