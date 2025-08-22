from flask_mail import Message
from flask import current_app
from app.extensions import mail
from celery import shared_task

@shared_task(ignore_result=False)
def send_async_email(subject, recipients, body):
    msg = Message(
        subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[recipients],
    )
    msg.body = body
    mail.send(msg)
