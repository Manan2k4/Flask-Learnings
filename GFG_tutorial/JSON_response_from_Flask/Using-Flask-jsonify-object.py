from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/returnjson', methods=['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules": 15,
            "Subject": "DSA",
        }

        return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)