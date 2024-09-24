REM CREATE USER
SET "JAVA_HOME=C:\opt\software\java\jdk-11.0.1"
bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9094 --topic demo-topic --from-beginning --consumer.config config/ssl-consumer.properties