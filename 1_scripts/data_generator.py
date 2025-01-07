import random
import time
from datetime import datetime
from confluent_kafka import Producer
import os
import json

# Absolute path setup for logs
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(project_dir, "5_logs")
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, "data_generator.log")

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Replace with your Kafka server address
}
producer = Producer(producer_config)

# Kafka topic
kafka_topic = "user_activity"

# Sample data generation
def generate_user_activity():
    user_ids = range(1, 101)  # Simulated user IDs
    activities = ["login", "logout", "purchase", "view_item", "add_to_cart"]
    activity = random.choice(activities)
    user_id = random.choice(user_ids)
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "user_id": user_id,
        "activity": activity,
        "timestamp": timestamp
    }

# Function to send data to Kafka
def send_to_kafka(topic, data):
    try:
        producer.produce(topic, value=json.dumps(data).encode('utf-8'))
        producer.flush()
        log_message(f"Data sent to Kafka: {data}")
    except Exception as e:
        log_message(f"Error sending data to Kafka: {e}", error=True)

# Logging function
def log_message(message, error=False):
    with open(log_file_path, "a") as log_file:
        log_type = "ERROR" if error else "INFO"
        log_file.write(f"{datetime.now()} - {log_type} - {message}\n")
    print(f"{log_type}: {message}")

# Main script
if __name__ == "__main__":
    log_message("Starting data generator script.")
    try:
        while True:
            user_activity = generate_user_activity()
            log_message(f"Generated user activity: {user_activity}")
            send_to_kafka(kafka_topic, user_activity)
            time.sleep(2)  # Pause for 2 seconds
    except KeyboardInterrupt:
        log_message("Data generator stopped by user.")
    except Exception as e:
        log_message(f"Unexpected error: {e}", error=True)