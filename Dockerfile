FROM python:3.8-alpine
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN adduser -D myuser
RUN apk update && apk add python3-dev gcc g++ libc-dev musl-dev linux-headers
RUN /usr/local/bin/python -m pip install flask uWSGI
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "app/app.ini"]
