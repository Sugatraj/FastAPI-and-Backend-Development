from fastapi import FastAPI
from typing import Any

app = FastAPI()

shipments = {
    121: {
    "name" : "Coolie Powerhouse",
    "badge_no" : "1421",
    "shipment_status" : "Powerful"
    },
    122: {
    "name" : "Say My Name",
    "badge_no" : "786",
    "shipment_status" : "Delivered"
    },
    123: {
    "name" : "God Damn Right",
    "badge_no" : "131313",
    "shipment_status" : "In Transit"
    },
    124: {
    "name" : "Breaking Bad",
    "badge_no" : "007",
    "shipment_status" : "Pending"
    },
    125: {
    "name" : "Walter White",
    "badge_no" : "1950",
    "shipment_status" : "Cancelled"
    },
    126: {
    "name" : "Jesse Pinkman",
    "badge_no" : "999",
    "shipment_status" : "Returned"
    }
}

@app.get("/")
def welcome():
    return {"message" : "Welcome to FastAPI world"}

@app.get("/latest")
def latest() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipments/")
def shipmentData(id : int) -> dict[str, Any | list[str]]:
    if id not in shipments:
        return {"error" : f"Shipment for id : {id} not found"}
    return shipments[id]