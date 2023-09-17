FROM python:3.11.5-slim

WORKDIR /MC426

COPY requirements.txt requirements.txt 
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-u", "-m", "flask", "run", "--host=0.0.0.0"]