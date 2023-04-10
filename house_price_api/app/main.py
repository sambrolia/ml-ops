import logging.config
import pickle
import os
import uvicorn

import pandas as pd
import numpy as np
from fastapi import FastAPI, Response, HTTPException

import prometheus_client
from prometheus_client import Counter, Histogram, CollectorRegistry

import random

from pydantic import ValidationError
from .request_item import RequestItem

logger = logging.getLogger(__name__)
app = FastAPI()

custom_registry = CollectorRegistry()

logging.error(os.getcwd())
with open(f'model/model.pickle', 'rb') as handle:
    model = pickle.load(handle)

missing_params_counter = Counter(
    "missing_params_count_total",
    "Counts the number of times input parameters are missing",
    registry=custom_registry)

prediction_distribution = Histogram(
    "prediction_distribution",
    "Histogram of predicted house prices",
    buckets=[0, 100000, 250000, 500000, 750000, 1000000, 2000000, 5000000, float("inf")],
    registry=custom_registry)

@app.get("/metrics")
async def get_metrics():
    return Response(prometheus_client.generate_latest(custom_registry), media_type=prometheus_client.CONTENT_TYPE_LATEST)


@app.post("/")
async def valuate(request: dict):
    required_params = ["bed", "bath", "acre_lot", "zip_code", "house_size"]
    missing_params = [param for param in required_params if param not in request]

    if missing_params:
        missing_params_counter.inc()
        error_msg = ", ".join(missing_params)
        raise HTTPException(status_code=422, detail=f"Missing parameters: {error_msg}")

    try:
        request_item = RequestItem(**request)
    except ValidationError as e:
        error_msg = ", ".join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
        raise HTTPException(status_code=422, detail=f"Invalid parameters: {error_msg}")

    y = model.predict(np.array(list(request_item.dict().values())).reshape(1, -1))

    # Record the prediction in the histogram
    prediction = round(np.exp(y[0]), -2)
    prediction_distribution.observe(prediction)

    return {'prediction': prediction}



async def generate_initial_data():
    sample_data = [
         {
            "bed": random.randint(1, 10),
            "bath": random.uniform(1, 5),
            "acre_lot": random.uniform(0.5, 10),
            "zip_code": random.randint(10000, 99999),
            "house_size": random.randint(500, 5000),
        }
        for _ in range(100)
    ]

    for data in sample_data:
        if random.random() < 0.3:  # 30% chance of missing a field
            del data[random.choice(list(data.keys()))]

        try:
            await valuate(data)
        except HTTPException as e:
            logger.error(f"Error during generate_initial_data: {e.detail}")



app.add_event_handler("startup", generate_initial_data)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
