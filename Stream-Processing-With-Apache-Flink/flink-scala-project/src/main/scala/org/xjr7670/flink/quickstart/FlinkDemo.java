package org.xjr7670.flink.quickstart;

import org.apache.flink.api.java.tuple.Tuple;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import scala.Tuple2;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class FlinkDemo {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        List<ArrayList<Integer>> list = new ArrayList<>();
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        for (int i = 0; i < 100; i++) {
            tmp.add(i);
            tmp.add(i*2);
            tmp.add(i+5);
            list.add(tmp);
            tmp.clear();
        }
        DataStream<Tuple2<String, Integer>> persons = env.fromElements(
                new Tuple2<>("Adam", 17),
                new Tuple2<>("Sarah", 23),
                new Tuple2<>("Cavin", 16)
        );

        SingleOutputStreamOperator<Integer> map = persons.map(p -> p._2 + 2);

        map.print();

        env.execute("my java flink program");
    }
}
