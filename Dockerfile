FROM python:3.7.4-buster

RUN adduser --disabled-password mappad

WORKDIR /home/mappad

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install psycopg2

COPY webapp webapp
COPY migrations migrations
COPY wsgi.py ./
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP webapp

RUN chown -R mappad:mappad ./
USER mappad

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
