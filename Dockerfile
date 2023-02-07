FROM python:3.10

WORKDIR /fruit_world

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["python", "./app./server.py"]

EXPOSE 5000