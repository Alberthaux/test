from rucoh import app
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'berthaux.alice@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)
my_email=app.config['MAIL_USERNAME']


def send_message(
        user_name,
        user_email,
        message
):
    msg = Message(
        sender=my_email,
        recipients=[user_email])
    msg.body = f'Message from {user_name}: ' + message
    #mail.send(msg)
