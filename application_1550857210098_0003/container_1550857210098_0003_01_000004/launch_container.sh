#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/Library/Java/JavaVirtualMachines/jdk1.8.0_202.jdk/Contents/Home"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/usr/local/Cellar/hadoop/3.1.1/libexec"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/usr/local/Cellar/hadoop/3.1.1/libexec"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/usr/local/Cellar/hadoop/3.1.1/libexec/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/usr/local/Cellar/hadoop/3.1.1/libexec"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/usr/local/Cellar/hadoop/3.1.1/libexec"}
export HADOOP_TOKEN_FILE_LOCATION="/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/appcache/application_1550857210098_0003/container_1550857210098_0003_01_000004/container_tokens"
export CONTAINER_ID="container_1550857210098_0003_01_000004"
export NM_PORT="50309"
export NM_HOST="10.48.45.112"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/appcache/application_1550857210098_0003"
export LOCAL_USER_DIRS="/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/"
export LOG_DIRS="/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004"
export USER="justin.graber"
export LOGNAME="justin.graber"
export HOME="/home/"
export PWD="/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/appcache/application_1550857210098_0003/container_1550857210098_0003_01_000004"
export JVM_PID="$$"
export MALLOC_ARENA_MAX=""
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export STDOUT_LOGFILE_ENV="/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/stdout"
export SHELL="/bin/bash"
export HADOOP_ROOT_LOGGER="INFO,console"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export STDERR_LOGFILE_ENV="/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/stderr"
export HADOOP_CLIENT_OPTS=""
echo "Setting up job resources"
ln -sf "/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/appcache/application_1550857210098_0003/filecache/11/job.jar" "job.jar"
ln -sf "/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/filecache/13/reducer.py" "reducer.py"
ln -sf "/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/filecache/12/mapper.py" "mapper.py"
ln -sf "/tmp/hadoop-justin.graber/nm-local-dir/usercache/justin.graber/appcache/application_1550857210098_0003/filecache/13/job.xml" "job.xml"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/launch_container.sh"
chmod 640 "/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
ls -l 1>>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
find -L . -maxdepth 5 -ls 1>>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 10.48.45.112 50511 attempt_1550857210098_0003_m_000002_0 4 1>/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/stdout 2>/usr/local/Cellar/hadoop/3.1.1/libexec/logs/userlogs/application_1550857210098_0003/container_1550857210098_0003_01_000004/stderr "
