import requests
import json

url="https://restcountries.com/v3.1"

response=requests.get(url)

# Check response status and content
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text[:200]}")  # Print first 200 chars

if response.status_code == 200:
    try:
        data=response.json()
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON")
else:
    print(f"Error: API returned status code {response.status_code}")
