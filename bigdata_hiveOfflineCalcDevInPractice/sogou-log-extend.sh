#!/bin/bash
#infile=/sogou.500w.utf8 输入文件
infile=$1
#outfile=/sogou.500w.utf8.ext 输出文件
outfile=$2
awk -F '\t' '{print $0"\t"substr($1,1,4)" \t"substr($1,5,2)"\t"substr($1,7,2)"\t"substr($1,9,2)}' $infile > $outfile
