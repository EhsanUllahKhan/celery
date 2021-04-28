FROM python:3.8
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A test_celery worker --concurrency=20 --loglevel=info