package org.xjr7670.flink.chapter6

import org.apache.flink.api.common.state.ValueState
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment
import org.apache.flink.streaming.api.scala.DataStream
import org.xjr7670.flink.util.{SensorReading, SensorSource, SensorTimeAssigner}

class CoProcessFunction {
	def main(args: Array[String]): Unit = {
		val env = StreamExecutionEnvironment.getExecutionEnvironment();
		val sensorData: DataStream[SensorReading] = env.addSource(new SensorSource)
			.assignTimestampsAndWatermarks(new SensorTimeAssigner)

		// 开启读数转发的过滤开关
		val filterSwitches: DataStream[(String, Long)] = env.fromCollection(Seq(
			("sensor_2", 10 * 1000L),
			("sensor_7", 60 * 1000L)
		))

	}
}

class ReadingFilter extends CoProcessFunction[SensorReading, (String, Long), SensorReading] {
}
