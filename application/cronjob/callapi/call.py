#kubectl create configmap script-configmap --from-file=script.py
import os
import requests
import json
from pymongo import MongoClient

api_url = os.environ.get('API_URL')
mongo_uri = os.environ.get('MONGO_URI')

if not api_url:
    print('Error: API_URL environment variable not set')
    exit(1)

if not mongo_uri:
    print('Error: MONGO_URI environment variable not set')
    exit(1)

try:
    # Make API request
    response = requests.get(api_url)
    response.raise_for_status()
    data = json.loads(response.text)
    timestamp = data['timestamp']
    print(timestamp)

    # Insert timestamp into MongoDB
    client = MongoClient(mongo_uri)
    db = client['hello-world']
    collection = db['API_CALL']
    collection.insert_one({'timestamp': timestamp})
    print('Timestamp inserted successfully')
except requests.exceptions.RequestException as e:
    print(f'Error requesting API: {e}')
except json.JSONDecodeError as e:
    print(f'Error decoding JSON: {e}')
except KeyError as e:
    print(f'Error: Key "{e.args[0]}" not found in API response')
except Exception as e:
    print(f'Error inserting timestamp into MongoDB: {e}')
finally:
    client.close()

