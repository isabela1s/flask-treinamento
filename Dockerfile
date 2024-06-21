FROM python:3.11-slim-buster

RUN apt update
RUN apt install -y build-essential python3-dev libpq-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY web/. .

CMD flask run --debug --host 0.0.0.0