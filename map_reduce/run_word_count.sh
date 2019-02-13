#!/bin/bash

# Runs hadoop map/reduce word count on input files. 
# Before running ensure that your $HADOOP_HOME env variable
# is set and that HDFS is running ($HADOOP_HOME/sbin/start-dfs.sh). 

# Create directory on HDFS. This will throw an error if 
# the directory alreay exists. Ppdate the directory structure as needed
hdfs dfs -mkdir /cs5540
hdfs dfs -mkdir /cs5540/input

# Copy the input files from local filesystem to the HDFS filesystem
hdfs dfs -put ../input/* /cs5540/input

# Run Map Reduce. This path to the hadood-streaming jar may vary. 
hadoop jar /usr/local/Cellar/hadoop/3.1.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -input /cs5540/input -output /cs5540/output -mapper ./word_count_mapper.py -reducer ./word_count_reducer.py -numReduceTasks 1

# Merge results and store into output
hdfs dfs -getmerge /cs5540/output/* ./output/word_count_output.txt

# Remove the hdfs files
hdfs dfs -rmr /cs5540