FROM python:3.8-slim-buster

WORKDIR /app/

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev

ARG REQUIREMENTS_FILE_NAME=production.txt
COPY requirements /app/requirements
RUN pip install --no-cache-dir -r /app/requirements/$REQUIREMENTS_FILE_NAME

COPY docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
COPY . /app

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
