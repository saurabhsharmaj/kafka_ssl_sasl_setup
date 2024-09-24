from kafka import KafkaConsumer
import json

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    'PING_TOPIC',  # Replace with your topic name
    bootstrap_servers=['localhost:9094'],  # Replace with your Kafka broker IP and port
    auto_offset_reset='earliest',  # Start reading from the earliest available message
    enable_auto_commit=True,
    group_id='email_consumer_group',  # Replace with your consumer group ID
   value_deserializer=lambda x: json.loads(x.decode('utf-8'))   # Deserialize JSON data
)

# Consume data from the Kafka topic
for message in consumer:
    print(f"Consumed message: {message.value}")
