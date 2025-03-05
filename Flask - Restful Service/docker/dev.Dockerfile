FROM python:3.7-alpine

WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install debugpy flask -t /tmp
COPY docker/requirements.txt /
RUN pip install -r /requirements.txt
EXPOSE 5000
ENV FLASK_APP=flaskr
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["flask", "run"]