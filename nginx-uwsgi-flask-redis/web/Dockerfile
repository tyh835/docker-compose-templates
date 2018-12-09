FROM alpine:3.8

ENV PATH /usr/local/bin:$PATH

RUN apk update
RUN apk add --no-cache \
        uwsgi-python3 \
        python3

RUN pip3 install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD uwsgi --socket 0.0.0.0:4000 \
          --buffer-size=32768 \
          --enable-threads \
          --manage-script-name \
          --master \
          --mount /app=app:app \
          --plugin python3 \
          --processes 2 \
          --protocol uwsgi \
          --thunder-lock \
          --uid uwsgi
