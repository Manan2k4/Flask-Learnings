from flask import Flask

app = Flask(__name__)

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the id {id}'

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}'

@app.route('/hello')
def hello():
    return "Hello, Welcome to GeeksForGeeks"

@app.route('/')
def index():
    return "Homepage of GeeksForGeeks"

if __name__ == '__main__':
    app.run(debug=True)