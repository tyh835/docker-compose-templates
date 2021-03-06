FROM python:3.7-alpine

RUN apk update && apk add libpq

WORKDIR /flask-app

COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc python-dev musl-dev postgresql-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
          | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
          | sort -u \
          | xargs -r apk info --installed \
          | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.app:create_app()"
