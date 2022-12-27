import logging.config
import pickle
import os

import pandas as pd
import numpy as np
from fastapi import FastAPI

from request_item import RequestItem

logger = logging.getLogger(__name__)
app = FastAPI()
logging.error(os.getcwd())
with open(f'{os.getcwd()}/model/model.pickle', 'rb') as handle:
    model = pickle.load(handle)


@app.post("/")
async def valuate(request: RequestItem):
    df = pd.DataFrame([request.__dict__])
    y = model.predict(df.values.tolist())

    return {'prediction': round(np.exp(y[0]), -2)}
