from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

@app.route('/vfloat/<float:balance>')
def vfloat(balance):
    return "My Account Balance %f" % balance

app.run(debug=True)