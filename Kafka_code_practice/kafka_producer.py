from kafka import KafkaProducer
import json
import time
import random
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Producing customer data to Kafka...")

# ...existing code...
# replaced static customers list + infinite loop with generation of 100 unique IDs
first_names = ["Rohit","Anjali","Rahul","Kiran","Sneha","Vikram","Pooja","Amit","Neha","Sahil","Riya","Manish","Tara","Dev","Isha"]
last_names = ["Shah","Patel","Kumar","Verma","Singh","Joshi","Mehta","Rao","Gupta","Bose"]
cities = ["Pune","Delhi","Mumbai","Bangalore","Chennai","Hyderabad","Kolkata","Jaipur","Lucknow","Ahmedabad"]

try:
    for id_ in range(1, 101):
        customer = {
            "id": id_,
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "age": random.randint(18, 75),
            "city": random.choice(cities)
        }
        producer.send("customer_topic", customer)
        print(f"✅ Sent: {customer}")
        time.sleep(0.1)  # small delay between messages
    producer.flush()
    print("🎯 Finished sending 100 unique customer records.")
finally:
    producer.close()