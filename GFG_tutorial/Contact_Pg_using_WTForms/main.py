from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "your-secret-key-here"  # Change this to a real secret key

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    message = TextAreaField(label='Message')
    submit = SubmitField(label="Submit")

@app.route('/', methods=['GET', 'POST'])
def home():
    cform = ContactForm()
    if cform.validate_on_submit():
        print(f"Name: {cform.name.data}, Email: {cform.email.data}, Message: {cform.message.data}")
    return render_template('contact.html', form=cform)

if __name__ == '__main__':
    app.run(debug=True)