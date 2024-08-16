FROM python:3.9-slim-buster  # Base image
WORKDIR /app

COPY . app/.
RUN pip3 install -r /app/requirements.txt

CMD ["uvicorn", "main:app","--host=0.0.0.0", "--port=8080","--reload"]