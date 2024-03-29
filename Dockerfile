# Use an official Python runtime as the base image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 9999
CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]