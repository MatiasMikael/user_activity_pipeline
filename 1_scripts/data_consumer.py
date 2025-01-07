from confluent_kafka import Consumer, KafkaException
from pymongo import MongoClient
import json
import os
from datetime import datetime

# Absolute path setup for logs
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(project_dir, "5_logs")
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, "kafka_consumer.log")

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["user_activity_db"]
mongo_collection = mongo_db["user_activity"]

# Kafka consumer setup
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mongo_consumer_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)
topic = "user_activity"
consumer.subscribe([topic])

# Logging function
def log_message(message, error=False):
    with open(log_file_path, "a") as log_file:
        log_type = "ERROR" if error else "INFO"
        log_file.write(f"{datetime.now()} - {log_type} - {message}\n")
    print(f"{log_type}: {message}")

# Main script
if __name__ == "__main__":
    log_message("Starting Kafka consumer script.")
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll messages with 1-second timeout
            if msg is None:
                continue
            if msg.error():
                log_message(f"Consumer error: {msg.error()}", error=True)
                continue
            try:
                # Parse the message and insert into MongoDB
                user_activity = json.loads(msg.value().decode('utf-8'))
                mongo_collection.insert_one(user_activity)
                log_message(f"Inserted to MongoDB: {user_activity}")
            except Exception as e:
                log_message(f"Error processing message: {e}", error=True)
    except KeyboardInterrupt:
        log_message("Kafka consumer stopped by user.")
    finally:
        consumer.close()