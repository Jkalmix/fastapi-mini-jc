# fastapi-mini-jc

Mini API en **FastAPI** con endpoints CRUD en memoria y **pruebas unitarias** con `pytest`. Útil para demostrar:
- Código limpio (PEP8), tipado y Pydantic.
- REST básico (GET/POST/PUT/DELETE).
- Testing con `TestClient`.

## Requisitos
```bash
pip install -r requirements.txt
```

## Ejecutar la API
```bash
uvicorn app:app --reload
```
Abrir: http://127.0.0.1:8000/docs

## Ejecutar pruebas
```bash
pytest -q
```
