REM CREATE USER
SET "JAVA_HOME=C:\opt\software\java\jdk-11.0.1"
bin\windows\kafka-console-producer.bat --broker-list localhost:9094 --topic demo-topic --producer.config config/ssl-producer.properties