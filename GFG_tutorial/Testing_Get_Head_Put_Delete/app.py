from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        if user:
            return redirect(url_for('success', name=user))
        else:
            return "name not provided in POST", 400
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)