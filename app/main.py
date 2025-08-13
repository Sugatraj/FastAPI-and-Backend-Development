from fastapi import FastAPI
from typing import Any
import random

app = FastAPI()

@app.get("/readme")
def readme() -> dict[str, Any]:
    random_name = ["Coolie Powerhouse", "Say My Name", "God Damn Right"]
    random_badge_no = ["1421", "786", "131313", "007", "1950"]
    return {
        "name" : random.choice(random_name),
        "badge_no" : random.choice(random_badge_no)
    }

@app.get("/shipment/{id}")
def shipmentData(id : int) -> dict[str, Any | list[str]]:
    random_status = ["ok", "not so ok", "ok ok"]
    random_id = random.randint(1,121)
    return {
        "shipment_id" : random_id,
        "shipment_status" : random.choice(random_status)
    }