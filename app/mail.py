from flask_mail import Message
from app.extensions import mail

def send_email(subject, recipients, body):
    from app import app  # Import here to avoid circular import issues

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipients])
    msg.body = body
    with app.app_context():
        mail.send(msg)
