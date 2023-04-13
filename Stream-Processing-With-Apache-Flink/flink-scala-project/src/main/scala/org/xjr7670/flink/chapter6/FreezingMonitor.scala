package org.xjr7670.flink.chapter6

import org.apache.flink.streaming.api.functions.ProcessFunction
import org.apache.flink.streaming.api.scala.OutputTag
import org.apache.flink.util.Collector
import org.xjr7670.flink.util.SensorReading

class FreezingMonitor extends ProcessFunction[SensorReading, SensorReading] {
	// 定义副输出标签
	lazy val freezingAlarmOutput: OutputTag[String] = new OutputTag[String]("freezing-alarms")

	override def processElement(i: SensorReading, context: ProcessFunction[SensorReading, SensorReading]#Context, collector: Collector[SensorReading]): Unit = {
		if (i.temperatue < 32.0) {
			context.output(freezingAlarmOutput, s"Freezing Alarm for ${i.id}")
		}
		collector.collect(i)
	}
}
