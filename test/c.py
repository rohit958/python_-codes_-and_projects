import json
import pandas as pd

with open(r"D:\git\python_-codes_-and_projects\sample_JSON\Govement_data\City_bus.JSON") as file:
    data = json.load(file)
    print(data['fields'])
