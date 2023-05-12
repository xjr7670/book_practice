package Util;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class Utils {
    private FileSystem fileSystem = null;

    public Utils(Configuration conf) {
        try {
            this.fileSystem = FileSystem.get(new URI("hdfs://localhost:9000/"), conf, "hadoop");
        } catch (URISyntaxException e) {
            System.err.println("IOExeception \n" + e);
            System.exit(1);
        } catch (InterruptedException e) {
            System.err.println("InterruptedException \n" + e);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("IOException \n" + e);
            System.exit(1);
        }
    }

    public void deleteDir(String path) throws IOException {
        Path p = new Path(path);
        if (fileSystem.exists(p)) {
            boolean result = fileSystem.delete(new Path(path), true);
            if (result) {
                System.out.printf("%s 已删除！\n", path);
            }
        } else {
            System.out.printf("%s 不存在。\n", path);
        }
    }

    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        Utils u = new Utils(conf);

        u.deleteDir("/tmp/abcde");
    }
}
