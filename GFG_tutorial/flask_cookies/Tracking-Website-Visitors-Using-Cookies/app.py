from flask import Flask, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def visitors_count():
    count = int(request.cookies.get('visitors count', 0))
    count = count + 1
    output = 'You visited this page for ' + str(count) + ' times'
    resp = make_response(output)
    resp.set_cookie('visitors count', str(count))
    return resp

@app.route('/get')
def get_visitors_count():
    count = request.cookies.get('visitors count')
    return count

app.run()