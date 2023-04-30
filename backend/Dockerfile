FROM python:3.11.1-slim-buster
WORKDIR /app/

COPY ./requirements.txt /app/
RUN pip install -r requirements

COPY ./ /app/

CMD uvicorn --host=0.0.0.0 --port 80 main:app