from celery import Celery
from app import app

celery_service = Celery(
    "mailing_tasks",
    broker=app.config.get("broker_url", "redis://localhost:6379/0"),
    backend=app.config.get("result_backend", "redis://localhost:6379/0")
)

celery_service.conf.update(app.config)

# Ensure tasks run inside Flask app context
class ContextTask(celery_service.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return super().__call__(*args, **kwargs)

celery_service.Task = ContextTask
