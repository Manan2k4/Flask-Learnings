from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, Welcome to GeeksForGeeks'

@app.route('/')
def index():
    return "Homepage of GeeksForGeeks"

if __name__ == '__main__':
    app.run(debug=True)