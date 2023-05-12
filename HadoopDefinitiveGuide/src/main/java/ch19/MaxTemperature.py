# -*- coding:utf-8 -*-

from pyspark import SparkContext
import re, sys

sc = SparkContext("local", "Max Temperature")
sc.textFile("e:/temp/sample.txt") \
    .map(lambda s: s.split("\t") \
    .filter(lambda rec: (rec[1] != "9999" and re.match("[01459]", rec[2]))) \
    .map(lambda rec: (int(rec[0]), int(rec[1]))) \
    .reduceByKey(max) \
    .saveAsTextFile("e/temp/result.txt")