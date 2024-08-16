from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from google.cloud import bigquery
import os

app = FastAPI(version="0.0.2")

def query_bigquery(query):
    # Replace with your BigQuery project, dataset, and table
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    return results

def construct_query(data):
    pass

@app.get("/version")
def get_version():
    return {"app_version": app.version}

@app.post("/input")
async def query_data(request: Request):
    data = await request.json()
    # Extract query parameters from JSON data
    uid = data['uid']
    password = data['password']
    query = construct_query(data)  # Function to build BigQuery query
    # results = query_bigquery(query)
    result = {"message":"successful",
    "id":id,
    "password":password}
    return result
