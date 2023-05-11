from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_data = {'message': 'Hello, World!', 'timestamp': timestamp}
    return json.dumps(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

