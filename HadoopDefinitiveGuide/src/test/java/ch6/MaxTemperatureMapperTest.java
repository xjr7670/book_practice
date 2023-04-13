//package ch6;
//
//import java.io.IOException;
//
//import org.apache.hadoop.io.*;
//import org.junit.*;
//
//
//public class MaxTemperatureMapperTest {
//    @Test
//    public void processesValidRecord() throws IOException, InterruptedException {
//        Text value = new Text("0043011990999991950051518004+68750+023550FM-12+0382" +
//                              "99999V0203201N00261220001CN9999999N9-00111+99999999999");
//        new MapDriver<LongWritable, Text, Text, IntWritable>()
//            .withMapper(new MaxTemperatureMapper())
//            .withInput(new LongWritable(0), value)
//            .withOutput(new Text("1950"), new IntWritable(-11))
//            .runTest();
//    }
//}
