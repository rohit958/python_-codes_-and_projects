from kafka import KafkaConsumer
import json

# Initialize consumer
consumer = KafkaConsumer(
    'customer_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='customer-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Listening for customer data...\n")

# Continuously listen for messages
for message in consumer:
    data = message.value
    print(f"📥 Received customer data: {data}")