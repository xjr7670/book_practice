package ch3;

import org.apache.hadoop.fs.FsUrlStreamHandlerFactory;
import org.apache.hadoop.io.IOUtils;

import java.io.InputStream;
import java.net.URL;

public class URLCat {
    static {
        try {
            System.load("d://ProgramFiles/hadoop/bin/hadoop.dll");
        } catch (UnsatisfiedLinkError e) {
            e.printStackTrace();
            System.exit(1);
        }
        URL.setURLStreamHandlerFactory(new FsUrlStreamHandlerFactory());
    }

    public static void main(String[] args) throws Exception {
        InputStream in = null;
        try {
            in = new URL("hdfs://localhost:9000/tmp/quangle.txt").openStream();
            IOUtils.copyBytes(in, System.out, 4096, false);
        } finally {
            IOUtils.closeStream(in);
        }
    }
}
