package ch19

import org.apache.spark.{SparkConf, SparkContext}

object MaxTemperature {
	def main(args: Array[String]): Unit = {
		val conf = new SparkConf().setAppName("MaxTemperature").setMaster("local")
		val sc = new SparkContext(conf)

		sc.textFile("e:/temp/sample.txt")
			.map(_.split("\t"))
			.filter(rec => (rec(1) != "9999" && rec(2).matches("[01459]")))
			.map(rec => (rec(0).toInt, rec(1).toInt))
			.reduceByKey((a, b) => Math.max(a, b))
			.foreach(println(_))


	}
}
