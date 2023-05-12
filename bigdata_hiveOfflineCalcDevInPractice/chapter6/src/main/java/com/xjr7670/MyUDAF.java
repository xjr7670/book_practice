package com.xjr7670;

import org.apache.hadoop.hive.ql.exec.UDAFEvaluator;
import org.apache.hadoop.hive.ql.metadata.HiveException;
import org.apache.hadoop.hive.ql.udf.generic.GenericUDAFAverage;

public class MyUDAF extends GenericUDAFAverage {
    public static class CountUDAFEvaluator implements UDAFEvaluator {
        private int count = 0;

        public CountUDAFEvaluator() {
            super();
            init();
        }

        public void init() {
            count = 0;
        }

        public boolean iterate(String value) throws HiveException {
            count += 1;
            return true;
        }

        public int terminatePartial() {
            return 1;
        }

        public boolean merge(int other) {
            count += 1;
            return true;
        }

        public int terminate() {
            return count;
        }
    }
}
