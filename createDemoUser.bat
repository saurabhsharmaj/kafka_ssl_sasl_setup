REM CREATE USER
SET "JAVA_HOME=C:\opt\software\java\jdk-11.0.1"
bin\windows\kafka-configs.bat --zookeeper localhost:2181 --alter --add-config SCRAM-SHA-512=[password=secret] --entity-type users --entity-name demouser