import os

from fastapi import FastAPI

app = FastAPI()
app_version = "0.0.0"  # Store version information (optional)

@app.get("/test")
async def hello_world():
    return {"message": f"Hello! This is version {app_version} of my application."}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))