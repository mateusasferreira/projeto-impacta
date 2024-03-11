FROM python:3.10

RUN apt-get update && apt-get install -y \
    netcat-traditional \
    libpq-dev postgresql \
    postgresql-contrib

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
