FROM python:2.7.16-alpine3.9

WORKDIR /consumer

COPY consumer.py .
COPY requirements.txt .

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "consumer.py"]
