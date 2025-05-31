from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! this application running on 192.168.137.1'

if __name__ == '__main__':
    app.run(host='192.168.137.1', debug=True)   # MY IP ADDR...