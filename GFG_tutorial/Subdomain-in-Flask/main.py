from flask import Flask

app = Flask(__name__)

# to run manan.app:5000, change "localhost" hosts file
# at 


@app.route('/')
def home():
    return "Welcome to GeeksForGeeks !"


@app.route('/basic/')
def basic():
    return "Basic Category Articles " \
           "listed on this page."


@app.route('/', subdomain ='practice')
def practice():
    return "Coding Practice Page"


@app.route('/courses/', subdomain ='practice')
def courses():
    return "Courses listed " \
           "under practice subdomain."


if __name__ == "__main__":
    
    app.run(host='manan.app')