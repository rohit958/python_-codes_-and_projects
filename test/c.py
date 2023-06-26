import json
import pandas as pd

with open(r"D:\git\python_-codes_-and_projects\sample_JSON\Govement_data\Monthly_petroleum_consumption.JSON") as file:
    for line in file:
        data = json.loads(line)
