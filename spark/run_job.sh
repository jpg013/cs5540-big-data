#!/bin/bash

cat $PWD/../logs/*.log > $PWD/spark-input.log

$SPARK_HOME/bin/spark-submit run-example JavaWordCount $PWD/spark-input.log &> spark-output.log

rm $PWD/spark-input.log
