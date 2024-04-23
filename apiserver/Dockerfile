FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./message_server /code/message_server
WORKDIR /code/message_server
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "80"]
