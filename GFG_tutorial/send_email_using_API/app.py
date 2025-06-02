from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='onethat326@gmail.com'
app.config['MAIL_PASSWORD']='cnqk xrmg dgal pupk'
app.config['MAIL_USE_TLS']=True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message(
            subject='Mail via Flask',
            sender='onethat326@gmail.com',
            recipients=['23dce112@charusat.edu.in',
                        '23dce102@charusat.edu.in']
        )
    msg.cc=['ghoniyamanan@gmail.com']
    msg.html = """
    <p><b>મિત્રો</b>, (oh..Wrong Script)</p>
    <p>કેમ છો બધા? આશા રાખું છું કે મજામાં જ હશો. તમને બધાને જણાવી દઉં કે આ ઇમેઇલ મેં કોઈ નોર્મલ રીતે નથી મોકલ્યો, પણ પાયથનના કોડથી, ફ્લાસ્ક-મેઇલનો ઉપયોગ કરીને સીધો તમારા ઇનબોક્સમાં પહોંચાડ્યો છે. આવા મેઇલિંગના કામ માટે હું છું હો! 😉</p>
    <p><a href="https://linkedin.com/in/manan-ghoniya">LinkedIn</a></p>
    <p><a href="https://github.com/manan2k4">Github</p></a>
    <p>Resume ⬇️</p>
    """
    with app.open_resource("static/Manan ghoniya.pdf") as pdf:
        msg.attach(
            filename="Manan_Resume.pdf",
            content_type="application/pdf",
            data=pdf.read()
        )
    mail.send(msg)
    return '<h1>Email Sent</h1>'

if __name__ =='__main__':
    app.run(debug=True)