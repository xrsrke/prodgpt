from logging import send_inference_log_to_mongo

from fastapi import FastAPI, HTTPException, status
from schema import InferenceLog

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Check out my project: github/xrsrke/prodgpt"}


@app.post("/monitoring/inference")
def monitor_inference(request: InferenceLog):
    try:
        send_inference_log_to_mongo(request.dict())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not send inference log to MongoDB"
        )
    else:
        return {"message": "Inference log sent to MongoDB"}


@app.get("/blog")
def blog():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Blog not found"
    )
