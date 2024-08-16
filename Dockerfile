FROM python:3.9-slim-buster  # Base image

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]