import os
import uvicorn
from fastapi import FastAPI,Request
from models import CanInput

app_version = "0.0.0"  # Store version information (optional)
app = FastAPI(version=app_version)


app = FastAPI(version="0.0.2")

def query_bigquery(query):
    # Replace with your BigQuery project, dataset, and table
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    return results

def construct_query(request):
    pass

@app.get("/version")
def get_version():
    return {"message": f"Hello! This is version {app_version} of my application."}

@app.post("/input")
async def query_data(request: CanInput):
    # Extract query parameters from JSON data
    uid = request.uid
    num_id = request.num_id
    query = construct_query(request)  # Function to build BigQuery query
    # results = query_bigquery(query)
    result = {"message":"successful",
    "uid":uid,
    "num_id":num_id}
    return result