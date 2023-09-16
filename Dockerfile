FROM python:3.9

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev default-libmysqlclient-dev

RUN pip install -r requirements.txt

EXPOSE 800

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]