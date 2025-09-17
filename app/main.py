from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.storage import store_data, query_data

app = FastAPI()

class DataPoint(BaseModel):
    timestamp: str
    value: float

@app.post("/data")
def receive_data(data: DataPoint):
    """Recibe un punto de datos con timestamp y valor."""
    try:
        store_data(data.timestamp, data.value)
        return {"status": "Data stored"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/query")
def query_by_interval(start: str, end: str):
    """Consulta los datos en un intervalo de fecha y hora."""
    try:
        results = query_data(start, end)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))