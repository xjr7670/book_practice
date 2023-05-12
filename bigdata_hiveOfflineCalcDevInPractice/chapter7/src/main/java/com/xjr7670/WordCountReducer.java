package com.xjr7670;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    /**
     * reduce 函数主要负责对 map 函数处理之后的中间结果进行最后处理
     * 参数 key 是 map 函数处理完后输出的中间结果键值对的键值
     * values 是 map 函数处理完成后输出的中间结果值的列表
     * context 是 MapReduce 框架的上下文对象，可以存放公共类型的数据，比如 reduce
     * 函数处理完成的中间结果可以保存到 context 上下文对象中，由上下文再写入 HDFS 中
     */

    public void reduce(Text key, Iterable<IntWritable> values, Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable v : values) {
            sum += v.get();
        }

        // 将 reduce 处理完的结果输出到 HDFS 文件系统中
        context.write(key, new IntWritable(sum));
    }
}
