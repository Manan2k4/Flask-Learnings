from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username} !'

@app.route('/hello')
def hello():
    return "Hello, welcome to GeeksForGeeks"

@app.route('/')
def index():
    return "Homepage of GeeksForGeeks"

if __name__ == '__main__':
    app.run(debug=True)