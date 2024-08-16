FROM python:3.9-slim-buster  # Base image
WORKDIR /app

COPY . app/.
RUN pip3 install --no-cache -r /app/requirements.txt
EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]