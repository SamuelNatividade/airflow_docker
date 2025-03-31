FROM apache/airflow:2.10.5
FROM python:3.10
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
