package ch19;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import scala.Tuple2;

public class MaxTemperatureSpark {
    public static void main(String[] args) throws Exception {
        SparkConf conf = new SparkConf();
        JavaSparkContext sc = new JavaSparkContext("local", "MaxTemperatureSpark", conf);
        JavaRDD<String> lines = sc.textFile("e:/temp/sample.txt");

        JavaRDD<String[]> records = lines.map((Function<String, String[]>) s -> s.split("\t"));

        JavaRDD<String[]> filtered = records.filter((Function<String[], Boolean>) rec -> rec[1] != "9999" && rec[2].matches("[01459]"));

        JavaPairRDD<Integer, Integer> tuples = filtered.mapToPair((PairFunction<String[], Integer, Integer>) rec -> new Tuple2<>(Integer.parseInt(rec[0]), Integer.parseInt(rec[1])));

        JavaPairRDD<Integer, Integer> maxTmeps = tuples.reduceByKey((Function2<Integer, Integer, Integer>) (integer, integer2) -> Math.max(integer, integer2));

        maxTmeps.foreach(System.out::println);
    }
}
