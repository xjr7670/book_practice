package org.xjr7670.flink.quickstart

import org.apache.flink.api.common.state.{ValueState, ValueStateDescriptor}
import org.apache.flink.api.scala.typeutils.Types
import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.{AssignerWithPeriodicWatermarks, AssignerWithPunctuatedWatermarks, KeyedProcessFunction}
import org.apache.flink.streaming.api.scala.function.WindowFunction
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.watermark.Watermark
import org.apache.flink.streaming.api.windowing.time.Time
import org.apache.flink.streaming.api.windowing.windows.TimeWindow
import org.apache.flink.util.Collector
import org.xjr7670.flink.util.{SensorReading, SensorSource, SensorTimeAssigner}

object AverageSensorReadings {
	def main(args: Array[String]): Unit = {
		// 设置流式执行环境
		val env = {
			StreamExecutionEnvironment.getExecutionEnvironment
		}

		// 在应用中使用事件时间
		env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)

		// 从流式数据源中创建 DataStream[SensorReading] 对象
		val sensorData: DataStream[SensorReading] = env
			.addSource(new SensorSource)
			.assignTimestampsAndWatermarks(new SensorTimeAssigner)

		val avgTemp: DataStream[SensorReading] = sensorData
			.map( r => {
				val celsius = (r.temperatue - 32) * (5.0 / 9.0)
				SensorReading(r.id, r.timestamp, celsius)
			})
			.keyBy(_.id)
			.timeWindow(Time.seconds(5))
			.apply(new TemperatureAverager)

		avgTemp.print()

		env.execute("Compute average sensor temperature")
	}
}

class TemperatureAverager extends WindowFunction[SensorReading, SensorReading, String, TimeWindow] {
	override def apply(sensorId: String, window: TimeWindow, input: Iterable[SensorReading], out: Collector[SensorReading]): Unit = {
		val (cnt, sum) = input.foldLeft((0, 0.0))((c, r) => (c._1 + 1, c._2 + r.temperatue))
		val avgTemp = sum / cnt

		out.collect(SensorReading(sensorId, window.getEnd, avgTemp))
	}
}

class PeriodicAssigner extends AssignerWithPeriodicWatermarks[SensorReading] {
	val bound: Long = 60 * 1000
	var maxTs: Long = Long.MinValue

	override def getCurrentWatermark: Watermark = {
		new Watermark(maxTs - bound)
	}

	override def extractTimestamp(t: SensorReading, l: Long): Long = {
		maxTs = maxTs.max(t.timestamp)
		t.timestamp
	}
}

class PunctuatedAssigner extends AssignerWithPunctuatedWatermarks[SensorReading] {
	val bound: Long = 60 * 1000

	override def checkAndGetNextWatermark(t: SensorReading, l: Long): Watermark = {
		if (t.id == "sensor_1") {
			new Watermark(bound)
		} else {
			null
		}
	}

	override def extractTimestamp(t: SensorReading, l: Long): Long = {
		t.timestamp
	}
}

/**
 * 如果某传感器的温度在 1 秒（处理时间内持续增加
 * 则发出警告
 */
class TempIncreaseAlertFunction extends KeyedProcessFunction[String, SensorReading, String] {
	// 存储最近一次传感器温度读数
	lazy val lastTemp: ValueState[Double] = getRuntimeContext.getState(
		new ValueStateDescriptor[Double]("lastTemp", Types.of[Double])
	)

	// 存储当前活动计时器的时间戳
	lazy val currentTimer: ValueState[Long] = getRuntimeContext.getState(
		new ValueStateDescriptor[Long]("timer", Types.of[Long])
	)

	override def processElement(i: SensorReading, context: KeyedProcessFunction[String, SensorReading, String]#Context, collector: Collector[String]): Unit = {
		val prevTemp = lastTemp.value()
		lastTemp.update(i.temperatue)

		val curTimerTimestamp = currentTimer.value();
		if (prevTemp == 0.0 || i.temperatue < prevTemp) {
			// 温度下降，删除当前计时器
			context.timerService().deleteProcessingTimeTimer(curTimerTimestamp)
			currentTimer.clear()
		} else if (i.temperatue > prevTemp && curTimerTimestamp == 0) {
			// 温度升高并且还未设置计时器
			// 以当前时间 +1 秒设置处理时间计时器
			val timerTs = context.timerService().currentProcessingTime() + 1000
			context.timerService().registerProcessingTimeTimer(timerTs)
			// 记住当前的计时器
			currentTimer.update(timerTs)
		}
	}

	override def onTimer(timestamp: Long, ctx: KeyedProcessFunction[String, SensorReading, String]#OnTimerContext, out: Collector[String]): Unit = {
		out.collect("Temperature of sensor '" + ctx.getCurrentKey + "' monotonically increased for 1 second.")
		currentTimer.clear()
	}
}