from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Producing customer data to Kafka...")

customers = [
    {"id": 1, "name": "Rohit", "age": 28, "city": "Pune"},
    {"id": 2, "name": "Anjali", "age": 24, "city": "Delhi"},
    {"id": 3, "name": "Rahul", "age": 30, "city": "Mumbai"},
    {"id": 4, "name": "Kiran", "age": 26, "city": "Bangalore"}
]

while True:
    customer = random.choice(customers)
    producer.send("customer_topic", customer)
    print(f"✅ Sent: {customer}")
    time.sleep(2)