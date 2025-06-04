from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

client = MongoClient('mongodb://localhost:27017/')
db = client['demo']
collection = db['data']

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)

    return 'Data added to MongoDB'

if __name__ == '__main__':
    app.run()