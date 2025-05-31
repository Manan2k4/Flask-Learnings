from flask import Flask
app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome to the GFG"

app.run(debug=True)