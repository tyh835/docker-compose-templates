FROM alpine:3.8

ENV PATH /usr/local/bin:$PATH

RUN apk update
RUN apk add uwsgi-python3 python3

RUN pip3 install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4000

ENV PYTHONBUFFERED true
ENV FLASK_APP app.py

CMD uwsgi --ini conf.ini --mount /app=app:app --socket 0.0.0.0:4000
