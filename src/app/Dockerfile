FROM python:3.9.7-slim-buster

WORKDIR /src/app

COPY requirements.txt ./

# RUN apt-get update

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# gunicorn --bind 0.0.0.0:5000 app:app
CMD [ "gunicorn", "-k", "eventlet", "-w", "1", "--bind", "0.0.0.0:5000", "app:app" ]
