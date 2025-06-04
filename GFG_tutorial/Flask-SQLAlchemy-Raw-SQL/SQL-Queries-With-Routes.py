from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import urllib.parse

app = Flask(__name__)

db_cred = {
    'user': 'root',
    'pass': 'Manan2k4@MySQL',  # has @ in it!
    'host': '127.0.0.1',
    'name': 'demo'
}

# URL-encode password
encoded_password = urllib.parse.quote_plus(db_cred['pass'])

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{db_cred['user']}:{encoded_password}@{db_cred['host']}/{db_cred['name']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/get_results', methods=['POST'])
def get_results():
    try:
        data = request.get_json()
        query = data.get('query')

        with db.engine.connect() as connection:
            result = connection.execute(text(query))
            return {f"Record {i}": list(row) for i, row in enumerate(result, start=1)}

    except Exception as e:
        print("❌ Error in /get_results:", e)
        return {"message": "Internal server error", "error": str(e)}, 500
    
@app.route('/execute_query', methods=['POST'])
def execute_query():
    try:
        query = request.get_json()['query']
        with db.engine.begin() as conn:  # begin() gives transaction context
            conn.execute(text(query))
    except Exception as e:
        print("❌ Error in /execute_query:", e)
        return {"message": "Request could not be completed."}, 400
    return {"message": "Query executed successfully."}
if __name__ == '__main__':
    app.run(debug=True)
