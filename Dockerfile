FROM python:2.7.16-alpine3.9

WORKDIR /root

RUN pip install kafka-python
RUN pip install pymongo

COPY consumer.py consumer.py

ENTRYPOINT ["python", "consumer.py"]