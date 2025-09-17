from datetime import datetime
from typing import List

# Simulación de almacenamiento en memoria
data_storage = []

def store_data(timestamp: str, value: float):
    """Guarda un punto de datos."""
    data_storage.append({
        "timestamp": timestamp,
        "value": value
    })

def query_data(start: str, end: str) -> List[dict]:
    """Consulta datos en un rango de fechas."""
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    return [item for item in data_storage if start_dt <= datetime.fromisoformat(item["timestamp"]) <= end_dt]