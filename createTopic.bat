REM CREATE USER
SET "JAVA_HOME=C:\opt\software\java\jdk-11.0.1"
bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9094 --command-config config/ssl-user-config.properties --replication-factor 1 --partitions 1 --topic demo-topic