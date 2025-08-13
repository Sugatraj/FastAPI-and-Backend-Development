from fastapi import FastAPI
from typing import Any
import random

app = FastAPI()

@app.get("/shipment/{id}")
def shipmentData(id : int) -> dict[str, Any | list[str]]:
    random_status = ["ok", "not so ok", "ok ok"]
    random_id = random.randint(1,121)
    return {
        "shipment_id" : random_id,
        "shipment_status" : random.choice(random_status)
    }