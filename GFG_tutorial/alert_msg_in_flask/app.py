from flask import Flask, request, flash, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username != 'admin' or password != 'admin':
            flash('❌ Invalid username or password', 'error')
        else:
            flash('✅ Succussfully logged in!', 'success')
            return redirect(url_for('index'))
    
    return render_template('login.html')