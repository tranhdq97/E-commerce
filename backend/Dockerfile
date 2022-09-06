FROM python:3.9.12

ENV PYTHONUNBUFFERED 1
ENV DJANGO_APP_TARGET ''
ENV PORT 8000

EXPOSE 8000

WORKDIR /app

RUN apt-get update && apt-get install -y gettext
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN rm -rf venv ec_customer ec_staff ec_storage
