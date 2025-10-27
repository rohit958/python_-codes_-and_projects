import os
import json
import pandas as pd

with open('\recieved_messages\all_customers.json', 'r', encoding='utf-8') as json_file:
    data=pd.read_json(json_file)

print(data.head(5))
    