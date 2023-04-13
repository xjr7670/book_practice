package org.xjr7670.flink.quickstart

import org.apache.flink.streaming.api.scala._

object MyFlink {
	def main(args: Array[String]): Unit = {
		val env = StreamExecutionEnvironment.getExecutionEnvironment

		val inputStream: DataStream[Person] = env.fromElements(
			Person("Adam", 17),
			Person("Sarah", 23),
			Person("John", 28)
		)

		val resultStream: DataStream[Person] = inputStream.filter(p => p.age > 18)

		resultStream.print()

		env.execute("My Scala Flink Program")
	}
}

case class Person(name: String, age: Int)
