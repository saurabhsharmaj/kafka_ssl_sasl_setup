REM CREATE USER
SET "JAVA_HOME=C:\opt\software\java\jdk-11.0.1"
bin\windows\kafka-acls.bat --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:demouser --consumer --topic demo-topic --group demo-consumer-group