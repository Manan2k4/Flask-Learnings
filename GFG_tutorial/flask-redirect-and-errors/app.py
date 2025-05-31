from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['post', 'get'])
def login():
    if request.method == 'post' and request.form['username'] == "admin":
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == "__main__":
    app.run(debug=True)