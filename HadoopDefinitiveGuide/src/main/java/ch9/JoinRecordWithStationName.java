//package ch9;
//
//import ch5.TextPair;
//import ch8.JobBuilder;
//import org.apache.hadoop.conf.Configuration;
//import org.apache.hadoop.conf.Configured;
//import org.apache.hadoop.fs.Path;
//import org.apache.hadoop.io.Text;
//import org.apache.hadoop.mapred.FileOutputFormat;
//import org.apache.hadoop.mapred.TextInputFormat;
//import org.apache.hadoop.mapred.lib.MultipleInputs;
//import org.apache.hadoop.mapreduce.Job;
//import org.apache.hadoop.mapreduce.Partitioner;
//import org.apache.hadoop.util.Tool;
//import org.apache.hadoop.util.ToolRunner;
//
//public class JoinRecordWithStationName extends Configured implements Tool {
//    public static class KeyPartitioner extends Partitioner<TextPair, Text> {
//        @Override
//        public int getPartition(TextPair key, Text value, int numPartitions) {
//            return (key.getFirst().hashCode() & Integer.MAX_VALUE) % numPartitions;
//        }
//    }
//
//    @Override
//    public int run(String[] args) throws Exception {
//        if (args.length != 3) {
//            JobBuilder.printUsage(this, "<ncdc input> <station input> <output>");
//            return -1;
//        }
//
//        Configuration conf = new Configuration();
//
//        Job job = Job.getInstance(conf, "Join weather records with station names");
//        job.setJarByClass(getClass());
//
//        Path ncdcInputPath = new Path(args[0]);
//        Path stationInputPath = new Path(args[1]);
//        Path outputPath = new Path(args[2]);
//
//        MultipleInputs.addInputPath(getConf(), ncdcInputPath,
//                TextInputFormat.class, JoinRecordMapper.class);
//        MultipleInputs.addInputPath(job, stationInputPath,
//                TextInputFormat.class, JoinStationMapper.class);
//        FileOutputFormat.setOutputPath(job, outputPath);
//
//        job.setPartitionerClass(KeyPartitioner.class);
//        job.setGroupingComparatorClass(TextPair.FirstComparator.class);
//
//        job.setMapOutputKeyClass(TextPair.class);
//        job.setReducerClass(Text.class);
//        job.setOutputKeyClass(Text.class);
//
//        return job.waitForCompletion(true) ? 0 : 1;
//    }
//
//    public static void main(String[] args) throws Exception {
//        int exitCode = ToolRunner.run(new JoinRecordWithStationName(), args);
//        System.exit(exitCode);
//    }
//}
