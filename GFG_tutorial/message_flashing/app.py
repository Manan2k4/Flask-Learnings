from flask import *

app = Flask(__name__)
app.secret_key = 'GeeksForGeeks'

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/profile')
def row():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['pass'] != 'GFG':
            error = 'Invalid Password'
        else:
            flash('You are successfully login into Flask application')
            return redirect(url_for('row'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)