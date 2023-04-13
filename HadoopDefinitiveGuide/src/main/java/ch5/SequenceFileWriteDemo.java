package ch5;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;

import java.io.IOException;
import java.net.URI;

public class SequenceFileWriteDemo {
    private static final String[] DATA = {
        "One, tow, buckle myshoe",
        "Three, four, shut the door",
        "Five, six, pick up sticks",
        "Seven, eight, lay them straight",
        "Nine, ten, a big fat hen"
    };

    public static void main(String[] args) throws IOException {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(uri), conf);
//        Path path = new Path(uri);

//        IntWritable key = new IntWritable();
//        Text value = new Text();
        SequenceFile.Writer writer = null;

        SequenceFile.Writer.Option path = SequenceFile.Writer.file(new Path(uri));
        SequenceFile.Writer.Option key = SequenceFile.Writer.keyClass(IntWritable.class);
        SequenceFile.Writer.Option value = SequenceFile.Writer.valueClass(Text.class);

        try {
//            writer = SequenceFile.createWriter(fs, conf, path, key.getClass(), value.getClass());  // 书中的这个写法已经过时了
            writer = SequenceFile.createWriter(conf, path, key, value);
            for (int i = 0; i < 100; i++) {
//                key = 100 - i;
//                value.set(DATA[i % DATA.length]);
                System.out.printf("[%s]\t%s\t%s\n", writer.getLength(), 100-i, DATA[i % DATA.length]);
//                writer.append(new IntWritable(i), new Text(DATA[i % DATA.length]));   // 因为是后面必为新写法的时候修改的。所以不需要重新写入到 sequencefile 了
            }
        } finally {
            IOUtils.closeStream(writer);
        }
    }
}
