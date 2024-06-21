FROM python:3.11-slim-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY web/. .

CMD flask run --debug --host 0.0.0.0