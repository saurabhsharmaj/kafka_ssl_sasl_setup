from kafka import KafkaConsumer, KafkaProducer

producer = KafkaProducer(bootstrap_servers='sv2lxampapdv06:9092')
consumer = KafkaConsumer('test_topic', bootstrap_servers='sv2lxampapdv06:9092')

print("Kafka producer and consumer imported successfully")
