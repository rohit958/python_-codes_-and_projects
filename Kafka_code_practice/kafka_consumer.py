from kafka import KafkaConsumer
import json
import os
from pathlib import Path
from datetime import datetime

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

# Set up single output file
script_dir = Path(__file__).resolve().parent
output_dir = script_dir / "received_messages"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "all_customers.json"

# Initialize file with empty array if it doesn't exist
if not output_file.exists():
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump([], f)

# Continuously listen for messages
for message in consumer:
    data = message.value
    
    # Read existing data
    with open(output_file, 'r', encoding='utf-8') as f:
        all_data = json.load(f)
    
    # Append new message
    all_data.append({
        'timestamp': datetime.utcnow().isoformat(),
        'partition': message.partition,
        'offset': message.offset,
        'data': data
    })
    
    # Write updated data back
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    print(f"📥 Received customer data: {data}")
    print(f"💾 Appended to: {output_file}")