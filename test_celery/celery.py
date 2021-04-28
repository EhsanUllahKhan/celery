from __future__ import absolute_import
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672',include=['test_celery.tasks'])


if __name__ == '__main__':
    app.start()

# to start celery worker locally
# celery -A test_celery.tasks worker --loglevel=INFO