from flask import Flask, request, render_template
import os

app = Flask(__name__)

app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route('/')
def home():
    return render_template('squarenum.html')

@app.route('/square', methods=['GET', 'POST'])
def squarenumber():
    if request.method == 'POST':
        num = request.form.get('num')
        if not num or not num.strip():
            return "<h1>Please enter a number</h1>"
        try:
            square = int(num) ** 2
            return render_template('answer.html',
                                   squareofnum=square,
                                   num=num)
        except ValueError:
            return "<h1>Invalid number - please enter a numeric value</h1>"
    return render_template('squarenum.html')

if __name__ == '__main__':
    app.run(debug=True)