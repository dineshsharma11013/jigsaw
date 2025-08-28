from flask import current_app
from flask_mail import Message
from app.extensions import mail
import logging

from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task(name="send_async_email")
def send_async_email(subject, recipients, body):
    try:
        app = current_app._get_current_object()  # get real Flask app
        with app.app_context():
            msg = Message(
                subject,
                sender=app.config['MAIL_USERNAME'],
                recipients=[recipients] if isinstance(recipients, str) else recipients,
            )
            msg.body = body
            mail.send(msg)
            return f"✅ Email sent to {recipients}"
    except Exception as e:
        logger.error(f"❌ Failed to send email to {recipients}: {e}", exc_info=True)
        return f"❌ Error sending email: {str(e)}"
    finally:
        logger.info(f"Email task finished for {recipients}")
