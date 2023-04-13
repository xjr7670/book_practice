package com.xjr7670;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class WordCountMap extends Mapper<LongWritable, Text, Text, IntWritable> {
    private static final IntWritable one = new IntWritable(1);
    private static final Text word = new Text();

    /**
     * map 函数主要负责对 README.txt 文件内容进行映射处理
     * key 是从 README.txt 文件中读取的每行文本的偏移量地址
     * value 是从 README.txt 中获取的一行文本，由 MapReduce 框架负责传入
     * context 是 MapReduce 框架的上下文对象，可以存放公共类型的数据，比如 map
     * 函数处理完的中间结果可以保存到 context 上下文对昂中，MapReduce 框架再根据
     * 上下文对象中的数据将其持久化到本地磁盘，这都是 MapReduce 框架完成的
     */

    public void map(LongWritable kye, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] words = line.split(" ");
        for (String w : words) {
            word.set(w);
            context.write(word, one);
        }
    }

}
