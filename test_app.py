# ================================================================
# fastapi-mini-jc / test_app.py
# ------------------------------------------------
# Pruebas unitarias simples con pytest y TestClient.
# Demuestran cómo validar endpoints, estados HTTP y payloads.
# ================================================================

# Importamos TestClient para simular peticiones HTTP contra la app.
from fastapi.testclient import TestClient
# Importamos la aplicación FastAPI desde app.py.
from app import app

# Instanciamos el cliente una única vez para todas las pruebas.
client = TestClient(app)

def test_health():
    # Hacemos una petición GET a /health.
    resp = client.get("/health")
    # Debe retornar 200 OK.
    assert resp.status_code == 200
    # Y el JSON debe contener {"status": "ok"}.
    assert resp.json()["status"] == "ok"

def test_crud_item():
    # Definimos un payload válido para crear un ítem.
    payload = {"name": "book", "price": 9.9}

    # CREATE: enviamos POST /items/1 con el JSON.
    r_post = client.post("/items/1", json=payload)
    # Esperamos 200 OK (por defecto FastAPI devuelve 200 en POST si no especificamos otro).
    assert r_post.status_code == 200
    # La respuesta debe contener el id y los datos enviados.
    data = r_post.json()
    assert data["id"] == 1 and data["name"] == "book" and abs(data["price"] - 9.9) < 1e-9

    # READ: consultamos el ítem creado con GET /items/1.
    r_get = client.get("/items/1")
    assert r_get.status_code == 200
    assert r_get.json()["name"] == "book"

    # UPDATE: reemplazamos el recurso con PUT /items/1.
    new_payload = {"name": "notebook", "price": 12.5}
    r_put = client.put("/items/1", json=new_payload)
    assert r_put.status_code == 200
    assert r_put.json()["name"] == "notebook"

    # DELETE: borramos con DELETE /items/1.
    r_del = client.delete("/items/1")
    assert r_del.status_code == 200
    assert r_del.json()["status"] == "deleted"

    # READ inexistente: ahora debe dar 404.
    r_missing = client.get("/items/1")
    assert r_missing.status_code == 404
