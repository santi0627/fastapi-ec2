from app.storage import store_data, query_data

def test_store_and_query():
    # Limpiar almacenamiento (solo si haces pruebas repetidas)
    from app.storage import data_storage
    data_storage.clear()

    store_data("2025-09-10T10:00:00", 10.5)
    store_data("2025-09-10T12:00:00", 20.0)
    store_data("2025-09-10T14:00:00", 30.5)

    result = query_data("2025-09-10T09:00:00", "2025-09-10T13:00:00")

    assert len(result) == 2
    assert result[0]["value"] == 10.5
    assert result[1]["value"] == 20.0
