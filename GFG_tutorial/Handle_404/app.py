from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Home Page</h1>"

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run()