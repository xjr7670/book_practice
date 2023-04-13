package org.xjr7670.flink.util

import org.apache.flink.streaming.api.windowing.time.Time
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor

class SensorTimeAssigner extends BoundedOutOfOrdernessTimestampExtractor[SensorReading] (Time.seconds(5)) {
	override def extractTimestamp(t: SensorReading): Long = t.timestamp
}
