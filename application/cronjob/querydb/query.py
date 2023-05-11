import os
from pymongo import MongoClient

mongo_uri = os.environ.get('MONGO_URI')

if not mongo_uri:
    print('Error: MONGO_URI environment variable not set')
    exit(1)

try:
    # Connect to MongoDB and retrieve latest timestamp document
    client = MongoClient(mongo_uri)
    db = client['hello-world']
    collection = db['API_CALL']
    latest_timestamp_doc = collection.find_one(sort=[('timestamp', -1)])

    # Print latest timestamp value
    if latest_timestamp_doc is not None and 'timestamp' in latest_timestamp_doc:
        latest_timestamp = latest_timestamp_doc['timestamp']
        print(f'Latest timestamp: {latest_timestamp}')
    else:
        print('No timestamps found in database')
except Exception as e:
    print(f'Error retrieving latest timestamp from MongoDB: {e}')
finally:
    client.close()

