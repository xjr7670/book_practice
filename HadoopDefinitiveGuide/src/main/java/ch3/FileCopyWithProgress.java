package ch3;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.util.Progressable;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URI;

/**
 * 将本地文件复制到 Hadoop 文件系统
 * */

public class FileCopyWithProgress {
    public static void main(String[] args) throws Exception {
        String localStr = "file:///f://book_data/HadoopBook/input/docs/1400-8.txt";
        String dst = "hdfs://localhost:9000/tmp/1400-8.txt";
        InputStream in  = new BufferedInputStream(new FileInputStream(localStr));

        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(dst), conf);
        OutputStream out = fs.create(new Path(dst), new Progressable() {
            @Override
            public void progress() {
                System.out.print(".");
            }
        });

        IOUtils.copyBytes(in, out, 4096, true);
    }
}
