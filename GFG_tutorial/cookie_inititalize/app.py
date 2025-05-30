from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('cookie.html', user=user))
        resp.set_cookie('UserID', user)
        return resp
    return render_template('index.html')

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('UserID')
    if not name:
        return '<h1>No cookie found! Please set one first. 🍪</h1>'
    return f'<h1>Welcome, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
