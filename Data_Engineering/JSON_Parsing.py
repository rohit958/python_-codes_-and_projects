import json
import pandas as pd
import os

df = pd.read_json(r"D:\git\python_-codes_-and_projects\sample_JSON\new 1.json")
#df=pd.json_normalize(df)
print(df.to_string())





# separating street address, city and state from address
import flatten_json
data = open(r"D:\git\python_-codes_-and_projects\sample_JSON\new 1.json")

file= json.load(data)
f=flatten_json(file)
print(f)
