from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection
csrf = CSRFProtect(app)  # Enable CSRF Protection

# Creating a FlaskForm to manage CSRF properly
class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            flash(f'Hello {name} from Protected Form!', 'success')
            return render_template('index.html', form=form)
        else:
            flash('CSRF Token Missing or Invalid!', 'danger')

    return render_template('index.html', form=form)

@app.route("/unprotected_form", methods=['POST'])
def unprotected_form():
    name = request.form.get('Name', '').strip()
    if not name:
        return "Error: Name is required!", 400
    return f'Hello {name} from Unprotected Form!'

if __name__ =='__main__':
    app.run(debug=True)