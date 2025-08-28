# jigsaw/app/celery.py
from celery import Celery

celery = Celery(
    "app",
    broker="redis://localhost:6379/0",        
    backend="redis://localhost:6379/0",       
)

def init_celery(flask_app):
    celery.conf.update(flask_app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
