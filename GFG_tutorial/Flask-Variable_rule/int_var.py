from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

@app.route('/vint/<int:age>')
def vint(age):
    return "I am %d years old " % age

app.run(debug=True)