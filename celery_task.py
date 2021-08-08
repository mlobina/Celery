from celery import Celery
import yagmail
from app import app
from models import User


def make_celery(app):
    """configure Celery’s broker and backend to use Redis, create a celery application """

    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/3',
        broker='redis://localhost:6379/4'
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task()
def send_email():
    """define the task"""

    users = User.query.all()
    emails = [user.email for user in users]
    try:
        # initializing the server connection
        yag = yagmail.SMTP(user=app.config['SENDER_EMAIL'], password=app.config['SENDER_PASSWORD'])
        # sending the email
        yag.send(to=emails, subject=app.config['EMAIL_SUBJECT'], contents=app.config['CONTENTS'])
        return "Email sent successfully"
    except:
        return "Error, email was not sent"
