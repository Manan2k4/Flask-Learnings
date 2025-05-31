from flask import Flask, redirect, render_template, request, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form.get('username', '').strip()
        print(f"Received username: '{username}'")  # Debug print
        
        if username == "admin":
            return redirect(url_for("success"))
        else:
            flash('Invalid username! Try "admin"')
    
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Login successful! Welcome, admin!"

if __name__ == '__main__':
    app.run(debug=True)