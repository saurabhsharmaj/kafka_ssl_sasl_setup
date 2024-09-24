from kafka import KafkaProducer
import json
from datetime import datetime
import time

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Replace with your Kafka broker IP and port
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializing the data to JSON
)

# Send data to the Kafka topic
def send_data(topic, data):
    producer.send(topic, value=data)
    producer.flush()  # Ensure all messages are sent

if __name__ == "__main__":
    for i in range(100):
        topic_name = "PING_TOPIC"  # Replace with your topic name
        message = {"name": "saurabh", "message": "Hello, Kafka!"+datetime.now().strftime("%Y-%m-%d")}  # Example message to send
        send_data(topic_name, message)
        print(f"Sent message to {topic_name}: {message}")
        time.sleep(1)
