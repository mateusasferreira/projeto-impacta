FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    netcat-traditional \
    libpq-dev \
    postgresql

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
