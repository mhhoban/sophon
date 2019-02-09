FROM python:3.7-alpine

COPY requirements.txt /app/requirements.txt
COPY sophon_app.py /app/sophon_app.py

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["/usr/local/bin/gunicorn", "sophon_app:app", "-b", "0.0.0.0:80"]
